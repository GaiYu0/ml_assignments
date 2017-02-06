import numpy as np

def dot(left, right):
  return sum(l * r for l, r in zip(left, right))

def words(data, X):
  occurrence = {}
  for entry in data:
    word_list = entry[1:].split(' ')
    word_set = set(word_list)
    for word in word_set:
      try: occurrence[word] += 1
      except: occurrence[word] = 1
  return sorted(key for key, value in occurrence.items() if value > X - 1)

def feature_vector(entry, vocabulary):
  entry = set(entry)
  return list(int(word in entry) for word in vocabulary)

def format_data(data, vocabulary):
  X, Y = [], []
  for entry in data:
    words = entry.split(' ')
    X.append(feature_vector(words[1:], vocabulary))
    Y.append(1 if words[0] == '1' else -1)
  return np.array(X), np.array(Y)

def format_dataset(X):
  training_data = list(open('data/train.txt', 'r'))
  vocabulary = words(training_data, X)
  training_X, training_Y = format_data(training_data, vocabulary)
  validation_X, validation_Y = format_data(list(open('data/validation.txt', 'r')), vocabulary)
  test_X, test_Y = format_data(list(open('data/spam_test.txt', 'r')), vocabulary)
  return training_X, training_Y, validation_X, validation_Y, test_X, test_Y, vocabulary

if __name__ is '__main__':
  format_dataset(1200)
