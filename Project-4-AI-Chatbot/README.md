# Project 4 - Weather Dashboard

A Python-based weather dashboard application that fetches real-time weather data from the OpenWeatherMap API.

## Features

✨ **Real-Time Weather Data**
- Current temperature and "feels like" temperature
- Humidity and atmospheric pressure
- Weather conditions description
- Wind speed information

🌍 **Multiple Cities**
- Search weather for any city in the world
- Pre-loaded dataset with major world cities

📊 **Interactive Dashboard**
- User-friendly CLI interface
- Formatted weather display with emojis
- Continuous operation with quit option

## Requirements

```bash
pip install requests
```

## Setup

1. **Get API Key:**
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Get your API key from the dashboard

2. **Configure API Key:**
   - Open `app.py`
   - Replace `your_api_key_here` with your actual API key:
   ```python
   API_KEY = "your_actual_api_key"
   ```

## How to Run

```bash
python app.py
```

## Usage Example

```
🌤️  Weather Dashboard Application
--------------------------------------------------

Enter city name (or 'quit' to exit): London

Fetching weather data for London...

==================================================
🌍 Weather Dashboard - London, GB
==================================================
📅 Time: 2024-12-15 14:30:45
🌡️  Temperature: 8°C (feels like 6°C)
💧 Humidity: 75%
🔽 Pressure: 1013 hPa
☁️  Conditions: Cloudy
💨 Wind Speed: 3.5 m/s
==================================================
```

## API Endpoints

- **Current Weather:** `https://api.openweathermap.org/data/2.5/weather`
- **Forecast:** `https://api.openweathermap.org/data/2.5/forecast`

## Dataset

The `dataset.csv` file contains coordinates for 10 major world cities for quick reference.

| City | Latitude | Longitude | Elevation |
|------|----------|-----------|-----------|
| New York | 40.7128 | -74.0060 | 10m |
| London | 51.5074 | -0.1278 | 11m |
| Tokyo | 35.6762 | 139.6503 | 0m |
| Paris | 48.8566 | 2.3522 | 35m |
| Sydney | -33.8688 | 151.2093 | 58m |
| Dubai | 25.2048 | 55.2708 | 5m |
| Toronto | 43.6532 | -79.3832 | 76m |
| Berlin | 52.5200 | 13.4050 | 34m |
| Singapore | 1.3521 | 103.8198 | 15m |
| Mumbai | 19.0760 | 72.8777 | 14m |

## Future Enhancements

- 📈 5-day forecast display
- 💾 Weather history tracking
- 🎨 GUI using Tkinter or Flask
- 📱 Mobile app version
- 🗺️ Weather map visualization
- 🔔 Weather alerts

## Error Handling

The application includes error handling for:
- Invalid city names
- Network connection failures
- API rate limiting
- Invalid API keys

## License

MIT License

## Author

Your Name - [GitHub](https://github.com/bhavishyanarne)
