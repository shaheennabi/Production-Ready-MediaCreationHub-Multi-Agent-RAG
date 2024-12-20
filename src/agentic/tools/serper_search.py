import os
from taskflowai import WebTools
from src.agentic.logger import logging
from src.agentic.exception import CustomException

# Validate required API keys
required_keys = [
    "SERPER_API_KEY",
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


class SerperSearch:
    @classmethod
    def perform_search(cls):
        """
        Sends an API request to the Serper API to search the web and retrieve relevant information.
        The response provides context or information for the LLM to make decisions or enhance understanding of a specified topic.
        """
        try:
            logging.info("Performing search using Serper API.")
            search_results = WebTools.serper_search()
            logging.info("Successfully retrieved search results from Serper API.")
            return search_results
        except Exception as e:
            logging.error(f"Failed to fetch search results from Serper API: {e}")
            raise CustomException(f"An error occurred while performing search with Serper API: {e}")
