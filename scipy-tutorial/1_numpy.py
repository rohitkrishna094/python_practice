import numpy as np


# 1d array
# a = np.array([1, 2, 3, 4])
# print(a.ndim, a.shape)

# # 2d, 3d
# b = np.array([[0, 1, 2], [3, 4, 5]])
# print(b.ndim, b.shape, b.dtype)

# c = np.array([
#     [[0, 1, 2], [3, 4, 5]],
#     [[10, 11, 12], [13, 14, 15]],
# ])

# print(c.ndim, c.shape)

'''# arange & linspace'''
# a = np.arange(10)
# print(a)
# # start, end, step
# a = np.arange((1, 9, 2))
# print(a)

# or by number of points
# 6 points between [0,1]
# a = np.linspace(0, 1, 6)
# # dont include endpoint
# a = np.linspace(0, 1, 5, endpoint=false)

'''ones, zeroes, diag,eye'''
# a = np.ones((3,3))
# b = np.zeros((2,2))
# c = np.eye(3)
# # creates a 4x4 matrix with diagonal elements as 1,2,3,4
# d = np.diag(np.array([1,2,3,4]))

'''# random numbers'''
# uniform in [0,1]
# a = np.random.rand(4)
# # gaussian
# b = np.random.randn(4)
# # setting the random seed
# np.random.seed(1234)

'''data types'''
# the default datatype is floating point
# a = np.ones((3, 3))
# print(a.dtype)

# there are other types like
# complex, bool, strings, int32,int64,uint32,uint64
# d = np.array([1+2j, 3+4j, 5+6*1j])
# print(d, d.dtype)

# e = np.array([True, False, False, True])
# print(e, e.dtype)

# f = np.array(['Bonjour', 'Hello', 'Hello'])
# print(f, f.dtype)
