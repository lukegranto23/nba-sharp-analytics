#!/usr/bin/env python3
"""
Fetch NBA data from balldontlie API with authentication
"""
import requests
import json
from datetime import datetime
import os

# Your balldontlie API key
API_KEY = "0c1880ce-0aac-44ac-9e36-0e7aa6ca29c6"
HEADERS = {"Authorization": API_KEY}

def fetch_todays_games():
    """Fetch today's NBA schedule"""
    url = "https://api.balldontlie.io/v1/games"
    today = datetime.now().strftime("%Y-%m-%d")
    
    try:
        params = {"dates[]": today}
        response = requests.get(url, params=params, headers=HEADERS, timeout=10)
        
        if response.status_code == 200:
            games = response.json().get('data', [])
            print(f"✅ Fetched {len(games)} games for {today}")
            return games
        else:
            print(f"⚠️ API Error {response.status_code}: {response.text}")
            return []
    except Exception as e:
        print(f"❌ Error fetching games: {e}")
        return []

def fetch_team_stats():
    """Fetch current season team statistics"""
    url = "https://api.balldontlie.io/v1/stats"
    
    try:
        # Get recent stats for all teams
        params = {
            "seasons[]": 2024,  # Current season
            "per_page": 100
        }
        response = requests.get(url, params=params, headers=HEADERS, timeout=10)
        
        if response.status_code == 200:
            stats = response.json().get('data', [])
            print(f"✅ Fetched {len(stats)} team stats")
            return stats
        else:
            print(f"⚠️ API Error {response.status_code}: {response.text}")
            return []
    except Exception as e:
        print(f"❌ Error fetching stats: {e}")
        return []

def fetch_injuries():
    """Placeholder for injury data - can be expanded later"""
    return {}

def save_data():
    """Save all data to JSON files"""
    os.makedirs('data', exist_ok=True)
    
    games = fetch_todays_games()
    stats = fetch_team_stats()
    injuries = fetch_injuries()
    
    # Save games
    with open('data/todays_games.json', 'w') as f:
        json.dump(games, f, indent=2)
    
    # Save stats
    with open('data/team_stats.json', 'w') as f:
        json.dump(stats, f, indent=2)
    
    # Save injuries
    with open('data/injuries.json', 'w') as f:
        json.dump(injuries, f, indent=2)
    
    print(f"\n📊 Data saved to data/ folder")
    print(f"   - {len(games)} games")
    print(f"   - {len(stats)} stat entries")

if __name__ == "__main__":
    save_data()

