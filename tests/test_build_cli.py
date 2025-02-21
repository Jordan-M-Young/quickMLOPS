from quickmlops.build import get_project_name, read_python_file, build


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


def test_build_less_than_two_args():
    args = []

    exit = build(args)
    target = 0

    assert exit == target


def test_build_interactive():
    args = ["quickmlops", "build", "-i"]

    exit = build(args)
    target = 1

    assert exit == target


def test_build_incomplete_file_build():
    args = ["quickmlops", "build", "-f"]

    exit = build(args)
    target = 2

    assert exit == target


def test_build_config_not_found():
    args = ["quickmlops", "build", "-f", "notafile.toml"]

    exit = build(args)
    target = 3

    assert exit == target
