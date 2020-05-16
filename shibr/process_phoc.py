import numpy as np

word = 'october'
arr = np.load('predicted_phocs.npy')
sliced = np.concatenate((arr[0][:36], arr[0][86:122], arr[0][172:]))
normalized = np.around(sliced, 0)
truth = np.load(word + '.npy')[0]
masked = np.ma.masked_where(truth==0, normalized)
print("Result for " + word)
masked.sum()
print("Accuracy")
masked.sum() / truth.sum()

def phoc_to_strings(arr):
    s = '0123456789abcdefghijklmnopqrstuvwxyz'
    for i in range(len(arr)):
        if arr[i] == 1:
            print(str(i) + ": " + s[i % 36])

# svens: 0
# swen: 0
# anders: 1 (25)
# walfrid: 3 (28)
# maria: 2 (22)
# anna: 1 (15)

# with otsu
# anders: 0
# swen: 0
# maria: 1
# walfrid: 0
# anna: 0


for i in range(len(arr[0])):
    if arr[0][i] > 0.99999:
        print(s5[i])