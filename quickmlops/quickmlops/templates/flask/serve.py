from flask import Flask, request
from utils import load_model, inference

app = Flask(__name__)

MODEL_PATH = "../models/clf1.pkl"
model = load_model(MODEL_PATH)


@app.route("/version")
def version():
    return {"Version": "0.0.0", "Application": "Test"}


@app.route("/health")
def health():
    return 200


@app.route("/inference", methods=["POST"])
def inf():
    content = request.get_json()
    inp = content["input"]

    inf = inference(model, inp)

    return {"inference": inf}
