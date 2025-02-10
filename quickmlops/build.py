import os
import toml
import constants
from utils import expand_path

def build(args: list) -> None:
    print(args)
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
        

        print(config)

        project = config.get("Project",{})
        project_dir = project.get("output_dir","")

        project_dir = expand_path(project_dir)

        if not os.path.isdir(project_dir):
            os.mkdir(project_dir)

        write_readme(config)
        write_requirements(config)

def write_readme(config: dict):
    project = config.get("Project",{})
    project_dir = project.get("output_dir","")
    project_dir = expand_path(project_dir)

    project_name  = project.get("name","")
    readme = f'{project_dir}/README.md'
    doc_formatted = constants.DOCS.format(project_name)
    with open(readme,'w') as file:
        file.write(doc_formatted)
    
        

def write_requirements(config: dict):
    project = config.get("Project",{})
    serve = config.get("Serve",{})
    ml = config.get("ML",{})

    serve_framework = serve.get("framework","")
    ml_framework = ml.get("framework","")
    project_dir = project.get("output_dir","")
    project_dir = expand_path(project_dir)
    req_file = f'{project_dir}/requirements.txt'

    req_text = f"{serve_framework}\n{ml_framework}"

    with open(req_file,"w") as rfile:
        rfile.write(req_text)

        
        