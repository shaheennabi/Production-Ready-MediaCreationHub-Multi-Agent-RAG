from taskflowai import Agent
from src.agentic.utils.main_utils import LoadModel
from src.agentic.logger import logging
from src.agentic.exception import CustomException


class TravelReportAgent:
    @classmethod
    def initialize_travel_report_agent(cls):
        try:
            logging.info("Initializing the Travel Report Agent.")

            travel_report_agent = Agent(
                role="Travel Report Agent",
                goal="Write comprehensive travel reports with visual elements",
                attributes="friendly, hardworking, visual-oriented, and detailed in reporting",
                llm=LoadModel.load_openai_model()
            )

            logging.info("Travel Report Agent initialized successfully.")
            return travel_report_agent

        except CustomException as e:
            logging.error(f"Custom exception occurred while initializing the agent: {e}")
            raise CustomException(f"Error during agent initialization: {e}")

        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise CustomException(f"Unexpected error during agent initialization: {e}")
