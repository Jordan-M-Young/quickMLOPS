from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle


def write_model(model, file):
    with open(file, "wb") as f:
        pickle.dump(model, f)


def main():
    # Dummy Constants Please configure to your needs.
    DATA_FILE = "../data/data.csv"
    MODEL_OUTPATH = "../models"
    MODEL_FILE = "clf1.pkl"
    TARGET_COLUMN = "target_column"
    TEST_SIZE = 0.2
    VERBOSE = True
    SAVE_MODEL = True

    # load data
    df = pd.read_csv(DATA_FILE)
    targets = df[TARGET_COLUMN]
    features = df.drop(columns=[TARGET_COLUMN])

    # train test split.
    x_train, x_test, y_train, y_test = train_test_split(
        features, targets, test_size=TEST_SIZE
    )

    # Model instantiated with default args.
    model = XGBClassifier()

    # Model fit.
    model.fit(x_train, y_train)

    # Model Score
    if VERBOSE:
        print("Model Accuracy", model.score)

    # Model Eval
    _y_pred = model.predict(x_test)

    # Further Evaluation Code..

    # Save Model
    if SAVE_MODEL:
        MODEL_PATH = f"{MODEL_OUTPATH}/{MODEL_FILE}"
        write_model(model, MODEL_PATH)


if __name__ == "__main__":
    main()