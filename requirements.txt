# Weather Event Planning Application

## Overview
This application uses Python to retrieve historical weather data for a specified location and date,
calculates five-year weather aggregates, and stores the results in a local SQLite database.
The application is designed for the use of event planning decisions by providing expected weather
conditions for a given time of year.

The application uses the Open-Meteo Historical Weather API, SQLAlchemy ORM in conjunction with SQLite for local
data storage.

## Features
- Retrieves daily historical weather data for the most recent five years
- Calculates five-year averages, minimums, maximums, and precipitation totals
- Stores aggregated weather data in a SQLite database
- Queries and displays stored weather summary data in a formatted output

## Programs Used
- Python 3
- Requests
- SQLAlchemy
- SQLite
- Open-Meteo Historical Weather API
- Standard Python modules (such as datetime and sqlite3) are included with Python 3.13 and are covered by the Python version listed in requirements.txt.



## How to Run the Program
1. Clone the repository.
2. Create and activate a Python virtual environment (if necessary).
3. Install required dependencies:
   pip install -r requirements.txt
