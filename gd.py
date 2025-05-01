#simon parker
import random

def func(x, y):
  return 5*pow(x ,2) + 40*x + pow(y, 2) - 12*y + 127

def dx(x):
  return 10*x + 40

def dy(y):
  return 2*y - 12

def gradient_descent(eta, f, iters):
  x = x_init = random.randint(-10, 10)
  y = y_init = random.randint(-10, 10)
  for i in range(iters):
    x -= eta * dx(x)
    y -= eta * dy(y)
  return x, y, x_init, y_init
    


max_iters = 500
for step in [0.1, 0.01, 0.001]:
  min_val = min_x = min_y = x_init = y_init = 99999
  for i in range(10): #report the best of 10 trials
    x, y, x_0, y_0 = gradient_descent(step, func, max_iters)
    if func(x, y) < min_val:
      min_val = func(x, y)
      min_x = x
      min_y = y
      x_init = x_0
      y_init = y_0
  print(f"Step size {step}, best of 10 trials: starting point ({x_init}, {y_init}), final min f({min_x:.3f}, {min_y:.3f}) = {min_val:.3f}")
