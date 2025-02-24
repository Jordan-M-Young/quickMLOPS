import pickle
from xgboost import XGBClassifier


def load_model(model_path: str):
    model = XGBClassifier()
    model.load_model(model_path)
    return model


def inference(model, features):
    return model.predict(features)
