import numpy as np
from torch.nn import BCELoss
from torch.optim import Adam
from torch.utils.data import DataLoader, random_split
import pandas as pd
from models import CustomModel, train, evaluate, save_model
from utils import CustomDataset, log_epoch


def main():
    """Main Training Function."""
    # config

    SAVE_PATH = "../models"
    MODEL_NAME = "model.pth"
    SAVE = True
    BATCH_SIZE = 32
    TEST_FRACTION = 0.2
    EPOCHS = 5
    TARGET_COLUMN = "target_column"
    # load features and targets, change according to your needs.
    df = pd.read_csv("../data/my_data.csv")

    targets = df[TARGET_COLUMN]
    features = df.drop(columns=[TARGET_COLUMN])

    # load training and test datasets.
    dataset = CustomDataset(features=features, targets=targets)
    size = len(dataset)
    train_size = int((1 - TEST_FRACTION) * size)
    test_size = size - train_size
    train_dataset, test_dataset = random_split(dataset, lengths=[train_size, test_size])

    # initialize dataloaders.
    train_dataloader = DataLoader(train_dataset, batch_size=BATCH_SIZE)
    test_dataloader = DataLoader(test_dataset, batch_size=BATCH_SIZE)

    # initialize model, optimizer, and loss function.
    model = CustomModel()
    optimizer = Adam(params=model.parameters(), lr=0.0001)
    loss_fn = BCELoss()

    # main training loop.
    for epoch in range(EPOCHS):
        train_loss = train(train_dataloader, model, loss_fn, optimizer)
        evaluate_loss = evaluate(test_dataloader, model, loss_fn)
        log_epoch(epoch, train_loss, evaluate_loss)

    if SAVE:
        SAVE_FILE = f"{SAVE_PATH}/{MODEL_NAME}"
        save_model(model, SAVE_FILE)


if __name__ == "__main__":
    main()
