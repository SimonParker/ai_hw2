#simon parker
import random



step = 0.1

def func(x, y):
  return 5*pow(x ,2) + 40*x + pow(y, 2) - 12*y + 127


def GD(eta, f):
  pass

def run_tests(eta, f, iters):
  x = x_init = random.randint(-10, 10)
  y = y_init = random.randint(-10, 10)
  for i in range(iters):
   #x = gradient descent on x
   #y = gradient descent on y
   pass
  print(f" Gradient descent with step size {eta}: starting point ({x_init}, {y_init}), final min ({x}, {y})")
    


max_iters = 500
for i in range(3):
  run_tests(step, func, max_iters)
  step *= 0.1
