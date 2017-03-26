def _random_index(array):
  from random import choice
  return tuple(choice(range(d)) for d in array.shape)

def _relative_error(left, right):
  return abs(left - right) / (abs(left) + abs(right))

def check_gradient(f, wrt, analytical, times):
  # numeric gradient formula: df(x) / dx = (f(x + h) - f(x - h)) / (2 * h)
  h = 1e-5
  relative_errors = {}
  for t in range(times):
    index = _random_index(wrt)
    wrt[index] += h
    plus_h = f(wrt)
    wrt[index] -= 2 * h
    minus_h = f(wrt)
    wrt[index] += h
    numerical = (plus_h - minus_h) / (2 * h)
    relative_errors[index] = _relative_error(analytical[index], numerical)
  return relative_errors
