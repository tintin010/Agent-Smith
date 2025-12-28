import logging
import os
from datetime import datetime
from config import LOG_DIR

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    filename = f"{datetime.now().strftime('%Y%m%d')}.log"
    handler = logging.FileHandler(os.path.join(LOG_DIR, filename), encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger