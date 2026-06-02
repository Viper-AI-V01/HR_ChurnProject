import logging
import os
from datetime import datetime
x = datetime.now()
FILE_PATH = f'{x.strftime('%m_%d_%Y_%H_%M_%S')}.log'
LOG_PATH = os.path.join(os.getcwd(),'logs')
os.makedirs(LOG_PATH,exist_ok=True)
LOG_FILE_PATH = os.path.join(LOG_PATH,FILE_PATH)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s]-%(lineno)d-%(levelname)s-%(message)s',
    level=logging.INFO,)
