from torch import Tensor, save
from torch.nn import Dropout, Linear, Module, ReLU, Sequential, Sigmoid
import numpy as np
from torch import DoubleTensor, tensor
from torch.nn import Module
from torch.nn.modules.loss import _Loss
from torch.optim import Optimizer
from torch.utils.data import DataLoader


class CustomModel(Module):
    """Trivial CustomModel Template."""

    def __init__(self):
        """Initialize CustomModel."""
        super(CustomModel, self).__init__()

        self.fc1 = Linear(2, 5)
        self.re1 = ReLU()
        self.d = Dropout(0.2)
        self.fc2 = Linear(5, 1)
        self.sigmoid = Sigmoid()

        self.net = Sequential(self.fc1, self.re1, self.d, self.fc2, self.sigmoid)

    def forward(self, x) -> Tensor:
        """Forward pass function."""
        output = self.net(x)
        return output


def save_model(model: Module, path: str):
    """Save Model To File."""
    save(model, path)


def train(
    data: DataLoader,
    model: Module,
    loss_func: _Loss,
    optimizer: Optimizer,
) -> float:
    """Training loop."""
    model.train()
    batch_loss = 0.0
    for _, batch in enumerate(data):
        left, right, labels = batch
        labels = np.array(labels).transpose()
        labels = tensor(labels)
        output = model(left, right)
        output = output.type(DoubleTensor)
        loss = loss_func(output, labels)
        loss_val = loss.detach().item()
        batch_loss += loss_val
        loss.backward()

        optimizer.step()

    return batch_loss


def evaluate(data: DataLoader, model: Module, loss_func: _Loss) -> float:
    """Evaluation Loop."""
    model.eval()
    batch_loss = 0.0
    for _, batch in enumerate(data):
        left, right, labels = batch
        labels = np.array(labels).transpose()
        labels = tensor(labels)
        output = model(left, right)

        loss = loss_func(output, labels)
        loss_val = loss.detach().item()
        batch_loss += loss_val

    return batch_loss
