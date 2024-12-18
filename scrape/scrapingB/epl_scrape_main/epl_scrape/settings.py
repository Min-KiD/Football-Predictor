# Scrapy settings for epl_scrape project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "epl_scrape"

SPIDER_MODULES = ["epl_scrape.spiders"]
NEWSPIDER_MODULE = "epl_scrape.spiders"

# Common spider constants
MATCHES_CSV = "matches.csv"

# Logging level and location
# LOG_FILE = "scrapy_log.txt"
# LOG_LEVEL = "DEBUG"
# LOG_FORMAT = "%(levelname)s: %(message)s"
# LOG_STDOUT = True

# Exporter settings
FEED_STORAGES = {
    "gsheets": "scrapy_google_sheets_exporter.gsheets_exporter.GoogleSheetsFeedStorage",
}
FEEDS = {
    "gsheets://docs.google.com/spreadsheets/d/1_FbBbss_NAuaqIWKs7kwhDBEtzD7LS1zhAEDikQsBXw/edit#gid=0": {
        "format": "csv",
        "overwrite": True,
    }
}
GOOGLE_CREDENTIALS = {
    "type": "service_account",
    "project_id": "secure-proxy-324607",
    "private_key_id": "610ae542cb84251024259d47340505b4a68fc97f",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDQUKtO4W96tsbz\nRJ3QCkLtsvGzRqUvSLV8/+UVGbX6limbQ2zxl4rwVo6WJNKeqthjiPvib+/Hwv5r\nYq3s1Q3FCdwpESI93HxP6RKRFsvY5P2rCUJECXiT1Fsrbm8JA9ZjW8rzc0EDhhQV\nCzjStXDyWIhiudFjrcAcdw7qU/20bmlhfuW/ehu2M96WHaCfzj1vI5npuQ09om+w\nnDt9JtuE14JM0ewl2qENloA9ZQ1nOsIFAoF69CCRV9gZySUobLmLcOuevyo6zYbv\nLmEznT5JaLOJTs4DTqbclIWdiNSuoOMAJRpiwliJzC0pESoO+JNgess7D7W25mH8\nLD2WC4glAgMBAAECggEAIVNufIGTOJIKFPv6tUAXAfj5MuGP5pcetb8ocm45Dzw7\nrsOkJ6hDSXzHddyxN0IEuTO+fDTFKvOWiS5xvaw99jJEHuvHSxc9aflTB5Qai3ni\n3Rxvlfvf5uJ3rWSO7eXHxAB44Oak1X/7MXyonAj750FjnEu25Ff1HnirkbBbK6Se\nOHwiVZB6G1rlPlzcbge3usOWnP1Hrkp38INhAbGry8BTwjOFOchKR8Q52QU9+Fhj\nKkMrx7B1bhiD0fSYAFlxwF3StFeG9x2+i9cYgHZxMVPd9RsYuZffxeGzxTHWHHGe\nGRBGPn3Lxlcf3CdafC2jmV/gmIaxzy71Cb41+GJvhwKBgQD25Fvc4I0vTLa0e8ii\neFNXo4NiQWAMaU4pGj8jtfSSVH80QzeAH/8POmARg9eH6ntG/R/9r34kAbOYARbR\nrOC0P0kZwaSfHSljJ4atyeu1YNWdXrjMcbMMcE6aNwLvjs8wgWd67cRUo4O6mhMe\n39as3hnFIKOG+Ij4akCtQbhtJwKBgQDX//23unBbIpHX31BF7j43Dj1nopZ+SD7I\nfHlOZaus3GV0AVfsjwtQxtuDVsWL5QY0REWllD+Lw/TUGc9GBJzzkCrSQzW8iEPc\nDYuWqRG1pWPFjeaZOvYxi7LKjMgnwF4U7YL0Gq9ckQiUd4v9Dt/h3qbCbxG4vT9W\nYrQuSvaH0wKBgDXZPMgCGgkU/EyFKw90mwjkWwWVKLPMTAXe+aJ6TyuTTmNBvdsu\nH11c6BMp5Fp6pASptM6J9kM4M8mVgzqcMC5gFzuM5rDllV9RAajp/4UB59V5EWlV\n6y1tWVd9ZCCHz1zO/JjtPwMO3u5WKJF1VMdDce9y3PfVQVqdIhon2WfFAoGBAKNr\nAtrxTDY3Jl5LjuEJibp/pId25CMwp4dpXSGqHEORD5S/u3S3GJmJieSJTrYzlQkQ\nKh1G1vj4TY/24vGXZeOETFF+FfbIpYakHNrkmQhz09NQM4n0qPT9O0yxTHF+we9V\nbsEeO1RuSi6Bb8EKcunhWQs7mw3I6FWEIcvwXSqPAoGALytZQF8ycIL2KekksqXK\nAD13LAdIsABmBcUV6OHSSTkX0Gre6g5n4Pj9RGi0UdnB4IDJ7p8nGqFUoT9mMQjJ\nYeX3ibV4pdxppcOuGHnMAi672+zGuWIWtqmtcZUPDLc23LSqYSQKTB6fs3BB/atS\neXN6Mjgx8qnnY4zsFBoaGPY=\n-----END PRIVATE KEY-----\n",
    "client_email": "scrapy-cloud@secure-proxy-324607.iam.gserviceaccount.com",
    "client_id": "108735211432594675718",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/scrapy-cloud%40secure-proxy-324607.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com",
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "epl_scrape (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "*/*",
    "Origin": "https://www.premierleague.com",
    "Referer": "https://www.premierleague.com/",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "epl_scrape.middlewares.EplScrapeSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "epl_scrape.middlewares.EplScrapeDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "epl_scrape.pipelines.MatchPipeline": 300,
    "epl_scrape.pipelines.PlayerPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
