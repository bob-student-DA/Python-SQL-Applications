# D: unit tests - stat calculations, db insert/query

import unittest
from datetime import date

from models import WeatherSummary
from weather_client import get_daily_weather
from db import init_db, insert_weather_summary, get_weather_summary

class TestWeatherApplication(unittest.TestCase):

# Test 1 Statistics calc - avg / min / max logic

    def test_statistics_calculation(self):
        temps = [70.0, 75.0, 80.0, 85.0, 90.0]

        avg_temp = round(sum(temps) / len(temps), 1)
        min_temp = min(temps)
        max_temp = max(temps)

        self.assertEqual(avg_temp, 80.0)
        self.assertEqual(min_temp, 70.0)
        self.assertEqual(max_temp, 90.0)

# Test 2 Database insert and query - a weatherSummary record can be stored
# and retrieved

    def test_database_insert_and_query(self):
        init_db()

        summary = WeatherSummary(
            latitude=36.1699,
            longitude=-115.1398,
            month=5,
            day=18,
            year=date.today().year
        )

        summary.avg_temp_5yr = 80.0
        summary.min_temp_5yr = 70.0
        summary.max_temp_5yr = 90.0

        summary.avg_wind_5yr = 10.0
        summary.min_wind_5yr = 5.0
        summary.max_wind_5yr = 15.0

        summary.sum_precip_5yr = 1.2
        summary.min_precip_5yr = 0.0
        summary.max_precip_5yr = 0.5

        insert_weather_summary(summary)
        record = get_weather_summary()

        self.assertIsNotNone(record)
        self.assertEqual(record.latitude, summary.latitude)
        self.assertEqual(record.avg_temp_5yr, summary.avg_temp_5yr)

# Test 3 API method returns a list

    def test_api_response_shape(self):
        temp, wind, precip = get_daily_weather(
            latitude=36.1699,
            longitude=-115.1398,
            date_str="2023-05-18"
        )

        self.assertIsInstance(temp, float)
        self.assertIsInstance(wind, float)
        self.assertIsInstance(precip, float)


if __name__ == "__main__":
    unittest.main()