"""Weather Tracker — reads and summarizes local weather station data."""

import csv
import json
import os
from statistics import mean


def load_config():
    """Load configuration from config.json."""
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        return json.load(f)


def read_readings(filepath):
    """Read weather readings from a CSV file."""
    readings = []
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["temperature_c"] = float(row["temperature_c"])
            row["humidity_pct"] = float(row["humidity_pct"])
            row["wind_speed_kmh"] = float(row["wind_speed_kmh"])
            row["pressure_hpa"] = float(row["pressure_hpa"])
            readings.append(row)
    return readings


def summarize(readings):
    """Produce a summary dict for a list of readings."""
    temps = [r["temperature_c"] for r in readings]
    humidities = [r["humidity_pct"] for r in readings]
    winds = [r["wind_speed_kmh"] for r in readings]
    return {
        "total_readings": len(readings),
        "avg_temp_c": round(mean(temps), 1),
        "min_temp_c": min(temps),
        "max_temp_c": max(temps),
        "avg_humidity_pct": round(mean(humidities), 1),
        "avg_wind_kmh": round(mean(winds), 1),
    }


if __name__ == "__main__":
    config = load_config()
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    readings = read_readings(os.path.join(data_dir, "sample-readings.csv"))
    summary = summarize(readings)
    print(f"Weather Tracker v{config['version']}")
    print(f"Station data loaded: {summary['total_readings']} readings")
    print(f"Temperature range: {summary['min_temp_c']}°C to {summary['max_temp_c']}°C")
    print(f"Average temperature: {summary['avg_temp_c']}°C")
    print(f"Average humidity: {summary['avg_humidity_pct']}%")
    print(f"Average wind speed: {summary['avg_wind_kmh']} km/h")
