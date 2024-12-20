from taskflowai import WikipediaTools
from src.agentic.logger import logging
from src.agentic.exception import CustomException
import sys

class WikiImages:
    @classmethod
    def search_images(cls):
        try:
            logging.info("Searching images using WikipediaTools.")
            images = WikipediaTools.search_images
            logging.info("Images searched successfully.")
            return images
        except Exception as e:
            logging.info("Failed to search images from Wikipedia.")
            raise CustomException(sys, e)
