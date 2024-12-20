import os
from taskflowai import WikipediaTools
from src.agentic.logger import logging
from src.agentic.exception import CustomException

class WikiArticles:
    @classmethod
    def get_wiki_articles(cls):
        """
        Sends a request to Wikipedia to retrieve information about a destination, event, or entity using the Wikipedia REST API.
        The response will include details on the specified topic for use with the LLM.
        """
        try:
            logging.info("Fetching articles using Wikipedia API.")
            articles = WikipediaTools.search_articles()
            logging.info("Successfully fetched articles from Wikipedia API.")
            return articles
        except Exception as e:
            logging.error(f"Failed to fetch articles from Wikipedia API: {e}")
            raise CustomException(f"An error occurred while fetching articles from Wikipedia API: {e}")
