from taskflowai import WebTools
from src.agentic.logger import logging
from src.agentic.exception import CustomException
import sys

class GetWeatherData:
    @classmethod
    def fetch_weather_data(cls):
        try:
            logging.info("Fetching weather data using WebTools.")
            weather_data = WebTools.get_weather_data
            logging.info("Weather data fetched successfully.")
            return weather_data
        except Exception as e:
            logging.info("Failed to fetch weather data.")
            raise CustomException(sys, e)
