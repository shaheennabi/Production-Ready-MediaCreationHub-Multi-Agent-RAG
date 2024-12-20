from taskflowai import Task
from src.agentic.agents.web_research_agent import WebResearchAgent
from src.agentic.logger import logging
from src.agentic.exception import CustomException

class ResearchDestinationTask:
    @classmethod
    def initialize_research_destination_task(cls, destination, interests):
        """Research destination with enhanced image handling"""
        try:
            logging.info(f"Initializing research destination task for: {destination} with interests: {interests}")
            
            instruction = (
                f"Create a comprehensive report about {destination} with the following:\n"
                f"1. Use Wikipedia tools to find and include 2-3 high-quality images of key attractions\n"
                f"2. Ensure images are full URLs starting with http:// or https://\n"
                f"3. Format images as: ![Description](https://full-image-url)\n"
                f"4. Include a brief caption for each image\n"
                f"5. Research attractions and activities related to: {interests}\n"
                f"6. Organize the report with proper headings and sections\n"
                f"7. Place images naturally throughout the content where relevant\n"
                f"8. Include practical visitor information\n"
                f"Format the entire response in clean markdown"
            )

            # Create a task to research the destination.
            report = Task.create(
                agent=WebResearchAgent.initialize_web_research_agent(),
                context=f"Destination: {destination}\nInterests: {interests}",
                instruction=instruction
            )

            logging.info("Research destination task initialized successfully.")
            return report

        except CustomException as e:
            logging.error(f"Custom exception occurred while initializing research destination task: {e}")
            raise CustomException(f"Error during research destination task initialization: {e}")

        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise CustomException(f"Unexpected error during research destination task initialization: {e}")
