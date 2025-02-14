from quickmlops.build import get_project_name, read_python_file


def test_get_project_name():
    config = {"Project": {"name": "test"}}

    target = "test"

    project_name = get_project_name(config)

    assert target == project_name

    config = {"Project": {}}

    target = "app"

    project_name = get_project_name(config)

    assert target == project_name


def test_read_python_file():
    file = "./tests/assets/dummy.py"

    target = """def fn(x: int) -> float:
    return float(x)\n"""

    python_str = read_python_file(file)

    assert target == python_str
