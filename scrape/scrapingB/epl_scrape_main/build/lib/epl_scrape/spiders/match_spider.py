import scrapy
import json


class MatchSpider(scrapy.Spider):
    name = "matches"

    def __init__(
        self, from_season="2023/24", to_season="2023/24", *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.from_year = int(from_season[:4])
        self.to_year = int(to_season[:4])

    def start_requests(self):
        url = "https://footballapi.pulselive.com/football/competitions/1/compseasons?page=0&pageSize=100&startDate=1992-01-01"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        season_ids_dict = {}
        data = json.loads(response.text)
        for season in data["content"]:
            season_year = int(season["label"][:4])
            if self.from_year <= season_year <= self.to_year:
                season_ids_dict[season["label"]] = str(int(season["id"]))
        for season, season_id in season_ids_dict.items():
            season_url = f"https://footballapi.pulselive.com/football/fixtures?comps=1&compSeasons={season_id}&page=0&pageSize=2000"
            yield response.follow(season_url, self.parse_season)

    def parse_season(self, response):
        data = json.loads(response.text)
        for match in data["content"]:
            match_id = str(int(match["id"]))
            info_url = f"https://footballapi.pulselive.com/football/fixtures/{match_id}?altIds=true"
            yield response.follow(info_url, self.parse_match_info)

    def parse_match_info(self, response):
        match_info = json.loads(response.text)
        match_id = match_info.get("id")
        stats_url = f"https://footballapi.pulselive.com/football/stats/match/{match_id}"
        yield response.follow(
            stats_url, self.parse_match_stats, meta={"match_info": match_info}
        )

    def parse_match_stats(self, response):
        match_info = response.meta.get("match_info")
        match_stats = json.loads(response.text)
        yield {"match_info": match_info, "match_stats": match_stats}
