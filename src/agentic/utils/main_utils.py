import re
from taskflowai import OpenaiModels, set_verbosity
import os  
from dotenv import load_dotenv
from src.agentic.logger import logging
from src.agentic.exception import CustomException

class FormatMarkdownImages:
    @classmethod
    def format_markdown_images(cls, markdown_text):
        """
        Keep markdown image syntax intact and ensure URLs are properly formatted.
        """
        try:
            logging.info("Starting markdown image formatting.")
            
            img_pattern = r'!\[(.*?)\]\((.*?)\)'
            
            def fix_url(match):
                alt_text, url = match.groups()
                url = url.strip()
                if not url.startswith(('http://', 'https://')):
                    url = f"https:{url}" if url.startswith('//') else f"https://{url}"
                return f'![{alt_text}]({url})'
            
            formatted_text = re.sub(img_pattern, fix_url, markdown_text)
            logging.info("Markdown image formatting completed successfully.")
            return formatted_text
        except Exception as e:
            logging.error(f"Error formatting markdown images: {e}")
            raise CustomException(f"An error occurred while formatting markdown images: {e}")

# Load environment variables
load_dotenv()

# Validate required API keys
required_keys = [
    "OPENAI_API_KEY"
]

# Check for missing keys
missing_keys = [key for key in required_keys if not os.getenv(key)]
if missing_keys:
    raise CustomException(f"Missing required API keys: {', '.join(missing_keys)}")

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
            logging.error(f"Failed to load OpenAI GPT-3.5-turbo model: {e}")
            raise CustomException(f"An error occurred while loading the OpenAI GPT-3.5-turbo model: {e}")
