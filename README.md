# quickMLOPS
QuickMLOPS is a Machine Learning Operations (MLOPs) SDK for Python. Quickmlops can be used
to quickly build out fully functioning ML projects and serve them. Quickmlops allows
users to build projects using the most common python ML frameworks including Scikit-Learn
and Pytorch and serve them with popular API frameworks like flask and fastapi.

# Getting Started

## Installation

```bash
pip install quickmlops
```

## Build a project. 

To build a project run the following:

```bash
python3 quickmlops build -f <MY_QUICKMLOPS_TOML_FILE>
```

This will build your project according to the configuration specified in your quickmlops.toml file.

## Configuration

Currently your project build is controlled by the configuration detailed in a quickmlops.toml file. Currently this file has three main sections:

- Project: Controls project specifics (project name, output directory, python management)
- Serve: Controls how your ML model(s) will be served. The main field to select is framework (default is flask)
- ML: Controls which ML models / framework will be integrated into your built project.

For help on building a valid quickmlops.toml see an example file [here](https://github.com/Jordan-M-Young/quickMLOPS/blob/main/quickmlops.toml) or run:

```bash
python3 quickmlops config --help <SECTION>
```

## Supported Frameworks

### ML

- Scikit-Learn
- Pytorch

### Serving

- flask
- fastapi

