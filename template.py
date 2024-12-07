import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# List of files and directories relative to the current root
list_of_files = [
    "PRODUCTION-READY-MULTI-AGENT-RAG-PROJECT",  # directory, not a file
    ".github/FUNDING.yml",
    "docs/.gitkeep",
    "notebooks/.gitkeep",
    "flowcharts/.gitkeep",
    "src/agentic/.gitkeep",  
    ".gitignore",
    "demo.py",
    "LICENSE",
    "README.md",
    "requirements.txt",
    "setup.py",
    "template.py",
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