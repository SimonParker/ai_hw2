#simon parker
import random

def func(x, y):
  return 5*pow(x ,2) + 40*x + pow(y, 2) - 12*y + 127

def dx(x):
  return 10*x + 40

def dy(y):
  return 2*y - 12

def run_tests(eta, f, iters):
  x = x_init = random.randint(-10, 10)
  y = y_init = random.randint(-10, 10)
  for i in range(iters):
    x -= eta * dx(x)
    y -= eta * dy(y)
  print(f" Gradient descent with step size {eta}: starting point ({x_init}, {y_init}), final min f({x:.3f}, {y:.3f}) = {func(x, y):.3f}")
    


max_iters = 500
for step in [0.1, 0.01, 0.001]:
  run_tests(step, func, max_iters)
