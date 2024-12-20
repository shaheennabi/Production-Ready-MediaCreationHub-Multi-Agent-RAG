import os
from taskflowai import WebTools
from src.agentic.logger import logging
from src.agentic.exception import CustomException

# Validate required API keys
required_keys = [
    "WEATHER_API_KEY",
]

try:
    # Check for missing keys
    missing_keys = [key for key in required_keys if not os.getenv(key)]
    if missing_keys:
        raise CustomException(f"Missing required API keys: {', '.join(missing_keys)}")
    logging.info("All required API keys are present.")
except CustomException as e:
    logging.error(f"API key validation failed: {e}")
    raise


class WeatherTool:
    @classmethod
    def get_weather(cls):
        """
        This tool will ping the weather API and return the response back to the LLM.
        """
        try:
            logging.info("Fetching weather data using WebTools.")
            weather_data = WebTools.get_weather_data()
            logging.info("Successfully fetched weather data.")
            return weather_data
        except Exception as e:
            logging.error(f"Failed to fetch weather data: {e}")
            raise CustomException(f"An error occurred while fetching weather data: {e}")
