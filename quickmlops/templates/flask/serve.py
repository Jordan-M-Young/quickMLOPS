from flask import Flask, request
import pickle
from utils import load_model, inference
app = Flask(__name__)

MODEL_PATH = "../models/clf1.pkl"
model = load_model(MODEL_PATH)

@app.route("/health")
def health():
    return {"Version":"0.0.0","Application":"Test"}

@app.route("/inference", methods=["POST"])
def inference():
    content = request.get_json()
    inp = content['input']

    inf = inference(model, inp)

    return {"inference": inf}








