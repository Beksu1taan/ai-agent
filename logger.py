import logging
import re
import os
from logging.handlers import RotatingFileHandler

class SecureFormatter(logging.Formatter):
    def format(self, record):
        message = super().format(record)
        message = re.sub(r'sk-ant-api\d[a-zA-Z0-9\-_]+', 'sk-ant-api-***[REDACTED]', message)
        return message

def setup_logger():
    if not os.path.exists('logs'):
        os.makedirs('logs')

    logger = logging.getLogger('SecureAgent')
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler('logs/agent.log', maxBytes=1024*1024, backupCount=3)
    formatter = SecureFormatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
   
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger

logger = setup_logger()
