import torch
from torch import nn

logits = torch.tensor([
    [1.0, 2.0, 4.0],
    [3.0, 1.0, 0.0],
])
labels = torch.tensor([2, 0])

probabilities = torch.softmax(logits, dim=1)
predictions = probabilities.argmax(dim=1)
loss = nn.CrossEntropyLoss()(logits, labels)

print("probabilities:")
print(probabilities)
print("row sums:", probabilities.sum(dim=1))
print("predictions:", predictions.tolist())
print("loss:", round(loss.item(), 6))