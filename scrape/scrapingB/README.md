# EPL matches spider

A simple spider to scrape EPL matches from [the official website](https://www.premierleague.com/results), using Scrapy.
Python 3.12 and above recommended.

## Project folder structure

```
.
├── epl_scrape/
│   ├── epl_scrape/
│   │   ├── spiders/
│   │   │   ├── __init__.py
│   │   │   ├── match_spider.py
│   │   │   └── season_id_spider.py
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   └── settings.py
│   └── scrapy.cfg
└── requirements.txt
```

## Settings

Modify `settings.py` file directly.

```python
FROM_SEASON = "2019/20"
TO_SEASON = "2023/24"
SEASON_IDS_JSON = "season_ids.json"  # season IDs filename
MATCHES_CSV = "matches.csv"  # output filename
```

## How to run

Make sure to have Python added to PATH.

First-time setup might be slow due to venv creation and package installation.
Feel free to modify script files to your liking.

### Windows

Either double-click `get_matches.cmd`, or open Powershell Terminal in the main folder and run:

```powershell
.\get_matches.ps1
```

### Linux/MacOS

Open Terminal in the main folder and run line by line:

```bash
chmod +x get_matches.sh
./get_matches.sh
```