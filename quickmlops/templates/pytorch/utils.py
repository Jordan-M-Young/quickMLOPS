from torch.utils.data import Dataset


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


def inference():
    pass


def load_model():
    pass
