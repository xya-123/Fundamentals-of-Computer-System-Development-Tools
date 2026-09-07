import torch

x = torch.tensor(2.0, requires_grad=True)

y = x**3 + 2 * x
y.backward()
print("y =", y.item())
print("dy/dx =", x.grad.item())

x.grad.zero_()
z = x**2
z.backward()
print("dz/dx =", x.grad.item())