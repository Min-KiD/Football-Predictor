#!/bin/bash

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt

# Move into the project directory
cd epl_scrape

# Run the Scrapy spiders
scrapy crawl season_ids
scrapy crawl matches