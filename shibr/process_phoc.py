import numpy as np

def hits(arr):
    for i in range(len(arr)):
        if arr[i] > 0.7:
            print(i)

arr = np.load('predicted_phocs.py')
sliced = np.concatenate((arr[0][:36], arr[0][86:122], arr[0][172:]))
hits(sliced)