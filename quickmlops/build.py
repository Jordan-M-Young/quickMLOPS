import os
import toml
def build(args: list) -> None:

    if len(args) < 2:
        print("To use the build command fully add the following commands:\n\t -i: Interactive Build\n\t -f <MY_QUICKMLOP_TOML>")
        return

    if args[2] == "-i":
        print("Welcome to quickMLOPS interactive template builder.")
        print("More on this soon!.")
    
    if args[2] == "-f":
        if len(args) < 4:
            print("Please add the path to a valid quickmlops.toml file after the -f flag.")
            return
        
        file_path = args[3]

        if not os.path.isfile(file_path):
            print(f"File: {file_path} cannot be found. Please recheck your file name/path.")
            return
        
        try:
            config = toml.load(file_path)
        except Exception as e:
            print(f"Error: {e}")
            return
        

        
        
        