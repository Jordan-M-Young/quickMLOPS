import os


def expand_path(path: str) -> str:
    if "~" in path:
        path = os.path.expanduser(path)
    return path
