import os

SRC_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.abspath(os.path.join(SRC_PATH, '..', 'data'))

RAW_DATA_PATH = os.path.join(DATA_PATH, 'raw')
EXTERNAL_DATA_PATH = os.path.join(DATA_PATH, 'external')
PROCESSED_DATA_PATH = os.path.join(DATA_PATH, 'processed')

HACKERNEWS_DATA_PATH = os.path.join(RAW_DATA_PATH, 'hackernews/')
