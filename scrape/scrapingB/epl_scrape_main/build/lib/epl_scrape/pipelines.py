# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pandas as pd
from scrapy.utils.project import get_project_settings


class MatchPipeline:

    def open_spider(self, spider):
        self.items = []

    def close_spider(self, spider):
        settings = get_project_settings()
        df = pd.DataFrame(self.items)
        df.to_csv(settings.get("MATCHES_CSV"), index=False)

    def process_item(self, item, spider):
        match_info, match_stats = item["match_info"], item["match_stats"]
        composed_data = {
            "match_id": match_info["id"],
            "season": match_info["gameweek"]["compSeason"]["label"],
            "date": match_info["kickoff"]["label"],
            "ground": match_info["ground"]["name"],
            "duration": match_info["clock"]["secs"],
            "outcome": match_info["outcome"],
        }

        for i in range(2):
            team_data = {}
            attr_prefix = "h_" if i == 0 else "a_"

            team_dict = match_info["teams"][i]
            name = team_dict["team"]["name"]
            team_id = str(team_dict["team"]["id"])
            score = team_dict["score"]
            formation = match_stats["data"][team_id]["M"]
            formation = [data for data in formation if data["name"] == "formation_used"]
            formation = formation[0]["value"]
            formation = str(int(formation))
            formation = "-".join(formation)
            players = [player["id"] for player in match_info["teamLists"][i]["lineup"]]

            team_data[attr_prefix + "name"] = name
            team_data[attr_prefix + "team_id"] = team_id
            team_data[attr_prefix + "score"] = score
            team_data[attr_prefix + "formation"] = formation
            team_data[attr_prefix + "players"] = players

            stats_list = match_stats["data"][team_id]["M"]
            for stat_dict in stats_list:
                stat_name = stat_dict["name"]
                if stat_name == "formation_used":
                    continue
                stat_value = stat_dict["value"]
                team_data[attr_prefix + stat_name] = stat_value

            composed_data.update(team_data)

        self.items.append(composed_data)
        return composed_data
