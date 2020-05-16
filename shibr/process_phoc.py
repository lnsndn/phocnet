import numpy as np

word = 'anna'
arr = np.load('predicted_phocs.npy')
sliced = np.concatenate((arr[0][:36], arr[0][86:122], arr[0][172:]))
normalized = np.around(sliced, 0)
truth = np.load(word + '.npy')[0]
masked = np.ma.masked_where(truth==0, normalized)
print("Result for " + word)
masked.sum()

# svens: 0
# swen: 0
# anders: 1 (25)
# walfrid: 3 (28)
# maria: 2 (22)
# anna: 1 (15)