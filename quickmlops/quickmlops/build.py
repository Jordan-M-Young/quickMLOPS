import os
import toml
from quickmlops import constants
from quickmlops.utils import expand_path
from quickmlops.templates import scikit_learn, pytorch, flask


def build(args: list) -> None:
    if len(args) < 2:
        print(
            "To use the build command fully add the following commands:\n\t -i: Interactive Build\n\t -f <MY_QUICKMLOP_TOML>"
        )
        return

    if args[2] == "-i":
        print("Welcome to quickMLOPS interactive template builder.")
        print("More on this soon!.")

    if args[2] == "-f":
        if len(args) < 4:
            print(
                "Please add the path to a valid quickmlops.toml file after the -f flag."
            )
            return

        file_path = args[3]

        if not os.path.isfile(file_path):
            print(
                f"File: {file_path} cannot be found. Please recheck your file name/path."
            )
            return

        try:
            config = toml.load(file_path)
        except Exception as e:
            print(f"Error: {e}")
            return

        project = config.get("Project", {})
        project_dir = project.get("output_dir", "")

        project_dir = expand_path(project_dir)

        if not os.path.isdir(project_dir):
            os.mkdir(project_dir)

        build_project(config)
        print(f"Project built at {project_dir}")


def build_project(config: dict):
    project = config.get("Project", {})
    project_dir = project.get("output_dir", "")
    project_dir = expand_path(project_dir)

    write_readme(config, project_dir)
    write_requirements(config, project_dir)
    create_structure(config, project_dir)
    write_scripts(config, project_dir)


def write_scripts(config, project_dir):
    scripts_path = f"{project_dir}/scripts"
    if not os.path.isdir(scripts_path):
        os.mkdir(scripts_path)

    write_train_script(config, project_dir)


def write_train_script(config, project_dir):
    ml_frameworks_enum = constants.MLFrameworks
    project = config.get("Project", {})
    project_name = project.get("name", "app")

    scripts_path = f"{project_dir}/scripts"
    train_file_outpath = f"{scripts_path}/train.py"
    ml = config.get("ML", {})

    ml_framework = ml.get("framework", "scikit-learn")

    if ml_framework == ml_frameworks_enum.SCIKIT_LEARN.value:
        path = scikit_learn.__path__[0]
        train = f"{path}/train.py"
        train_file_str = read_python_file(train)

        ml_model = ml.get("model", "random_forest_classifier")

        sklearn_enum = constants.ScikitLearn

        model_injects = sklearn_enum[ml_model].value

        train_file_str = train_file_str.replace(
            "ensemble", model_injects["import_path"]
        ).replace("RandomForestClassifier", model_injects["class_instance"])

    elif ml_framework == ml_frameworks_enum.PYTORCH.value:
        path = pytorch.__path__[0]
        train = f"{path}/train.py"
        train_file_str = read_python_file(train)
        train_file_str = train_file_str.replace(
            "from utils", f"from {project_name}.utils"
        )

        train_file_str = train_file_str.replace(
            "from models", f"from {project_name}.models"
        )

    else:
        train_file_str = ""

    write_python_file(train_file_outpath, train_file_str)


def create_structure(config, project_dir):
    project_name = get_project_name(config)

    ml = config.get("ML", {})
    ml_framework = ml.get("framework", "scikit-learn")
    ml_framework_enum = constants.MLFrameworks
    app_path = f"{project_dir}/{project_name}"
    if not os.path.isdir(app_path):
        os.mkdir(app_path)
    if not os.path.isdir(f"{project_dir}/data"):
        os.mkdir(f"{project_dir}/data")
    if not os.path.isdir(f"{project_dir}/models"):
        os.mkdir(f"{project_dir}/models")

    write_init(app_path)
    write_serve(config, app_path)
    write_utils(config, app_path)

    print(ml_framework)
    if ml_framework == ml_framework_enum.PYTORCH.value:
        write_models(app_path)


def write_models(path):
    outpath = f"{path}/models.py"
    template_path = pytorch.__path__[0]
    models = f"{template_path}/models.py"
    models_file_str = read_python_file(models)

    write_python_file(outpath, models_file_str)


def write_utils(config, path):
    outpath = f"{path}/utils.py"

    ml_frameworks_enum = constants.MLFrameworks
    ml = config.get("ML", {})
    ml_framework = ml.get("framework", "scikit-learn")

    if ml_framework == ml_frameworks_enum.SCIKIT_LEARN.value:
        template_path = scikit_learn.__path__[0]
        utils = f"{template_path}/utils.py"
        utils_file_str = read_python_file(utils)

    elif ml_framework == ml_frameworks_enum.PYTORCH.value:
        template_path = pytorch.__path__[0]
        utils = f"{template_path}/utils.py"
        utils_file_str = read_python_file(utils)

    else:
        print(ml_framework, "not implemented yet!")
        utils_file_str = ""

    write_python_file(outpath, utils_file_str)


def write_serve(config, path):
    outpath = f"{path}/app.py"
    serve_frameworks_enum = constants.ServeFrameworks
    serve = config.get("Serve", {})
    serve_framework = serve.get("framework", "flask")

    if serve_framework == serve_frameworks_enum.flask.value:
        template_path = flask.__path__[0]
        serve = f"{template_path}/serve.py"
        serve_file_str = read_python_file(serve)

    else:
        print(serve_framework, "not implemented yet!")
        serve_file_str = ""

    write_python_file(outpath, serve_file_str)


def write_init(path: str):
    file = f"{path}/__init__.py"
    doc_string = '"""Init file Docstring."""'
    with open(file, "w") as file:
        file.write(doc_string)


def write_readme(config: dict, project_dir: str):
    project_name = get_project_name(config)
    readme = f"{project_dir}/README.md"
    serve = config.get("Serve", {})
    ml = config.get("ML", {})
    serve_framework = serve.get("framework", "flask")
    ml_framework = ml.get("framework", "scikit-learn")
    ml_model = ml.get("model", "random_forest_classifier")

    doc_formatted = constants.DOCS.format(
        project_name, serve_framework, ml_framework, ml_model
    )

    write_text_file(readme, doc_formatted)


def write_requirements(config: dict, project_dir: str):
    serve = config.get("Serve", {})
    ml = config.get("ML", {})

    serve_framework = serve.get("framework", "")
    ml_framework = ml.get("framework", "")
    req_file = f"{project_dir}/requirements.txt"

    if ml_framework == constants.MLFrameworks.SCIKIT_LEARN.value:
        ml_req = constants.scikit_requirements
    elif ml_framework == constants.MLFrameworks.PYTORCH.value:
        ml_req = constants.torch_requirements
    else:
        ml_req = ""

    if serve_framework == constants.ServeFrameworks.flask.value:
        serve_req = constants.flask_requirements
    else:
        serve_req = ""

    req_text = f"{constants.base_requirements}\n{ml_req}\n{serve_req}"

    write_text_file(req_file, req_text)


def read_python_file(file_path: str) -> str:
    with open(file_path, "r") as pfile:
        data = pfile.read()
    return data


def write_python_file(file_path: str, content: str):
    write_text_file(file_path, content)


def write_text_file(file_path: str, content: str):
    with open(file_path, "w") as rfile:
        rfile.write(content)


def get_project_name(config: dict) -> str:
    project = config.get("Project", {})
    return project.get("name", "app")
