# EPL matches spider

A simple spider to scrape EPL matches from [the official website](https://www.premierleague.com/results), using Scrapy.
Python 3.12 and above recommended.

## Project folder structure

```
.
└── epl_scrape_main/
    ├── epl_scrape/
    │   ├── spiders/
    │   │   ├── __init__.py
    │   │   └── match_spider.py
    │   ├── __init__.py
    │   ├── items.py
    │   ├── middlewares.py
    │   ├── pipelines.py
    │   └── settings.py
    ├── requirements.txt
    ├── scrapinghub.yml
    └── scrapy.cfg
```

## How to run offline

Make sure to have Python added to PATH.

First-time setup might be slow due to venv creation and package installation.
Feel free to modify script files to your liking.

> [!TIP]
> All script files for getting matches end with the line
> ```cmd
> scrapy crawl matches -a from_season=2019/20 -a to_season=2023/24
> ```
> You can change the range of seasons to scrape by changing the command arguments (after the `-a` flag).

### Windows

Either double-click `get_matches.cmd`, or open Powershell Terminal in the main
folder (where lie these scripts) and run:

```powershell
.\get_matches.ps1
```

### Linux/MacOS

Open Terminal in the main folder and run line by line:

```bash
chmod +x get_matches.sh
./get_matches.sh
```

## How to deploy to Cloud and run periodically

Follow these guides, which have much more detailed instructions than I could ever provide:

- Create, deploy, and run a Zyte Scrapy Cloud project. [Official guide](https://docs.zyte.com/web-scraping/tutorials/main/cloud.html)
- Schedule a periodic crawl job (optional).
- Export CSV data to a Google Sheet (optional). [Official guide](https://docs.zyte.com/web-scraping/guides/export/file-storage/google-sheets.html)

Under ideal conditions, you should have a spider that scrapes EPL matches data periodically
and updates them into a Google Sheet.