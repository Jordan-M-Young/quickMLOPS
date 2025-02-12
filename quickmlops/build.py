import os
import toml
import constants
from utils import expand_path
from templates import scikit_learn, pytorch
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

        build_project(config)


def build_project(config: dict):
        write_readme(config)
        write_requirements(config)
        create_structure(config)
        write_scripts(config)


def write_scripts(config):
    project = config.get("Project",{})
    project_dir = project.get("output_dir","")
    project_dir = expand_path(project_dir)
    scripts_path = f'{project_dir}/scripts'
    if not os.path.isdir(scripts_path):
        os.mkdir(scripts_path)

    write_train_script(config)

def write_train_script(config):
    ml_frameworks_enum = constants.MLFrameworks


    project = config.get("Project",{})
    project_dir = project.get("output_dir","")
    project_dir = expand_path(project_dir)
    scripts_path = f'{project_dir}/scripts'
    train_file_outpath = f'{scripts_path}/train.py'
    ml = config.get("ML",{})

    ml_framework = ml.get("framework","scikit-learn")


    if ml_framework == ml_frameworks_enum.SCIKIT_LEARN.value:
        path = scikit_learn.__path__[0]
        train = f'{path}/train.py'
        train_file_str = read_python_file(train)

        ml_model = ml.get("model","random_forest_classifier")

        sklearn_enum = constants.ScikitLearn

        model_injects = sklearn_enum[ml_model].value

        train_file_str = train_file_str.replace(
            "ensemble",model_injects["import_path"]
            ).replace(
                "RandomForestClassifier",
                model_injects['class_instance'])


    else:
        train_file_str = ""

    
    write_python_file(train_file_outpath,train_file_str)






def create_structure(config):
    project = config.get("Project",{})
    project_dir = project.get("output_dir","")
    project_dir = expand_path(project_dir)

    project_name = project.get("name","app")

    app_path  = f'{project_dir}/{project_name}'
    if not os.path.isdir(app_path):
        os.mkdir(app_path)

    write_init(app_path)

def write_init(path: str):
    file = f'{path}/__init__.py'
    doc_string = '"""Init file Docstring."""'
    with open(file, 'w') as file:
        file.write(doc_string)

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

    req_text = f"{serve_framework}\n{ml_framework}\npickle"

    with open(req_file,"w") as rfile:
        rfile.write(req_text)

        

def read_python_file(file_path: str) -> str:
    with open(file_path, 'r') as pfile:
        data = pfile.read()
    return data


def write_python_file(file_path: str, content: str):
    with open(file_path, 'w') as pfile:
        pfile.write(content)