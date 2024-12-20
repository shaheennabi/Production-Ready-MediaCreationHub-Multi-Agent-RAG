from taskflowai import Agent
from src.agentic.utils.main_utils import LoadModel
from src.agentic.tools.search_flights import SearchFlights
from src.agentic.tools.get_weather_data import WeatherTool
from src.agentic.logger import logging
from src.agentic.exception import CustomException
import sys


class TravelAgent:
    @classmethod
    def initialize_travel_agent(cls):
        try:
            logging.info("Initializing the Travel Agent.")

            travel_agent = Agent(
                role="Travel Agent",
                goal="Assist travelers with their queries",
                attributes="friendly, hardworking, and detailed in reporting back to users",
                llm=LoadModel.load_openai_model(),
                tools=[
                    
                ]
            )

            logging.info("Travel Agent initialized successfully.")
            return travel_agent

        except Exception as e:
            logging.info("An unexpected error occurred")
            raise CustomException(sys, e)

