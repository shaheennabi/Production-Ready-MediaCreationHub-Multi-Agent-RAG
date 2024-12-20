from taskflowai import Task
from src.agentic.agents.travel_agent import TravelAgent
from src.agentic.logger import logging
from src.agentic.exception import CustomException


class ResearchWeatherTask:
    @classmethod
    def initialize_research_weather_task(cls, destination, dates):
        """Research weather information"""
        try:
            logging.info(f"Initializing research weather task for destination: {destination} and dates: {dates}")
            
            report = Task.create(
                agent=TravelAgent.initialize_travel_agent(),
                context=f"Destination: {destination}\nDates: {dates}",
                instruction=(
                    "Provide detailed weather information including:\n"
                    "1. Temperature ranges\n"
                    "2. Precipitation chances\n"
                    "3. General weather patterns\n"
                    "4. Recommended clothing/gear"
                )
            )

            logging.info("Research weather task initialized successfully.")
            return report

        except CustomException as e:
            logging.error(f"Custom exception occurred while initializing research weather task: {e}")
            raise CustomException(f"Error during research weather task initialization: {e}")

        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise CustomException(f"Unexpected error during research weather task initialization: {e}")
