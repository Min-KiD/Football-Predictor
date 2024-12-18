import sys
sys.dont_write_bytecode = True

import ast
import random
import time
from io import StringIO
import requests
import pandas as pd
from datetime import timedelta, datetime
import json
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def add_driver_options(options):
    """
    Add configurable options
    """
    chrome_options = Options()
    for opt in options:
        chrome_options.add_argument(opt)
    return chrome_options


def initialize_driver(proxy_server=None):
    """
    Initialize the web driver
    """
    driver_config = {
        "options": [
            "--headless",
            "--no-sandbox",
            # "--start-fullscreen",
            "--allow-insecure-localhost",
            "--disable-dev-shm-usage",
            "user-agent=Chrome/116.0.5845.96"
        ],
    }
    if proxy_server:
        driver_config["options"].append(f"--proxy-server={proxy_server}")
    options = add_driver_options(driver_config["options"])
    driver = webdriver.Chrome(options=options)
    return driver


# Get free proxies for rotating
def get_free_proxies():
    driver = initialize_driver()
    driver.get('https://sslproxies.org')

    table = driver.find_element(By.TAG_NAME, 'table')
    thead = table.find_element(By.TAG_NAME, 'thead').find_elements(By.TAG_NAME, 'th')
    tbody = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

    headers = []
    for th in thead:
        headers.append(th.text.strip())

    proxies = []
    for tr in tbody:
        proxy_data = {}
        tds = tr.find_elements(By.TAG_NAME, 'td')
        for i in range(len(headers)):
            proxy_data[headers[i]] = tds[i].text.strip()
        if proxy_data['Code'] == 'VN':
            continue
        proxies.append(proxy_data)

    return proxies


def get_team_stats(team, links_dict):
    link_suffix = links_dict[team]
    driver = initialize_driver()
    driver.get(f'https://www.whoscored.com{link_suffix}')

    table_xpath = '//*[@id="statistics-team-table-summary"]'
    wait = WebDriverWait(driver, 300)
    table_element = wait.until(EC.presence_of_element_located((By.XPATH, table_xpath)))

    heads = table_element.find_elements(By.CSS_SELECTOR, 'thead > tr > th')
    heads = [head.text for head in heads]
    heads = heads[1:4] + heads[5:]

    rows = table_element.find_elements(By.CSS_SELECTOR, 'tbody > tr')
    data = []
    for row in rows:
        row_data = row.find_elements(By.CSS_SELECTOR, 'td')
        if row_data[0].text == 'Premier League':
            row_data = [row_datum.text for row_datum in row_data]
            data = row_data[1:4] + row_data[5:]
            break

    return {team: {k: v for k, v in zip(heads, data)}}


def get_teams_stats_multithread(team1, team2):
    with open("data/links.json", 'r') as file:
        links_dict = json.load(file)

    response = {}
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = {
            executor.submit(get_team_stats, team, links_dict): team
            for team in [team1, team2]
        }
        for future in futures:
            result = future.result()
            response.update(result)

    return response if response else None


def get_latest_match(team1, team2, date):
    """
    Get latest match between 2 teams, up to date (DD-MM-YY)
    """
    driver = initialize_driver()
    date_limit = list(map(int, date.split('-')[::-1]))
    with open("data/links.json", 'r') as file:
        links_dict = json.load(file)
    link_suffix = links_dict[team1]
    link_suffix = link_suffix.replace('Show', 'Fixtures')
    team2_name = links_dict[team2][links_dict[team2].index('England') + 8:].replace('-', ' ')

    driver.get(f'https://www.whoscored.com{link_suffix}')

    wait = WebDriverWait(driver, 300)
    select = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#team-fixture-tournaments')))
    select = Select(select)
    select.select_by_visible_text('Premier League')
    wait = WebDriverWait(driver, 300)
    fixture = wait.until(EC.presence_of_element_located((By.ID, 'team-fixtures')))

    rows = fixture.find_elements(By.CLASS_NAME, 'divtable-row')
    for row in rows[::-1]:
        dates = row.find_elements(By.CLASS_NAME, 'date')
        dates = list(map(lambda ele: ele.text, dates))
        date = list(filter(lambda date: date != '', dates))[0]
        date = list(map(int, date.split('-')[::-1]))
        if date > date_limit:
            continue
        away = row.find_element(By.CLASS_NAME, 'away').text
        if away == team2_name:
            match_link = row.find_element(By.CLASS_NAME, 'result-1').get_attribute('href')
            return match_link

    return None


def get_data_half(match_link):
    # scrapingH
    driver = initialize_driver()
    driver.get(match_link)

    # get the JSON data
    data_xpath = '/html/body/div[4]/script[1]'
    wait = WebDriverWait(driver, 300)
    data_element = wait.until(EC.presence_of_element_located((By.XPATH, data_xpath)))
    data = data_element.get_attribute('innerHTML')
    start_index = data.find('matchCentreData')
    end_index = data.find('matchCentreEventTypeJson')

    data = data[start_index + 17:end_index - 14]
    data = json.loads(data)

    # extract event data
    event_data = data['events']
    event_data = pd.DataFrame(event_data)

    # get the match date to crawl ELO rating data
    date = data['startTime'][:-9]
    ddate = datetime.strptime(date, '%Y-%m-%d')

    previous_day = ddate - timedelta(days=1)
    predate = previous_day.strftime('%Y-%m-%d')

    # get data from clubelo api
    r = requests.get('http://api.clubelo.com/' + predate)
    elo_data = StringIO(r.text)
    elo = pd.read_csv(elo_data, sep=",")

    # get team name
    name_xpath = '/html/body/div[4]/div[3]/div[1]/div[2]/table/tbody/tr[1]'
    wait = WebDriverWait(driver, 300)
    name_element = wait.until(EC.presence_of_element_located((By.XPATH, name_xpath)))
    name = name_element.get_attribute('innerHTML')

    end_index = name.find('</a>')
    start_index = name[:end_index].rfind('>')
    home_team_name = name[start_index + 1:end_index]

    # some team names need to be synchronized from Whoscored to clubelo
    if home_team_name == 'Man Utd': home_team_name = 'Man United'
    if home_team_name == 'WBA': home_team_name = 'West Brom'
    if home_team_name == 'Sheff Utd': home_team_name = 'Sheffield United'
    if home_team_name == 'Nottingham Forest': home_team_name = 'Forest'
    end_index = name.rfind('</a>')
    start_index = name[:end_index].rfind('>')
    away_team_name = name[start_index + 1:end_index]
    if away_team_name == 'Man Utd': away_team_name = 'Man United'
    if away_team_name == 'WBA': away_team_name = 'West Brom'
    if away_team_name == 'Sheff Utd': away_team_name = 'Sheffield United'
    if away_team_name == 'Nottingham Forest': away_team_name = 'Forest'

    # get elo ratings data
    home_team_elo = elo.loc[elo['Club'] == home_team_name, 'Elo'].values[0]
    away_team_elo = elo.loc[elo['Club'] == away_team_name, 'Elo'].values[0]

    # data_integration
    # default data instance
    game_data = [{
        'minute': 0,
        'half': 1,
        'ht_elo': home_team_elo,
        'at_elo': away_team_elo,
        'ht_goal': 0,
        'at_goal': 0,
        'pass': 0,
        'short_pass': 0,
        'long_pass': 0,
        'final_3rd_pass': 0,
        'key_pass': 0,
        'cross': 0,
        'corner': 0,
        'big_chance': 0,
        'shot': 0,
        'shot_6_yard_box': 0,
        'shot_penalty_box': 0,
        'shot_open_play': 0,
        'shot_fast_break': 0,
        'dispossessed': 0,
        'turnover': 0,
        'duel': 0,
        'tackle': 0,
        'interception': 0,
        'clearance': 0,
        'offside': 0,
        'yellow': 0,
        'red': 0,
        'result': 'D'
    }]
    # home team and away team id
    ht_id = data['home']['teamId']
    at_id = data['away']['teamId']

    # # transform data into dictionary type
    # event_data['period'] = event_data['period'].apply(ast.literal_eval)
    # event_data['type'] = event_data['type'].apply(ast.literal_eval)
    # event_data['satisfiedEventsTypes'] = event_data['satisfiedEventsTypes'].apply(ast.literal_eval)

    # iterate through event to calculate values of needed attributes
    new_event = game_data[-1].copy()
    for ind, event in event_data.iterrows():
        new_event['minute'] = event['minute']
        new_event['half'] = event['period']['value']

        # only create new data instance whenever the minute change
        if new_event['minute'] > game_data[-1]['minute'] or (
                new_event['half'] > game_data[-1]['half'] and new_event['half'] == 2):
            game_data.append(new_event.copy())

        # using dictionary from event['type']['value'] to determine event type
        if event['type']['value'] == 16:
            if 23 in event['satisfiedEventsTypes']:
                if event['teamId'] == ht_id:
                    new_event['at_goal'] += 1
                else:
                    new_event['ht_goal'] += 1
            else:
                if event['teamId'] == ht_id:
                    new_event['ht_goal'] += 1
                else:
                    new_event['at_goal'] += 1
        if 117 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['pass'] += 1
            else:
                new_event['pass'] -= 1
        if 30 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['short_pass'] += 1
            else:
                new_event['short_pass'] -= 1
        if 127 in event['satisfiedEventsTypes'] or 128 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['long_pass'] += 1
            else:
                new_event['long_pass'] -= 1
        if 217 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['final_3rd_pass'] += 1
            else:
                new_event['final_3rd_pass'] -= 1
        if 123 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['key_pass'] += 1
            else:
                new_event['key_pass'] -= 1
        if 125 in event['satisfiedEventsTypes'] or 126 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['cross'] += 1
            else:
                new_event['cross'] -= 1
        if 31 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['corner'] += 1
            else:
                new_event['corner'] -= 1
        if 203 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['big_chance'] += 1
            else:
                new_event['big_chance'] -= 1
        if 10 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['shot'] += 1
            else:
                new_event['shot'] -= 1
        if 0 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['shot_6_yard_box'] += 1
            else:
                new_event['shot_6_yard_box'] -= 1
        if 1 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['shot_penalty_box'] += 1
            else:
                new_event['shot_penalty_box'] -= 1
        if 3 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['shot_open_play'] += 1
            else:
                new_event['shot_open_play'] -= 1
        if 4 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['shot_fast_break'] += 1
            else:
                new_event['shot_fast_break'] -= 1
        if 70 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['dispossessed'] += 1
            else:
                new_event['dispossessed'] -= 1
        if 69 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['turnover'] += 1
            else:
                new_event['turnover'] -= 1
        if 197 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['duel'] += 1
            else:
                new_event['duel'] -= 1
        if 143 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['tackle'] += 1
            else:
                new_event['tackle'] -= 1
        if 101 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['interception'] += 1
            else:
                new_event['interception'] -= 1
        if 95 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['clearance'] += 1
            else:
                new_event['clearance'] -= 1
        if 61 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['offside'] += 1
            else:
                new_event['offside'] -= 1
        if 65 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['yellow'] += 1
            else:
                new_event['yellow'] -= 1
        if 68 in event['satisfiedEventsTypes']:
            if event['teamId'] == ht_id:
                new_event['red'] += 1
            else:
                new_event['red'] -= 1

    df = pd.DataFrame(game_data)

    # result attribute from home team goal and away team goal
    diff = game_data[-1]['ht_goal'] - game_data[-1]['at_goal']
    if diff > 0:
        df['result'] = 'W'
    elif diff < 0:
        df['result'] = 'L'

    selected_features_wrapper = ['half', 'ht_goal', 'at_goal', 'final_3rd_pass', 'key_pass', 'corner',
                                 'shot_6_yard_box', 'dispossessed', 'duel', 'tackle', 'interception', 'yellow', 'red']

    return df[selected_features_wrapper]


def generate_random_probabilities():
    win = round(random.uniform(0, 1), 4)
    draw = round(random.uniform(0, 1 - win), 4)
    lose = round(1 - win - draw, 4)
    return win, draw, lose


# driver = initialize_driver()
#
# team2 = 'manchester united'
# team1 = 'manchester city'
#
# start = time.time()
# link = get_latest_match(driver, team1, team2, '15-12-24')
# array = get_data_half(driver, link)
# print(array)
# print(f"Execution time: {time.time() - start}")