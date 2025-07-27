import numpy as np

# arr =np.array([1, 2, 3, 4, 5])

# # print(arr.size)

# # Create a 3×3 matrix filled with zeros
# arr1=np.array([[2,3,4],
#               [5,6,7],
#               [8,9,0]])

# # print(arr1[])

# ar1=np.zeros((2,3))

# # print(ar1)

# # arr2=np.random.randint(0,1,(3,3))
# # print(arr2)

# arr3=np.identity(5)
# # print(arr3)

# arr4=np.array([10,20,30,40,50])
# # print(arr4[0:3])

# # A = np.array([[1, 2, 3],  
# #               [4, 5, 6],  
# #               [7, 8, 9]])

# # print(A[1:2,1:])

# # print(np.where(A % 2 == 0 ,-1, A ))

# arr = np.array([1, 2, 3, 4])
# # print(np.std(A,axis=0))

A = np.array([[2, 1],  
              [3, 4]])

B = np.array([5, 6])
# # print(np.dot(A,B))
# # print(np.matmul(A,B))
# det=np.linalg.det(A)
# # print(det)

# inverse=np.linalg.inv(A)
# # print(inverse)

# eval,evec=np.linalg.eig(A)

# # print(eval,evec)

ans=np.linalg.solve(A,B)
# print(ans)

# arr = np.fromfunction(lambda i, j: (i * 5 + j) ** 2, shape=(5, 5), dtype=int)
# print(arr)

# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

arr=np.ones((5,5))

for i in range(5):
    for j in range(5):
        arr[i,j]=(i*5+j) ** 2
        
        
# print(arr)

M = np.array([1, 20, 3,-np.inf,np.inf])

# print(np.where(M > 10 ,0,M)) 

# M = np.array([[1, 2, 3],  
#               [4, 5, 6],  
            #   [7, 8, 9]])
# for i in range(3):
#     for j in range(3):
#         arr[i,j]



# row_sums = np.sum(M, axis=1)
# print(row_sums)
#1D TO 2D RESHAPE 2D TO 1D
# flatten()  COPY
# Ravel() VIEW

# isnan() isinf()
print(np.nan_to_num(M,posinf=999,neginf=-999))
#is inf 
# python -m notebook