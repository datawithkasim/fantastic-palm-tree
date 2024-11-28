import logging
import os
from datetime import datetime

# Define log directory and file
LOG_DIR = os.path.join(os.getcwd(), "logs")
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
os.makedirs(LOG_DIR, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure the logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p'
)

# Example logging
logging.info("Logger is successfully configured and writing to the file.")