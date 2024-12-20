from taskflowai import WebTools
from src.agentic.logger import logging
from src.agentic.exception import CustomException
import sys

class SerperSearch:
    @classmethod
    def search_web(cls):
        try:
            logging.info("Performing web search using SerperSearch tool.")
            search = WebTools.serper_search
            logging.info("Web search completed successfully.")
            return search
        except Exception as e:
            logging.info("Failed to perform web search.")
            raise CustomException(sys, e)
