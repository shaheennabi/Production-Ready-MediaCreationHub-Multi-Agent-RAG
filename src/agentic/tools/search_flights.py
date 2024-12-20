import os
from taskflowai import AmadeusTools
from src.agentic.logger import logging
from src.agentic.exception import CustomException

# Validate required API keys
required_keys = [
    "AMADEUS_API_KEY",
    "AMADEUS_API_SECRET",
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


class SearchFlights:
    @classmethod
    def get_flights(cls):
        """
        This method sends an API request to the Amadeus Flights Search API
        and returns the flight report to the LLM.
        """
        try:
            logging.info("Fetching flight data using AmadeusTools.")
            flight_data = AmadeusTools.search_flights()
            logging.info("Successfully fetched flight data.")
            return flight_data
        except Exception as e:
            logging.error(f"Failed to fetch flight data: {e}")
            raise CustomException(f"An error occurred while fetching flight data: {e}")
