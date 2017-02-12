# divide data into training data and validation data
DATA = 'data/spam_train.txt'
TRAINING = 'data/train.txt'
VALIDATION = 'data/validation.txt'
N_VALIDATION_SAMPLES = 1000
data = tuple(open(DATA, 'r'))
bound = len(data) - N_VALIDATION_SAMPLES
open(TRAINING, 'w').write(''.join(data[:bound]))
open(VALIDATION, 'w').write(''.join(data[bound:]))
