import torch
from torch.utils.data import DataLoader, TensorDataset

features = torch.arange(20, dtype=torch.float32).reshape(10, 2)
labels = torch.arange(10)
dataset = TensorDataset(features, labels)
loader = DataLoader(dataset, batch_size=4, shuffle=False)

for number, (x, y) in enumerate(loader, start=1):
    print(f"batch {number}: shape={tuple(x.shape)}, labels={y.tolist()}")