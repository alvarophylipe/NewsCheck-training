import sys
from src.log import logging
from src.exception import CustomException

def exception(func):
    def wrapper(*args, **kwargs):
        try:
            logging.info(f"Entered into the {func.__name__} function")
            result = func(*args, **kwargs)
            logging.info(f"{func.__name__} function executed sucessfully")
            return result
        except Exception as e:
            logging.error(f"Error in {func.__name__} function: {e}")
            raise CustomException(e, sys) from e
    return wrapper
