import sys
from build import build
def main(args: list) -> None:

    if len(args) < 2:
        print("Welcome to quickMLOPS")
        print("""Use one of the following commands to get started:\n\t- build\n\t- delete""")
        return

    if args[1] == "build":
        print("build selected!")
        build(args)
        return  

    if args[1] == 'delete':
        print("delete selected!")
        return


if __name__ == "__main__":
    args = sys.argv
    main(args)