import os

import torch
from torch import nn

torch.manual_seed(7)
model = nn.Sequential(nn.Linear(3, 4), nn.ReLU(), nn.Linear(4, 2))
x = torch.ones(1, 3)

model.eval()
with torch.no_grad():
    before = model(x)

torch.save(model.state_dict(), "weights.pth")

loaded = nn.Sequential(nn.Linear(3, 4), nn.ReLU(), nn.Linear(4, 2))
loaded.load_state_dict(torch.load("weights.pth", weights_only=True))
loaded.eval()

with torch.no_grad():
    after = loaded(x)

print("before:", before.tolist())
print("after: ", after.tolist())
print("same:", torch.allclose(before, after))
print("file size:", os.path.getsize("weights.pth"), "bytes")