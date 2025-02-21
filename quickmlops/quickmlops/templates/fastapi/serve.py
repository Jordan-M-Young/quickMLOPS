from fastapi import FastAPI
from utils import load_model, inference

app = FastAPI()
MODEL_PATH = "../models/clf1.pkl"
model = load_model(MODEL_PATH)


@app.get("/version")
def version():
    return {"Version": "0.0.0", "Application": "Test"}


@app.get("/health")
def health():
    return 200


@app.get("/inference")
def model_inference(input):
    inf = inference(model, input)

    return {"inference": inf}
