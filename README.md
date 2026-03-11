# C1: WeatherSummary data model for 5-year weather aggregation
# C4: weathersummaryORM - C4 (SQLAlchemy ORM table)

from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class WeatherSummary:
    def __init__(
        self,
        latitude,
        longitude,
        month,
        day,
        year
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year

        #Five-year temperature stats
        self.avg_temp_5yr = None
        self.min_temp_5yr = None
        self.max_temp_5yr = None

        #Five-year wind speed stats
        self.avg_wind_5yr = None
        self.min_wind_5yr = None
        self.max_wind_5yr = None

        #Five-year precipitation stats
        self.sum_precip_5yr = None
        self.min_precip_5yr = None
        self.max_precip_5yr = None


class WeatherSummaryORM(Base):
    __tablename__ = "weather_summary"

    id = Column(Integer, primary_key=True)

    latitude = Column(Float)
    longitude = Column(Float)
    month = Column(Integer)
    day = Column(Integer)
    year = Column(Integer)

    avg_temp_5yr = Column(Float)
    min_temp_5yr = Column(Float)
    max_temp_5yr = Column(Float)

    avg_wind_5yr = Column(Float)
    min_wind_5yr = Column(Float)
    max_wind_5yr = Column(Float)

    sum_precip_5yr =Column(Float)
    min_precip_5yr = Column(Float)
    max_precip_5yr = Column(Float)
