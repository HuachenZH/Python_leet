"""A prototype script to test the core functionalities"""
from numpy.linalg import inv
import numpy as np



mat1 = np.array([[94,22], [34,67]])
#mat2 = np.transpose(np.array([80, 40]))
mat2 = np.array([80, 40])
#res = np.matmul(mat1, mat2)
res = mat1 @ mat2
del mat1
del mat2
del res



A = np.array([[94,22], [34,67]])
G = np.array([8400, 5400])
x = inv(A) @ G
del A
del G
del x


def give_three():
    return 1, 2, 3

a, b, c = give_three()
breakpoint()
