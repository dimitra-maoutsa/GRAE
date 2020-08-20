"""Base class for datasets."""
import os

import numpy as np
import torch
from torch.utils.data import Dataset
from sklearn.model_selection import train_test_split

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

FIT_DEFAULT = .8  # Default train split ratio
SEED = 42  # Default seed for splitting

BASEPATH = os.path.join(
    os.path.dirname(__file__),
    os.path.join('..', '..', 'data', 'processed')
)

if not os.path.exists(BASEPATH):
    os.makedirs(BASEPATH)


class NumpyDataset(Dataset):
    """Wrapper for x ndarray with no target."""

    def __init__(self, x, y=None):
        self.data = torch.from_numpy(x).float()

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def numpy(self, idx=None):
        if idx == None:
            return self.data.numpy()
        else:
            return self.data.numpy()[idx]


class BaseDataset(Dataset):
    """All datasetse should subclass BaseDataset."""

    def __init__(self, x, y, split, split_ratio, seed):
        if split not in ('train', 'test', 'none'):
            raise Exception('split argument should be "train", "test" or "none"')

        # Get train or test split
        x, y = self.get_split(x, y, split, split_ratio, seed)

        self.data = x.float()
        self.targets = y.float()

    def __getitem__(self, index):
        return self.data[index], self.targets[index], index

    def __len__(self):
        return len(self.data)

    def numpy(self, idx=None):
        # Convenience method to fetch dataset as ndarrays.
        if idx == None:
            return self.data.numpy(), self.targets.numpy()
        else:
            return self.data.numpy()[idx], self.targets.numpy()[idx]

    def get_split(self, x, y, split, split_ratio, seed):
        if split == 'none':
            return torch.from_numpy(x), torch.from_numpy(y)

        n = x.shape[0]
        train_idx, test_idx = train_test_split(np.arange(n),
                                               train_size=split_ratio,
                                               random_state=seed)

        if split == 'train':
            return torch.from_numpy(x[train_idx]), torch.from_numpy(y[train_idx])
        else:
            return torch.from_numpy(x[test_idx]), torch.from_numpy(y[test_idx])

