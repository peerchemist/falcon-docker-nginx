import sys
from loguru import logger

# init logging
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")
