import scrapy
import json
from epl_scrape.spiders.season_id_spider import get_season_ids


class MatchSpider(scrapy.Spider):
    name = "matches"

    def start_requests(self):
        for url in self.generate_urls():
            yield scrapy.Request(url=url, callback=self.parse)

    def generate_urls(self):
        season_ids = get_season_ids()
        base_url = "https://footballapi.pulselive.com/football/fixtures?comps=1&compSeasons={}&page=0&pageSize=2000"
        for season, season_id in season_ids.items():
            yield base_url.format(season_id)

    def parse(self, response, **kwargs):
        data = json.loads(response.text)
        for match in data['content']:
            match_id = str(int(match["id"]))
            data_url = f"https://footballapi.pulselive.com/football/fixtures/{match_id}?altIds=true"
            yield response.follow(data_url, self.parse_match_info)

    def parse_match_info(self, response):
        match_info = json.loads(response.text)
        match_id = match_info.get("id")
        stats_url = f"https://footballapi.pulselive.com/football/stats/match/{match_id}"
        yield response.follow(stats_url, self.parse_match_stats, meta={"match_info": match_info})

    def parse_match_stats(self, response):
        match_info = response.meta.get("match_info")
        match_stats = json.loads(response.text)
        yield {
            "match_info": match_info,
            "match_stats": match_stats
        }
