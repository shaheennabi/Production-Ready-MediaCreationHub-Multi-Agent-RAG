import os
from taskflowai import WikipediaTools
from src.agentic.logger import logging
from src.agentic.exception import CustomException

class WikiImages:
    @classmethod
    def get_wiki_images(cls):
        """
        Sends a request to Wikipedia to retrieve images using the Wikipedia REST API.
        The response will include images for use with the LLM.
        """
        try:
            logging.info("Fetching images using Wikipedia API.")
            images = WikipediaTools.search_images()
            logging.info("Successfully fetched images from Wikipedia API.")
            return images
        except Exception as e:
            logging.error(f"Failed to fetch images from Wikipedia API: {e}")
            raise CustomException(f"An error occurred while fetching images from Wikipedia API: {e}")
