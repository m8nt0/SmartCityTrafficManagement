import logging

logger = logging.getLogger(__name__)

def track_error(error):
    logger.error(f"Error: {error}")
