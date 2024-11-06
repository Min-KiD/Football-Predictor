# Create a virtual environment
python -m venv venv

# Activate the virtual environment
& .\venv\Scripts\Activate.ps1

# Install the required packages
pip install -r requirements.txt

# Move into the project directory
Set-Location -Path epl_scrape

# Run the Scrapy spiders
scrapy crawl season_ids
scrapy crawl matches