#!/bin/bash

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Move into the project directory
cd epl_scrape_main

# Install the required packages
pip install -r requirements.txt

# Run the Scrapy spiders
scrapy crawl matches -a from_season=2019/20 -a to_season=2023/24