import datetime
import logging
import os , sys
from pathlib import Path


sys.path.append("C:/Users/sndpt/OneDrive/Desktop/PY-TEST/AutomationProjectEcom")

def custom_log(log_Level = logging.DEBUG):

    logger = logging.getLogger("test_Logger")

    logger.setLevel(log_Level)

    format = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s -%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    
    script_dir = os.path.dirname(__file__)

    path = '../../logs/automation.log'

    log_file_path = os.path.join(script_dir , path)

    fh = logging.FileHandler(log_file_path )
    
    fh.setLevel(log_Level)
    fh.setFormatter(format)

    logger.addHandler(fh)

    return logger
