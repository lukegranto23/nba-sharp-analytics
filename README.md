# 🏀 NBA Sharp Analytics Platform

**Professional NBA betting analytics with fully automated daily updates**

## Features

✅ **Fully Automated** - Zero maintenance required
✅ **Daily Updates** - Fresh predictions every morning at 9am ET
✅ **Performance Tracking** - Real win/loss record (no fake stats)
✅ **6 Prediction Models** - Sully Four Factors, ELO, Net Rating, Pythagorean, Ensemble
✅ **+EV Calculator** - Expected value for every bet
✅ **Multi-Book Line Shopping** - Compare 5+ sportsbooks
✅ **Sharp Money Indicators** - RLM, Steam Moves, CLV tracking
✅ **100% Free** - No subscriptions, no paid APIs

## How It Works

### Automated Daily Flow:

**9:00 AM ET** - GitHub Actions runs:
1. Fetches today's NBA schedule
2. Gets injury reports from ESPN
3. Pulls betting lines from multiple books
4. Calculates predictions using 6 models
5. Stores data in `data/` folder

**2:00 AM ET** (after games finish):
1. Fetches final scores
2. Checks predictions vs actual results
3. Updates win/loss record
4. Calculates accuracy stats

**When You Visit**: Fresh data from latest automated run!

## Quick Start

1. Visit: `https://lukegranto23.github.io/nba-sharp-analytics/`
2. See today's predictions automatically
3. Check back tomorrow for new games

## Tech Stack

- **Frontend**: HTML/CSS/JavaScript
- **Backend**: Python + GitHub Actions (cron jobs)
- **Database**: JSON files in `data/` folder
- **Hosting**: GitHub Pages (free)
- **APIs**: balldontlie.io (free NBA data)

## File Structure

```
.
├── index.html              # Main app
├── data/
│   ├── todays_games.json   # Updated daily at 9am
│   ├── predictions.json    # Today's predictions
│   ├── predictions_history.json  # All past predictions
│   ├── performance.json    # Win/loss stats
│   ├── team_stats.json     # Current season stats
│   └── injuries.json       # Latest injury reports
├── scripts/
│   ├── fetch_nba_data.py
│   ├── generate_predictions.py
│   ├── check_results.py
│   └── update_performance.py
└── .github/workflows/
    ├── daily-update.yml
    └── check-results.yml
```

## Performance Tracking

Check `data/performance.json` for live stats:
- Overall accuracy %
- Win/loss record
- By confidence level
- By model type

## Contributing

This is a personal project, but feel free to fork and customize!

## License

MIT
