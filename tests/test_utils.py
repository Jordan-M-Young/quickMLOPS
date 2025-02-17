from quickmlops.utils import expand_path
import os


def test_expand_path():
    path = "/home/test"
    target = expand_path(path)
    assert path == target

    path = "~/test"
    expand = expand_path(path)

    target = f"{os.getenv('HOME')}/test"

    assert expand == target
