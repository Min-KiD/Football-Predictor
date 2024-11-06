from pathlib import Path

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import json


class SeasonIDSpider(scrapy.Spider):
    name = "season_ids"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        settings = get_project_settings()
        self.from_year = int(settings.get("FROM_SEASON")[:4])
        self.to_year = int(settings.get("TO_SEASON")[:4])
        self.output_file = settings.get("SEASON_IDS_JSON")
        self.season_ids_dict = {}

    def start_requests(self):
        url = "https://footballapi.pulselive.com/football/competitions/1/compseasons?page=0&pageSize=100&startDate=1992-01-01"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        data = json.loads(response.text)
        for season in data["content"]:
            season_year = int(season["label"][:4])
            if self.from_year <= season_year <= self.to_year:
                self.season_ids_dict[season["label"]] = str(int(season["id"]))

    def closed(self, reason):
        with open(self.output_file, "w") as fp:
            json.dump(self.season_ids_dict, fp, indent=4)


def get_season_ids():
    settings = get_project_settings()
    season_ids_file = Path(settings.get("SEASON_IDS_JSON"))
    if not season_ids_file.exists(): # broken
        process = CrawlerProcess(settings)
        process.crawl(SeasonIDSpider)
        process.start()
    with open(season_ids_file, "r") as f:
        return json.loads(f.read())
