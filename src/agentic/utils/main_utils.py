import re
from taskflowai import OpenaiModels, set_verbosity
import os  
from dotenv import load_dotenv
from src.agentic.logger import logging
from src.agentic.exception import CustomException
import sys

# Load environment variables
load_dotenv()

# Validate required API keys
required_keys = [
    "OPENAI_API_KEY"
]

# Check for missing keys
missing_keys = [key for key in required_keys if not os.getenv(key)]
if missing_keys:
    raise CustomException(sys, "Missing required environment variables: " + ', '.join(missing_keys))

# Set verbosity for taskflowai
set_verbosity(True)

class LoadModel:
    @classmethod
    def load_openai_model(cls):
        """
        Load and return the OpenAI GPT-3.5-turbo model.
        """
        try:
            logging.info("Loading OpenAI GPT-3.5-turbo model.")
            model = OpenaiModels.gpt_3_5_turbo
            logging.info("OpenAI GPT-3.5-turbo model loaded successfully.")
            return model
        except Exception as e:
            logging.info("Failed to load OpenAI GPT-3.5-turbo model")
            raise CustomException(sys, e)
