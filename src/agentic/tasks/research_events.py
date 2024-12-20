from taskflowai import Task
from src.agentic.agents.web_research_agent import WebResearchAgent
from src.agentic.logger import logging
from src.agentic.exception import CustomException


class ResearchEventsTask:
    @classmethod
    def initialize_research_events_task(cls, destination, dates, interests):
        """Research events with enhanced image handling"""
        try:
            logging.info(f"Initializing research events task for destination: {destination}, dates: {dates}, and interests: {interests}")
            
            instruction = (
                f"Research events in {destination} during {dates} that match these interests: {interests}.\n\n"
                f"For each event, include:\n"
                f"- Event name\n"
                f"- Date and time\n"
                f"- Venue/location\n"
                f"- Ticket information (if applicable)\n"
                f"- A short description of the event\n"
                f"- Format event images as: ![Event Name](https://full-image-url)\n"
                f"- Format images as: ![Description](https://full-image-url)\n"
                f"- Ensure images are full URLs starting with http:// or https://\n"
                f"- Information is accurate and up-to-date\n"
                f"- Place images naturally throughout the content where relevant\n"
                f"- Format the entire response in clean markdown"
            )

            # Create a task to research the events.
            report = Task.create(
                agent=WebResearchAgent.initialize_web_research_agent(),
                context=f"Destination: {destination}\nDates: {dates}\nInterests: {interests}",
                instruction=instruction
            )

            logging.info("Research events task initialized successfully.")
            return report

        except CustomException as e:
            logging.error(f"Custom exception occurred while initializing research events task: {e}")
            raise CustomException(f"Error during research events task initialization: {e}")

        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise CustomException(f"Unexpected error during research events task initialization: {e}")
