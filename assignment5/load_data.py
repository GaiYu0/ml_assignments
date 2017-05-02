def load_dataset(path='data'):
  encoded_labels = {'Iris-setosa' : 0, 'Iris-versicolor' : 1, 'Iris-virginica' : 2}
  data, labels = [], []
  for line in open('data', 'r'):
    fields = line[:-1].split(',')
    data.append(map(float, fields[:-1]))
    labels.append(encoded_labels[fields[-1]])

  import numpy as np
  return np.array(data), np.array(labels)
