from quickmlops.utils import expand_path, section_validation, config_validation
import os


def test_expand_path():
    path = "/home/test"
    target = expand_path(path)
    assert path == target

    path = "~/test"
    expand = expand_path(path)

    target = f"{os.getenv('HOME')}/test"

    assert expand == target


def test_section_validation():
    config = {"ML": "foo"}
    section = "ML"

    target = True
    real = section_validation(section, config)

    assert target == real

    config = {"Serve": "foo"}
    section = "ML"

    target = False
    real = section_validation(section, config)

    assert target == real


def test_config_validation():
    config = {"ML": "foo", "Serve": "bar", "Project": "test"}

    target = True
    real = config_validation(config)

    assert target == real

    config = {"Serve": "bar", "Project": "test"}

    target = False
    real = config_validation(config)

    assert target == real

    config = {"ML": "bar", "Project": "test"}

    target = False
    real = config_validation(config)

    assert target == real

    config = {"ML": "bar", "Serve": "test"}

    target = False
    real = config_validation(config)

    assert target == real
