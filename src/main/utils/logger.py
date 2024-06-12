import logging, os


script_directory = os.path.dirname(os.path.abspath(__file__))

def configure_logging(log_level = logging.INFO):

    logging.basicConfig(level = log_level, format = '%(asctime)s - %(levelname)s - %(message)s')
    log_directory = os.path.join(script_directory, "../../../logs/test_logs.log")
    
    ch = logging.StreamHandler()
    fh = logging.FileHandler(log_directory)
    fh.setLevel(log_level)
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(fh)
    logger.addHandler(ch)
    
    return logger
