# SQLAlchemy engine + session setup
# SQLite connection
# Table creation (Base.metadata.create_all())

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, WeatherSummaryORM

DATABASE_URL = "sqlite:///weather.sqlite3"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    # Create database tables based on ORM models
    Base.metadata.create_all(bind=engine)

def insert_weather_summary(summary):
    # Insert a WeatherSummaryORM record into the database.
    session = SessionLocal()

    db_record = WeatherSummaryORM(
        latitude=summary.latitude,
        longitude=summary.longitude,
        month=summary.month,
        day=summary.day,
        year=summary.year,
        avg_temp_5yr=summary.avg_temp_5yr,
        min_temp_5yr=summary.min_temp_5yr,
        max_temp_5yr=summary.max_temp_5yr,
        avg_wind_5yr=summary.avg_wind_5yr,
        min_wind_5yr=summary.min_wind_5yr,
        max_wind_5yr=summary.max_wind_5yr,
        sum_precip_5yr=summary.sum_precip_5yr,
        min_precip_5yr=summary.min_precip_5yr,
        max_precip_5yr=summary.max_precip_5yr,
    )

    session.add(db_record)
    session.commit()
    session.close()


def get_weather_summary():
    # Retrieving weather summary record from db
    session = SessionLocal()
    record = (
        session.query(WeatherSummaryORM)
        .order_by(WeatherSummaryORM.id.desc())
        .first()
    )
    session.close()
    return record