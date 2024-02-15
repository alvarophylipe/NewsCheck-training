import os
import logging
from datetime import datetime

LOGFILE: str = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
logs_path: str = os.path.join(os.getcwd(), 'logs')

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOGFILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)