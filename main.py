import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt'
)
logger = logging.getLogger('test_logger')

logger.info('This will not show up. ')
logger.warning('This will.')
logger.debug('This is a debug message')
logger.critical('A critical error ocurred.')

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""