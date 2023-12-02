import sys
from src.log import logging


def error_msg_detail(error_msg, func_name):
    error_message = 'Error occurred python class method or function [{}], error message [{}]'.format(
        func_name, str(error_msg)
    )

class CustomException(Exception):
    def __init__(self, error_msg, func_name: str) -> None:
        super().__init__(error_msg)
        self.error_msg = error_msg_detail(
            error_msg=error_msg,
            func_name=func_name
        )
    
    
    def __str__(self) -> str:
        return self.error_msg 

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
