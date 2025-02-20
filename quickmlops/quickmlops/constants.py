from enum import Enum

DOCS = """# {}\n\nThis project repository contains an application built on 
the {} framework. Using the {} framework, this application generates inferences
via  a custom trained {} model.

# Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

# Train Model

```bash
python3 ./scripts/train.py
```

# Run Application

To run this application, run the following command:

```bash
dummy command
```

 """


class ScikitLearn(Enum):
    kmeans = {"import_path": "cluster", "class_instance": "KMeans"}
    random_forest_classifier = {
        "import_path": "ensemble",
        "class_instance": "RandomForestClassifier",
    }
    linear_regression = {
        "import_path": "linear_model",
        "class_instance": "LinearRegression",
    }
    logistic_regression = {
        "import_path":"linear_model",
        "class_instance":"LogisticRegression"
    }
    k_nearest_neighbors_classifier = {
        "import_path":"neighbors",
        "class_instance":"KNeighborsClassifier"
    }


class MLFrameworks(Enum):
    SCIKIT_LEARN = "scikit-learn"
    PYTORCH = "pytorch"
    XGBOOST = 'xgboost'


class ServeFrameworks(Enum):
    flask = "flask"
    fastapi = "fastapi"


base_requirements = "pandas\nnumpy\npickle"
torch_requirements = "torch"
scikit_requirements = "scikit-learn"
flask_requirements = "flask"
fastapi_requirements = 'fastapi'
xgboost_requirements = 'xgboost'

section_config_docs = """\n\n


  ___         _   _                             
 / __| ___ __| |_(_)___ _ _                     
 \__ \/ -_) _|  _| / _ \ ' \                    
 |___/\___\__|\__|_\___/_||_|
                                     
------------------------------
------------------------------                                   


Each quickmlops.toml file needs three sections:
    - Project
    - Serve
    - ML

To learn more about the fields of these sections, 
see an example quickmlops.toml file at https://github.com/Jordan-M-Young/quickMLOPS/blob/main/quickmlops.toml
or run:

python3 quickmlops config --help <SECTION_NAME>

------------------------------
------------------------------    

\n\n
"""

ml_config_docs = """\n\n

  __  __ _    
 |  \/  | |   
 | |\/| | |__ 
 |_|  |_|____|
--------------------
--------------------


Each quickmlops.toml file requires an ML section. This section of the 
file controls what ML model/framework will be integrated in with
your built project. The two fields required for this section are:

\t- framework
\t- model

The framework field controls which python ml framework
will be integreated with the built project.
Currently the options for framework are:

\t- scikit-learn


The model field controls which kind of model will be
integrated with the built project. Models are contingent
on the chose framework. We list available model values for each 
valid framework:

\t - scikit-learn
\t\t -linear_regression
\t\t -kmeans
\t\t -random_forest_classification

--------------------
--------------------
\n\n
"""


serve_config_docs = """
  ___                  
 / __| ___ _ ___ _____ 
 \__ \/ -_) '_\ V / -_)
 |___/\___|_|  \_/\___|
-------------------------
-------------------------

Each quickmlops.toml file requires a '[Serve]' section.
This section controls how the the project will be served.
For the serve section, the fields to consider are:

\t- framework

The framework field controls which python framework will be used
to serve our ML models. Currently these are the valid values for
the framework field:

\t- flask

-------------------------
-------------------------
\n\n
"""

project_config_docs = """
  ___          _        _   
 | _ \_ _ ___ (_)___ __| |_ 
 |  _/ '_/ _ \| / -_) _|  _|
 |_| |_| \___// \___\__|\__|
            |__/            
-----------------------------
-----------------------------

Each quickmlops.toml field requires a '[Project]' section.
This section controls how and where the project will be built.
The fields to consider for this section are:

\t- name
\t -output_dir
\t -manage


The name field is simply the name of the project you'll build, this 
can be any string that works as a directory name for your os.


The output_dir field is the location you want your project to be built.
This will make a new directory if the location does not exist.

The manage field is how you want your python environment to be managed.
Currently, valid values for manage are:

\t- pip

-----------------------------
-----------------------------
"""
