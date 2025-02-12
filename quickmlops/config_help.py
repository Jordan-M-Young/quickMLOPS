import constants
def conf(args: list) -> None:
    print(args)
    if len(args) < 2:
        print("To use the config command fully add one of the following commands:\n\t --help")
        return
    
    if args[2] != '--help':
        return print(f"Unknown arg '{args[2]}'")


    if len(args) < 3:
        print("To use the 'config --help' command fully add one of the following commands:\n\t sections\n\t Project\n\t Serve\n\t ML")
        return


    if args[3] == 'section' or args[3] == 'sections':
        print(constants.section_config_docs)

    if args[3] == 'ml' or args[3] == "ML":
        print(constants.ml_config_docs)
    
    if args[3] == 'project' or args[3] == 'Project':
        print(constants.project_config_docs)

    if args[3] == 'serve' or args[3] == 'Serve':
        print(constants.serve_config_docs)
