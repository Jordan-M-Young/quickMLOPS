from quickmlops import constants


def conf(args: list) -> None:
    print(args)
    if len(args) < 2:
        print(
            "To use the config command fully add one of the following commands:\n\t --help"
        )
        return 0

    if args[2] != "--help":
        print(f"Unknown arg '{args[2]}'")
        return 1

    if len(args) < 3:
        print(
            "To use the 'config --help' command fully add one of the following commands:\n\t sections\n\t Project\n\t Serve\n\t ML"
        )
        return 2

    if args[3] == "Sections" or args[3] == "sections":
        print(constants.section_config_docs)
        return 3
    if args[3] == "ml" or args[3] == "ML":
        print(constants.ml_config_docs)
        return 4
    if args[3] == "project" or args[3] == "Project":
        print(constants.project_config_docs)
        return 5
    if args[3] == "serve" or args[3] == "Serve":
        print(constants.serve_config_docs)
        return 6

    print(f"Arg: {args[3]} not valid.")

    return 7
