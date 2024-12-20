from taskflowai import Task
from src.agentic.agents.reporter_agent import TravelReportAgent
from src.agentic.logger import logging
from src.agentic.exception import CustomException
from src.agentic.tasks.research_destination_task import ResearchDestinationTask
from src.agentic.tasks.research_events import ResearchEventsTask
from src.agentic.tasks.research_weather import ResearchWeatherTask
from src.agentic.tasks.search_flights import SearchFlightsTask





class WriteTravelReportTask:
    def __init__(self):
        try:
            logging.info("Initializing the WriteTravelReportTask.")
            
            # Initialize reports
            self.destination_report = ResearchDestinationTask.initialize_research_destination_task()
            self.events_report = ResearchEventsTask.initialize_research_events_task()
            self.weather_report = ResearchWeatherTask.initialize_research_weather_task()
            self.flight_report = SearchFlightsTask.initialize_search_flights_task()
            
            logging.info("All reports initialized successfully.")
        
        except CustomException as e:
            logging.error(f"Custom exception occurred while initializing reports: {e}")
            raise CustomException(f"Error during report initialization: {e}")
        
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise CustomException(f"Unexpected error during report initialization: {e}")

    @classmethod
    def initialize_write_travel_report_task(cls):
        """Create final travel report"""
        instruction = (
            "Create a comprehensive travel report that:\n"
            "1. Maintains all images from the destination and events reports\n"
            "2. Organizes information in a clear, logical structure\n"
            "3. Keeps all markdown formatting intact\n"
            "4. Ensures images are properly displayed with captions\n"
            "5. Includes all key information from each section"
        )
        
        try:
            logging.info("Generating the final travel report.")
            
            report = Task.create(
                agent=TravelReportAgent.initialize_travel_report_agent(),
                context=f"Destination Report: {self.destination_report}\n\n"
                        f"Events Report: {self.events_report}\n\n"
                        f"Weather Report: {self.weather_report}\n\n"
                        f"Flight Report: {self.flight_report}",
                instruction=instruction
            )
            
            logging.info("Travel report created successfully.")
            return report
        
        except CustomException as e:
            logging.error(f"Custom exception occurred while creating the travel report: {e}")
            raise CustomException(f"Error during travel report creation: {e}")
        
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise CustomException(f"Unexpected error during travel report creation: {e}")
