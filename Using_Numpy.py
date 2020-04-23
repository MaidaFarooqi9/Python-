import numpy as np

arr=np.array([1,4,6,5])

print(arr)

print(arr[3]) #indexing
print(arr[0:4])#slicing start and end point
print(arr[1:4:3]) #start end step

#2-Dimension
A=np.array([['a','b','c'] ,['d','e','f']])
print(A)
for x in A: #iterating
    for y in x:
        print(y)

B=np.array([[1,2,4],[5,9,8]])
for z in np.nditer(B):
     print(z)
print(B.shape) #shape ,no of elements in eac dim

Reshape=arr.reshape(2,2)
print(Reshape)
print(A.reshape(6,1,1))

print(np.concatenate((A,B)))

print(np.concatenate((A,B),axis=1 ))