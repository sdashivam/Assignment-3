#!/usr/bin/env python
# coding: utf-8

# Write a function so that the columns of the output matrix are powers of the input
# vector.
# The order of the powers is determined by the increasing boolean argument. Specifically, when
# increasing is False, the i-th output column is the input vector raised element-wise to the power
# of N - i - 1.
# 
# HINT: Such a matrix with a geometric progression in each row is named for Alexandre-
# Theophile Vandermonde.

# In[1]:


import numpy as np

def gen_vander_matrix(ipvector, n, increasing=False):
    
    if not increasing:
        op_matx = np.array([x**(n-1-i) for x in ipvector for i in range(n)]).reshape(ipvector.size,n)
    elif increasing:
        op_matx = np.array([x**i for x in ipvector for i in range(n)]).reshape(ipvector.size,n)
    
    return op_matx

print("------------OUTPUT-------------\n")

inputvector = np.array([1,2,3,4,5])
no_col_opmat = 3
op_matx_dec_order = gen_vander_matrix(inputvector,no_col_opmat,False)
op_matx_inc_order = gen_vander_matrix(inputvector,no_col_opmat,True)

print("The input array is:",inputvector,"\n")
print("Number of columns in output matrix should be:",no_col_opmat,"\n")
print("Vander matrix of the input array in decreasing order of powers:\n\n",op_matx_dec_order,"\n")
print("Vander matrix of the input array in increasing order of powers:\n\n",op_matx_inc_order,"\n")

inputvector = np.array([1,2,4,6,8,10])
no_col_opmat = 5
op_matx_dec_order = gen_vander_matrix(inputvector,no_col_opmat,False)
op_matx_inc_order = gen_vander_matrix(inputvector,no_col_opmat,True)

print("---------------------------------------------------------------\n")
print("The input array is:",inputvector,"\n")
print("Number of columns in output matrix should be:",no_col_opmat,"\n")
print("Vander matrix of the input array in decreasing order of powers:\n\n",op_matx_dec_order,"\n")
print("Vander matrix of the input array in increasing order of powers:\n\n",op_matx_inc_order,"\n")


# Given a sequence of n values x1, x2, ..., xn and a window size k>0, the k-th moving average of
# the given sequence is defined as follows:
# The moving average sequence has n-k+1 elements as shown below.

# In[2]:


def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
a = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
print(moving_average(a, n=3))


# In[ ]:




