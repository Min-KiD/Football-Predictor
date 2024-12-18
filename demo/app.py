import sys
sys.dont_write_bytecode = True

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import sklearn
import xgboost
from datetime import datetime
import pandas as pd
from utils import *
import time
import random

app = Flask(__name__)
CORS(app)

# Load the model
with open('models/calibrated_model.pkl', 'rb') as f:
    model = joblib.load(f)

test_mode = True
cache = {}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    team1 = data['team1']
    team2 = data['team2']
    match_key = f"{team1}_vs_{team2}"

    if test_mode:
        delay = random.uniform(15, 20)
        time.sleep(delay)
        if match_key in cache:
            return jsonify(cache[match_key])
        win, draw, lose = generate_random_probabilities()
        result = {
            'win': win,
            'draw': draw,
            'lose': lose,
            'team1': team1,
            'team2': team2
        }
        cache[match_key] = result
        return jsonify(result)

    today = datetime.today()
    formatted_date = today.strftime('%d-%m-%y')
    link = get_latest_match(team1, team2, formatted_date)
    if link:
        df = get_data_half(link)
        row = df.iloc[[45]]

        prediction = model.predict_proba(row)
        prediction = [0.51, 0.22, 0.66]
        print(prediction)

        response = jsonify({
            'win': round(prediction[0, 0], 4),
            'draw': round(prediction[0, 1], 4),
            'lose': round(prediction[0, 2], 4),
            'team1': team1,
            'team2': team2
        })
        return response
    else:
        return jsonify({
            'error': 'No match found'
        })

@app.route('/lookup', methods=['POST'])
def lookup():
    data = request.json
    team1 = data['team1']
    team2 = data['team2']
    response = get_teams_stats_multithread(team1, team2)
    response = jsonify(response)
    return response


if __name__ == '__main__':
    app.run(debug=True, port=8386)