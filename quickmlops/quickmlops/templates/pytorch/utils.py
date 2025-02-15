from torch.utils.data import Dataset, DataLoader
from pandas import DataFrame
from models import CustomModel
from torch import load


class CustomDataset(Dataset):
    """Custom Dataset Class."""

    def __init__(self, features, targets):
        """Initialize Custom Dataset."""
        self.features = (features,)
        self.targets = targets

    def __getitem__(self, index):
        """Get item from dataset."""
        sample = self.features.iloc[index]
        target = self.targets.iloc[index]

        return sample, target

    def __len__(self) -> int:
        """Get length of dataset."""
        return len(self.features)


def log_epoch(epoch: int, train_loss: float, test_loss: float) -> None:
    """Logs epoch loss."""
    print(f"Epoch {epoch} | Train Loss: {train_loss}  | Test Loss {test_loss} ")


def inference(model, features):
    features = DataFrame(features)
    targets = DataFrame(["test"])

    data = CustomDataset(features=features, targets=targets)
    dataloader = DataLoader(data, batch_size=1)

    model.eval()
    for _, batch in enumerate(dataloader):
        features, label = batch
        output = model(features)

        return output


def load_model(path):
    model = CustomModel()
    model.load_state_dict(load(path, weights_only=True))
    return model
