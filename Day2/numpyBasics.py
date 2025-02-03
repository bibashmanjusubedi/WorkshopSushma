import numpy as np

arr = np.array([1, 2, 3, 4, 5,6,7])

print(arr)

print(type(arr))

print(arr[0]) # indexing at zero index
print(arr[1]) # one index
print(arr[1:5]) #slicing from 1st to 5th index
print(arr[4:]) # slicing from 4th to last index
print(arr[-3:-1]) # negative slcuding -1 stands for last item in array, -2 2nd last and so on
print(arr[1:5:2]) # step 2 slicing
print(arr[::2])# 1st to last step 2 slicing

