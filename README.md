# Weather Data Fetcher

A Python application that collects real-time weather data, stores it in **InfluxDB 2**, and visualizes it in **Grafana** dashboards.

## Features

* Fetches weather data (temperature, humidity, pressure, wind speed, etc.) for a specified city using the **OpenWeatherMap API**.
* Stores collected data in **InfluxDB 2**, a time-series database.
* Visualizes data in **Grafana** dashboards for real-time monitoring.
* Configurable via environment variables (`.env` file).

## Architecture

```
OpenWeatherMap API → Python script → InfluxDB 2 → Grafana dashboard
```

## Prerequisites

* Python 3.11+
* InfluxDB 2.x (local or server instance)
* Grafana (optional but recommended)
* OpenWeatherMap API key

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/adamusking/weather-data-fetcher.git
cd weather-data-fetcher
```

### 2. Create and activate a Python virtual environment

```bash
python3 -m venv weather-env
source weather-env/bin/activate  # On Windows: weather-env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a `.env` file in the root directory and add your credentials:

```dotenv
# InfluxDB
INFLUX_TOKEN=your_influxdb_token
INFLUX_ORG=your_organization
INFLUX_URL=http://localhost:8086
INFLUX_BUCKET=your_bucket_name

# OpenWeatherMap
WEATHER_API_KEY=your_openweathermap_api_key
CITY=your_city_name
```

## Usage

Run the Python script:

```bash
python main.py
```

The script will fetch weather data every minute and write it to InfluxDB.

## Grafana Dashboard Setup (Optional)

1. Open Grafana in your browser.
2. Add InfluxDB as a data source:

   * URL: `http://localhost:8086`
   * Token: Use `INFLUX_TOKEN` from `.env`
   * Organization: `INFLUX_ORG`
3. Create a new dashboard and add panels for metrics:

   * `temperature`
   * `humidity`
   * `pressure`
   * `wind_speed`

## License

MIT License. See [LICENSE](LICENSE) for details.
