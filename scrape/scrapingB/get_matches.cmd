@echo off
REM Create a virtual environment
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate

REM Move in the project directory
cd epl_scrape_main

REM Install the required packages
pip install -r requirements.txt

REM Run the Scrapy spiders
scrapy crawl matches -a from_season=2019/20 -a to_season=2023/24