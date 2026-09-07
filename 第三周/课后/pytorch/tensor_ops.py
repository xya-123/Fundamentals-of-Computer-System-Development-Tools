import torch

a = torch.arange(1, 7).reshape(2, 3)
b = torch.tensor([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])

print("a:")
print(a)
print("slice:")
print(a[:, 1:])
print("matmul:")
print(a.float() @ b)
print("cat shape:", torch.cat([a, a], dim=0).shape)