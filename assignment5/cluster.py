import numpy as np

def cluster(X, centriods, p=2):
    distances = []
    for centriod in centriods:
      distances.append(minkowski(X, centriod, p))
    distance_array = np.stack(distances).T
    cluster_indices = np.argmin(distance_array, axis=1)
    return cluster_indices

def loss_function(X, cluster_indices, centriods, p=2):
  loss = 0
  for i, centriod in enumerate(centriods):
    loss += np.mean(minkowski(X[cluster_indices == i], centriod, p), axis=0)
  return loss

def minkowski(u, v, p):
  return np.sum((u - v) ** p, axis=1) ** (1.0 / p)

def search_for_centriods(X, K, p=2, tolerance=0.001):
  N, D = X.shape
  centriod_indices = np.random.choice(np.arange(N), K, replace=False)
  centriods = list(X[i].reshape((1, D)) for i in centriod_indices)

  iteration = 0
  previous_loss = 0
  to_continue = True
  while to_continue:
    iteration += 1

    cluster_indices = cluster(data, centriods, p)

    for i, centriod in enumerate(centriods):
      centriods[i] = np.mean(X[cluster_indices == i], axis=0)

    loss = loss_function(X, cluster_indices, centriods)
    if abs(previous_loss - loss) < tolerance: to_continue = False
    previous_loss = loss

    if iteration % 1 == 0:
      print 'iteration %d loss %f' % (iteration, loss)

  return centriods

if __name__ == '__main__':
  from load_data import *
  data, labels = load_dataset()

  centriods = search_for_centriods(data, 3)
  cluster_indices = cluster(data, centriods)

  from itertools import permutations
  table = []
  for p in permutations(range(3)):
    permuted_labels = np.zeros(labels.shape)
    for i, label in enumerate(labels):
      permuted_labels[i] = p[label]
    table.append(np.count_nonzero(cluster_indices - permuted_labels))

  print '%d/%d' % (min(table), len(data))
