import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr)
print(np.version)
print(arr.ndim)
print(arr[3])
print(arr[2:5])
arr1=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(arr1)
print(arr1.ndim)
print(arr1[1][3])
print(arr1[1,2:5])
print(arr1[0:4,2])
print(arr1[0:4,2:6])
print(arr1.dtype)

arr2=np.array([1.1,2.2,3.3,4.4,5.5,6.6])
newarr=arr.astype("i")
print(newarr)
print(newarr.dtype)


#COPY AND VIEW 

ar=np.array([1,2,3,4,5,6,7,8,9])
x=ar.copy()
ar[0]=42
print(ar)
print(x)

ar1=np.array([1,2,3,4,5,6,7,8,9])
x=ar1.view()
ar1[0]=42
print(ar1)
print(x)

#shape of on array-no.of element in each dimension

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8,]])
print(arr.shape)

#RESHAPING THE ARRAY -1D---->2D
ar1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr1=ar1.reshape(4,-1)
print(newarr1)

#flattenig the array multi d ---->1d
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8,]])
newar=arr.reshape(-1)
print(newar)