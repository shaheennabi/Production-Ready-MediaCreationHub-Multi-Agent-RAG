import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# List of files and directories relative to the current root
list_of_files = [
    ".github/workflows/deploy.yml",
    "deployment/app.py",
    "docs/Agentic RAG Pipeline.md",
    "docs/Types of Agentic RAG.md",
    "flowcharts/project_pipeline.png",
    "notebooks/TripPlanner_Multi_AI_Agent_Experimental.ipynb",
    "src/agentic/agents/reporter_agent.py",
    "src/agentic/agents/travel_agent.py",
    "src/agentic/agents/web_research_agent.py",
    "src/agentic/exception/__init__.py",
    "src/agentic/logger/__init__.py",
    "src/agentic/tools/get_weather_data.py",
    "src/agentic/tools/search_articles.py",
    "src/agentic/tools/search_flights.py",
    "src/agentic/tools/search_images.py",
    "src/agentic/tools/serper_search.py",
    "src/agentic/utils/__init__.py",
    "src/agentic/utils/main_utils.py",
    ".gitignore",
    "demo.py",
    "LICENSE",
    "README.md",
    "requirements.txt",
    "scripts.sh",
    "setup.py",
    "template.py"
]


# File and directory creation logic
for filepath in list_of_files:
    filepath = Path(filepath)

    # Split file directory and filename
    filedir, filename = os.path.split(filepath)

    # Create directories if needed
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Create file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")
