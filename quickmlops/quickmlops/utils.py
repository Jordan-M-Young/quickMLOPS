import os


def expand_path(path: str) -> str:
    if "~" in path:
        path = os.path.expanduser(path)
    return path


def section_validation(section: str, config: dict) -> bool:
    if not config.get(section):
        print(f"Invalid quickmlops.toml: [{section}] section required.")
        return False

    return True


def config_validation(config: dict) -> bool:
    if not section_validation("ML", config):
        return False
    if not section_validation("Serve", config):
        return False
    if not section_validation("Project", config):
        return False

    return True
