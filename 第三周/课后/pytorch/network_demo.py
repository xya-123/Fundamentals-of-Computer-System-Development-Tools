import torch
from torch import nn

torch.manual_seed(7)

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(4, 8),
    nn.ReLU(),
    nn.Linear(8, 3),
)

x = torch.randn(5, 2, 2)
output = model(x)
parameters = sum(p.numel() for p in model.parameters())

print(model)
print("input shape:", tuple(x.shape))
print("output shape:", tuple(output.shape))
print("parameters:", parameters)