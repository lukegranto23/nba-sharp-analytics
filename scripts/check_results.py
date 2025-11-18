#!/usr/bin/env python3
"""
Check game results and update prediction records
"""
import json
import requests
from datetime import datetime, timedelta

def fetch_yesterdays_results():
    """Fetch results from yesterday's games"""
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    url = "https://api.balldontlie.io/v1/games"
    
    response = requests.get(url, params={"dates": [yesterday]})
    if response.status_code == 200:
        return response.json().get('data', [])
    return []

def check_predictions():
    """Compare predictions against actual results"""
    try:
        with open('data/predictions_history.json', 'r') as f:
            predictions = json.load(f)
    except FileNotFoundError:
        predictions = []
    
    results = fetch_yesterdays_results()
    
    for result in results:
        # Find matching prediction
        game_id = result.get('id')
        
        for pred in predictions:
            if pred.get('game_id') == game_id and not pred.get('result_checked'):
                # Check if prediction was correct
                home_score = result.get('home_team_score', 0)
                away_score = result.get('visitor_team_score', 0)
                
                actual_winner = "Home" if home_score > away_score else "Away"
                predicted_winner = pred.get('prediction')
                
                pred['actual_winner'] = actual_winner
                pred['was_correct'] = (actual_winner == predicted_winner)
                pred['result_checked'] = True
                pred['home_score'] = home_score
                pred['away_score'] = away_score
    
    # Save updated predictions
    with open('data/predictions_history.json', 'w') as f:
        json.dump(predictions, f, indent=2)
    
    print("✅ Results checked and updated")

if __name__ == "__main__":
    check_predictions()
