from taskflowai import Task
from src.agentic.agents.travel_agent import TravelAgent
from src.agentic.logger import logging
from src.agentic.exception import CustomException


class SearchFlightsTask:
    @classmethod
    def initialize_search_flights_task(cls, current_location, destination, dates):
        """Search flight options"""
        try:
            logging.info(f"Initializing search flights task from {current_location} to {destination} on {dates}.")
            
            report = Task.create(
                agent=TravelAgent.initialize_travel_agent(),
                context=f"Flights from {current_location} to {destination} on {dates}",
                instruction="Find top 3 affordable and convenient flight options and provide concise bullet-point information"
            )

            logging.info("Search flights task initialized successfully.")
            return report

        except CustomException as e:
            logging.error(f"Custom exception occurred while initializing search flights task: {e}")
            raise CustomException(f"Error during search flights task initialization: {e}")

        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise CustomException(f"Unexpected error during search flights task initialization: {e}")
