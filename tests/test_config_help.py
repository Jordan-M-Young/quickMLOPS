from quickmlops.config_help import conf


def test_conf_args_less_than_two():
    args = []
    exit = conf(args)
    target = 0
    assert target == exit
