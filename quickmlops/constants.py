from enum import Enum
DOCS = """# {}\nThis is a test project. Woohoo. Please render."""


class ScikitLearn(Enum):
    kmeans = {"import_path":"cluster","class_instance":"KMeans"}
    random_forest_classifier = {"import_path":"ensemble","class_instance":"RandomForestClassifier"}
    linear_regression = {"import_path":"linear_model","class_instance":"LinearRegression"}


class MLFrameworks(Enum):
    SCIKIT_LEARN = "scikit-learn"
    PYTORCH = 'pytorch'


class ServeFrameworks(Enum):
    flask = 'flask'
    fastapi = 'fastapi'
    django = 'django'
    grpc = 'grcp'
    pyspark = 'pyspark'