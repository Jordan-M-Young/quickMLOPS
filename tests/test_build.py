from quickmlops.build import Builder, create_dir_if_nonex
import os
import shutil


DUMMY_APP = "dummy_app"
DUMMY_PROJECT = "./tests/assets/dummy_project"
DUMMY_APP_PATH = f"{DUMMY_PROJECT}/{DUMMY_APP}"


def test_create_dir_if_nonex():
    target = False
    real = os.path.isdir(DUMMY_PROJECT)

    assert real == target

    create_dir_if_nonex(DUMMY_PROJECT)

    target = True
    real = os.path.isdir(DUMMY_PROJECT)

    assert real == target

    target = False
    real = os.path.isdir(DUMMY_APP_PATH)

    assert target == real

    create_dir_if_nonex(DUMMY_APP_PATH)

    target = True
    real = os.path.isdir(DUMMY_APP_PATH)

    assert target == real


def test_write_init():
    config = {
        "Project": {"output_dir": DUMMY_PROJECT, "name": DUMMY_APP},
        "ML": {},
        "Serve": {},
    }

    builder = Builder(config)
    builder.write_init()
    target = True
    INIT_PATH = f"{DUMMY_APP_PATH}/__init__.py"
    real = os.path.isfile(INIT_PATH)

    assert target == real

    with open(INIT_PATH, "r") as f:
        real = f.read()

    target = '"""Init file Docstring."""'
    assert real == target


def test_dummy():
    shutil.rmtree(DUMMY_PROJECT)
    assert True
