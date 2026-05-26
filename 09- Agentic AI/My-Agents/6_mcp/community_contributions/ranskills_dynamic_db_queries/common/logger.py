# Owner: Maitreya Sapariya
# Project: Crest Training

import logging

from dotenv import load_dotenv


load_dotenv(override=True)


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
