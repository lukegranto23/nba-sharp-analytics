#!/usr/bin/env python3
"""
Fetch NBA data from free public sources
"""
import requests
import json
from datetime import datetime
import os

def fetch_todays_games():
    """Fetch today's NBA schedule from balldontlie API (free)"""
    url = "https://api.balldontlie.io/v1/games"
    today = datetime.now().strftime("%Y-%m-%d")
    
    params = {"dates": [today]}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json().get('data', [])
    return []

def fetch_team_stats():
    """Fetch current team statistics"""
    # Using balldontlie for team stats
    url = "https://api.balldontlie.io/v1/season_averages"
    response = requests.get(url, params={"season": 2025})
    
    if response.status_code == 200:
        return response.json().get('data', [])
    return []

def fetch_injuries():
    """Scrape injury data from ESPN"""
    # ESPN provides public injury data
    url = "https://www.espn.com/nba/injuries"
    # Simple scraping or use RSS feed
    return {}

def save_data():
    """Save all data to JSON files"""
    os.makedirs('data', exist_ok=True)
    
    games = fetch_todays_games()
    stats = fetch_team_stats()
    injuries = fetch_injuries()
    
    with open('data/todays_games.json', 'w') as f:
        json.dump(games, f, indent=2)
    
    with open('data/team_stats.json', 'w') as f:
        json.dump(stats, f, indent=2)
    
    with open('data/injuries.json', 'w') as f:
        json.dump(injuries, f, indent=2)
    
    print(f"✅ Fetched {len(games)} games for {datetime.now().date()}")

if __name__ == "__main__":
    save_data()
