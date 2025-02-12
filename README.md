# quickMLOPS
Machine Learning Operations (MLOPs) SDK for Python

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

To see valid fields for reach of these sections

```bash
python3 quickmlops ls <SECTION>
```

To see valid values for a given field of a given section:

```bash
python3 quickmlops ls <SECTION> <FIELD>
```


