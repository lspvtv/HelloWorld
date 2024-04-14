import os

CURRENT_DIR = os.path.dirname(__file__)
FILES_DIR = os.path.join(CURRENT_DIR, 'files')


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)
