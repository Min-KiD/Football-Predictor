@echo off
REM Create a virtual environment
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate

REM Install the required packages
pip install -r requirements.txt

REM Move in the project directory
cd epl_scrape

REM Run the Scrapy spiders
scrapy crawl season_ids
scrapy crawl matches