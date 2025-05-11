import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    # filename='./objects/logs/logs.log',
    # filemode='w'
)

logger = logging.getLogger(__name__)