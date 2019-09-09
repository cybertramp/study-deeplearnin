#!/usr/bin/python3.7
# ===================== #
#
# Written: 19.09.09
#
# Name: 
#
# ===================== #

import numpy as np

x = np.array([[1,2,3],[4,5,6]])
print(x)
print()
print("# x * x")
print(x*x)

D = np.array([[1,2]])
B = np.array([[5],[6],[7]])
print()
print(D)
print()
print(B)
print()
print("+) D.shape")
print(D.shape)

print("+) B.shape")
print(B.shape)

print()

A = np.matmul(B,D)
print(A)
print()
print("+) A.shape")
print(A.shape)

print("+) np.dot(B,D)")
print(np.dot(B,D))
