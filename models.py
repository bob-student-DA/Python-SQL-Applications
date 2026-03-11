# C3 - WeatherSummary instance
# Calls API methods
#computes 5-year stats
#assigns values to the C1 object
# C5 insert data into the DB
#C6 queries DB and prints formatted output


from datetime import date
from weather_client import get_daily_weather

latitude = 36.1699
longitude = -115.1398
month = 5
day = 18

current_year = date.today().year
start_year = current_year - 4  # last 5 years total

temps = []
winds = []
precips = []

for year in range(start_year, current_year + 1):
    date_str = f"{year}-{month:02d}-{day:02d}"

    temp, wind, precip = get_daily_weather(
        latitude=latitude,
        longitude=longitude,
        date_str=date_str
    )

    temps.append(temp)
    winds.append(wind)
    precips.append(precip)


# Temperature stats (1 decimal place)
avg_temp_5yr = round(sum(temps) / len(temps), 1)
min_temp_5yr = round(min(temps), 1)
max_temp_5yr = round(max(temps), 1)

# Wind speed stats (1 decimal place)
avg_wind_5yr = round(sum(winds) / len(winds), 1)
min_wind_5yr = round(min(winds), 1)
max_wind_5yr = round(max(winds), 1)

# Precipitation stats (2 decimal places)
sum_precip_5yr = round(sum(precips), 2)
min_precip_5yr = round(min(precips), 2)
max_precip_5yr = round(max(precips), 2)


from models import WeatherSummary
from db import init_db, insert_weather_summary


# Create WeatherSummary object
summary = WeatherSummary(
    latitude=latitude,
    longitude=longitude,
    month=month,
    day=day,
    year=current_year
)

summary.avg_temp_5yr = avg_temp_5yr
summary.min_temp_5yr = min_temp_5yr
summary.max_temp_5yr = max_temp_5yr

summary.avg_wind_5yr = avg_wind_5yr
summary.min_wind_5yr = min_wind_5yr
summary.max_wind_5yr = max_wind_5yr

summary.sum_precip_5yr = sum_precip_5yr
summary.min_precip_5yr = min_precip_5yr
summary.max_precip_5yr = max_precip_5yr


# Making db and inserting record
init_db()
insert_weather_summary(summary)

from db import get_weather_summary

record = get_weather_summary()

print("\nWeather Summary (5-Year Aggregates)")
print("----------------------------------")
print(f"Location: ({record.latitude}, {record.longitude})")
print(f"Date: {record.month}/{record.day}")
print(f"Reference Year: {record.year}\n")

print(f"Avg Temp (5yr): {record.avg_temp_5yr} °F")
print(f"Min Temp (5yr): {record.min_temp_5yr} °F")
print(f"Max Temp (5yr): {record.max_temp_5yr} °F\n")

print(f"Avg Wind (5yr): {record.avg_wind_5yr} mph")
print(f"Min Wind (5yr): {record.min_wind_5yr} mph")
print(f"Max Wind (5yr): {record.max_wind_5yr} mph\n")

print(f"Total Precip (5yr): {record.sum_precip_5yr} in")
print(f"Min Precip (5yr): {record.min_precip_5yr} in")
print(f"Max Precip (5yr): {record.max_precip_5yr} in")
