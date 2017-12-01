import os
import glob
import pandas as pd

from ..config import HACKERNEWS_DATA_PATH


def get_hackernews_files():
    files = glob.glob(HACKERNEWS_DATA_PATH + '*')
    if not files:
        raise ValueError("No hackernews files found. Are you sure they exist in {}?".format(HACKERNEWS_DATA_PATH))
    return files


def load_hackernews_dataframe(file_path=os.path.join(HACKERNEWS_DATA_PATH, "HN_2006")):
    with open(file_path) as f:
        try:
            file_content = f.read()
        except MemoryError as _:
            raise MemoryError("{} is too large for my memory :-(".format(file_path))
    file_content = file_content.rstrip()
    file_content = file_content.replace('}\n{', '},{')
    file_content = "[{}]".format(file_content)

    try:
        df = pd.read_json(file_content)
    except ValueError as _:
        raise MemoryError("{} is too large for my memory :-(".format(file_path))
    return df