# Demo  Web Extension for Football Prediction

A Manifest V3 web extension providing football prediction for a recognized
match on browser tab. Built with Bootstrap 5 and Chart.js for the beautiful UI,
Flask for background data update and prediction.

## Setup

Suppose you have cloned the repository.

### Web Extension

Open your favorite Chromium-based browser and follow
[this guide](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world#load-unpacked)
to load the extension. The extension folder is this entire folder housing this `README.md` and `manifest.json`.

### Flask Server

Open a terminal/command prompt in this folder.

Activate the virtual environment (optional) and install the dependencies.

```bash
pip install -r requirements.txt
```

Then run the Flask server. The port is set to 8386 (very lucky number).

```bash
python app.py
```

## Usage

The extension will read the current tab title and recognize if a football match is mentioned. If so, it will
send requests to the Flask server to get the prediction and teams' recent stats.

Prediction is generated using ML models in `models/` folder. Both the models input and recent stats are scraped
from [WhoScored](https://whoscored.com) (blocks IP from Vietnam). So you might have to turn on VPN or use a proxy
for this function.