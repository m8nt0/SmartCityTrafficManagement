import time
import logging

logger = logging.getLogger(__name__)

def monitor_performance(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logger.info(f"Function {func.__name__} executed in {elapsed_time:.2f} seconds")
        return result
    return wrapper
