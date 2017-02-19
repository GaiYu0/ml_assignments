import numpy as np
import pickle
import sys

def normalize(data):
  mean = np.mean(data, axis=0)
  std = np.std(data, axis=0)
  data = (data - mean) / std
  return data, mean, std

if __name__ is '__main__':
  INPUT, OUTPUT = sys.argv[1], sys.argv[2]
  strings = tuple(open(INPUT, 'r'))
  data, labels = [], []
  for string in strings:
    converted = tuple(map(float, string.replace('\n', '').split(',')))
    data.append(converted[:-1])
    labels.append(converted[-1:])

  X = np.array(data)
  normalized_X, X_mean, X_std = normalize(X)
  Y = np.array(labels)
  normalized_Y, Y_mean, Y_std = normalize(Y)

  pickle.dump((normalized_X, normalized_Y), open(OUTPUT, 'wb'))
  pickle.dump((X_mean, X_std, Y_mean, Y_std), open('statistics', 'wb'))
