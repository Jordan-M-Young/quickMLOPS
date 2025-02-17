import os
import toml
from quickmlops import constants
from quickmlops.utils import expand_path
from quickmlops.templates import scikit_learn, pytorch, flask, docker


def build(args: list) -> None:
    if len(args) < 2:
        print(
            "To use the build command fully add the following commands:\n\t -i: Interactive Build\n\t -f <MY_QUICKMLOP_TOML>"
        )
        return

    if args[2] == "-i":
        print("Welcome to quickMLOPS interactive template builder.")
        print("More on this soon!.")
        return
        # config = get_interactive_config()

    elif args[2] == "-f":
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

        builder = Builder(config=config)
        builder.build_project()
    else:
        print(f"Arg: '{args[2]}' not valid!")
        return


class Builder:
    def __init__(self, config: dict):
        self.config = config
        self.project_name = get_project_name(self.config)
        self.ml = self.config["ML"]
        self.serve = self.config["Serve"]
        self.project = self.config["Project"]
        self.project_dir = get_project_dir(self.config)
        self.app_path = f"{self.project_dir}/{self.project_name}"
        self.init_directory()

    def init_directory(self):
        if not os.path.isdir(self.project_dir):
            os.mkdir(self.project_dir)

    def build_project(self):
        self.write_readme()
        self.write_requirements()
        self.create_structure()
        self.write_scripts()
        self.write_dockerfile()
        self.write_docker_entrypoint()

    def create_structure(self):
        ml_framework = self.ml.get("framework", "scikit-learn")
        ml_framework_enum = constants.MLFrameworks
        if not os.path.isdir(self.app_path):
            os.mkdir(self.app_path)
        if not os.path.isdir(f"{self.project_dir}/data"):
            os.mkdir(f"{self.project_dir}/data")
        if not os.path.isdir(f"{self.project_dir}/models"):
            os.mkdir(f"{self.project_dir}/models")

        self.write_init()
        self.write_serve()
        self.write_utils()

        print(ml_framework)
        if ml_framework == ml_framework_enum.PYTORCH.value:
            self.write_models()

    def write_readme(self):
        readme = f"{self.project_dir}/README.md"

        serve_framework = self.serve.get("framework", "flask")
        ml_framework = self.ml.get("framework", "scikit-learn")
        ml_model = self.ml.get("model", "random_forest_classifier")

        doc_formatted = constants.DOCS.format(
            self.project_name, serve_framework, ml_framework, ml_model
        )

        write_text_file(readme, doc_formatted)

    def write_requirements(self):
        serve_framework = self.serve.get("framework", "")
        ml_framework = self.ml.get("framework", "")
        req_file = f"{self.project_dir}/requirements.txt"

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

    def write_dockerfile(self) -> None:
        template_path = docker.__path__[0]
        dockerfile = f"{template_path}/Dockerfile"
        dockerfile_str = read_text_file(dockerfile)
        outpath = f"{self.project_dir}/Dockerfile"
        write_text_file(outpath, dockerfile_str)

    def write_docker_entrypoint(self) -> None:
        template_path = docker.__path__[0]
        entry_script = f"{template_path}/entrypoint.sh"
        entry_script_str = read_text_file(entry_script)
        outpath = f"{self.project_dir}/entrypoint.sh"
        write_text_file(outpath, entry_script_str)

    def write_scripts(self) -> None:
        scripts_path = f"{self.project_dir}/scripts"
        if not os.path.isdir(scripts_path):
            os.mkdir(scripts_path)

        self.write_train_script()

    def write_train_script(self) -> None:
        ml_frameworks_enum = constants.MLFrameworks

        scripts_path = f"{self.project_dir}/scripts"
        train_file_outpath = f"{scripts_path}/train.py"

        ml_framework = self.ml.get("framework", "scikit-learn")

        if ml_framework == ml_frameworks_enum.SCIKIT_LEARN.value:
            path = scikit_learn.__path__[0]
            train = f"{path}/train.py"
            train_file_str = read_python_file(train)

            ml_model = self.ml.get("model", "random_forest_classifier")

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
                "from utils", f"from {self.project_name}.utils"
            )

            train_file_str = train_file_str.replace(
                "from models", f"from {self.project_name}.models"
            )

        else:
            train_file_str = ""

        write_python_file(train_file_outpath, train_file_str)

    def write_models(self):
        outpath = f"{self.app_path}/models.py"
        template_path = pytorch.__path__[0]
        models = f"{template_path}/models.py"
        models_file_str = read_python_file(models)

        write_python_file(outpath, models_file_str)

    def write_utils(self) -> None:
        outpath = f"{self.app_path}/utils.py"

        ml_frameworks_enum = constants.MLFrameworks
        ml_framework = self.ml.get("framework", "scikit-learn")

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

    def write_serve(self) -> None:
        outpath = f"{self.app_path}/app.py"
        serve_frameworks_enum = constants.ServeFrameworks
        serve_framework = self.serve.get("framework", "flask")

        if serve_framework == serve_frameworks_enum.flask.value:
            template_path = flask.__path__[0]
            serve = f"{template_path}/serve.py"
            serve_file_str = read_python_file(serve)

        else:
            print(serve_framework, "not implemented yet!")
            serve_file_str = ""

        write_python_file(outpath, serve_file_str)

    def write_init(self) -> None:
        file = f"{self.app_path}/__init__.py"
        doc_string = '"""Init file Docstring."""'
        write_python_file(file, doc_string)


def read_python_file(file_path: str) -> str:
    with open(file_path, "r") as pfile:
        data = pfile.read()
    return data


def write_python_file(file_path: str, content: str) -> None:
    write_text_file(file_path, content)


def write_text_file(file_path: str, content: str) -> None:
    with open(file_path, "w") as rfile:
        rfile.write(content)


def read_text_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()


def get_project_name(config: dict) -> str:
    project = config.get("Project", {})
    return project.get("name", "app")


def get_project_dir(config):
    project = config.get("Project", {})
    project_dir = project.get("output_dir", "")
    return expand_path(project_dir)
