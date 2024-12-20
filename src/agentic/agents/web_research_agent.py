from taskflowai import Agent, WebTools, WikipediaTools
from src.agentic.utils.main_utils import LoadModel

from src.agentic.logger import logging
from src.agentic.exception import CustomException
import sys
from src.agentic.tools.serper_search import SerperSearch
from src.agentic.tools.search_articles import WikiArticles
from src.agentic.tools.search_images import WikiImages


class WebResearchAgent:
    @classmethod
    def initialize_web_research_agent(cls):
        """
        Initializes and returns the Web Research Agent.
        """
        try:
            logging.info("Initializing Web Research Agent.")
            web_research_agent = Agent(
                role="Web Research Agent",
                goal="Research destinations and find relevant images",
                attributes="diligent, thorough, comprehensive, visual-focused",
                llm=LoadModel.load_openai_model(),
                tools=[SerperSearch.search_web(), WikiArticles.fetch_articles(), WikiImages.search_images()],
            )
            logging.info("Web Research Agent initialized successfully.")
            return web_research_agent

        except Exception as e:
            logging.info("Error initializing Web Research Agent")
            raise CustomException(sys, e)
