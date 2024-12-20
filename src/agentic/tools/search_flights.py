from taskflowai import AmadeusTools
from src.agentic.logger import logging
from src.agentic.exception import CustomException
import sys

class SearchFlights:
    @classmethod
    def search_flights_tool(cls):
        try:
            logging.info("Initiating flight search using AmadeusTools.")
            search_flights = AmadeusTools.search_flights
            logging.info("Flight search initiated successfully.")
            return search_flights
        except Exception as e:
            logging.info("Failed to initiate flight search.")
            raise CustomException(sys, e)
