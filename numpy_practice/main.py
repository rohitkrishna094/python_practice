import numpy as np

# a = np.array([1, 2, 3])
# print(type(a))
# print(a.shape)
# print(a[0], a[1], a[2])
# a[0] = 5
# print(a)

# # b has rank of 2; rank is basically the number of dimensions
# b = np.array([[1, 2, 3], [4, 5, 6]])
# while shape is array of tuples giving size of array along each dimension
# print(b.shape)
# print(b[0, 0], b[0, 1], b[1, 0])

# numpy also has many functions to create arrays
# create zeroes of this dims
# a = np.zeros((2, 4, 5, 3))
# print(a)

# create ones of this dim
# b = np.ones((1, 2))
# print(b)

# create a constant array of this dims
# c = np.full((2, 4, 5, 3), 7)  # 7 will be printed everywhere
# print(c)

# create an identity matrix of this size
# d = np.eye(4, 4)
# print(d)

# create an array filled with random values between [0.0,1.0)
# e = np.random.random((4, 2, 5))
# print(e)

'''Array Indexing'''
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]])

# Use slicing to pull out subarray. first 2 rows and columns
# also note that the slice is just a view into array. if you change the slice,
# the original array will also change, so tread with caution
# b = a[:2, 1:3]
# # we changed b, but a will also change
# b[0][0] = 20
# print(b)
# print(a)

# two other ways to slice
# print(a[0, 1])
# print(a[0][1])

'''# Careful :Mixing integer and slice indexing like we did above'''
# Integer slicing common in python
# we get different rank compared to a, it will be (4,)
# row_r1 = a[1, :]
# # matlab styled slicing, common in numpy and stuff
# # we get similar rank as a. it will be (1,4)
# row_r2 = a[1:2, :]
# print(row_r1, row_r1.shape)
# print(row_r2, row_r2.shape)

# Same applies to columns
# col_r1 = a[:, 1]
# col_r2 = a[:, 1:2]
# print(col_r1, col_r1.shape)  # (3,)
# print(col_r2, col_r2.shape)  # (3,1)

'''# Mutate one element from each row of a matrix'''
# create an array of indices
# b = np.array([0, 2, 0, 1])

# # select on element from each row of a using indices in b
# print(a[np.arange(4), b])


# # mutate one element from each row of a using indices in b
# a[np.arange(4), b] += 10
# print(a)

# print(np.arange(4))

'''boolean array indexing'''
# a = np.array([[1, 2], [3, 4], [5, 6]])

# # find elems of a that are bigger than 2
# # returns a numpy array of booleans of same shape as a, where each slot
# # of bool_idx tells whether that element of a is > 2
# bool_idx = (a > 2)

# print(bool_idx)

# # we can use boolean array indexing to construct a rank 1 array
# # consisting of elemsn of a corresponding to the True values of bool_idx
# print(a[bool_idx])
# # shorter way to do that
# print(a[a > 2])

'''Datatypes'''
# print(a.dtype)
# a = np.array([1, 2], dtype=np.int64)
# print(a.dtype)

# a = np.array([1.0, 2.0])
# print(a.dtype)

'''Array math'''
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

# # both notations produce same output
# print(x+y)
# print(np.add(x, y))

# # both notations produce same output
# print(x-y)
# print(np.subtract(x, y))

# # both notations produce same output
# * is elementwise multiplication unlike matlab
# print(x*y)
# print(np.multiply(x, y))

# # both notations produce same output
# print(x/y)
# print(np.divide(x, y))

# element wise square root; produces the array
# print(np.sqrt(x))

'''Products'''
# x = np.array([[1, 2], [3, 4]])
# y = np.array([[5, 6], [7, 8]])
# v = np.array([9, 10])
# w = np.array([11, 12])

# # Inner product of vectors, both produce same product
# print(v.dot(w))
# print(np.dot(v, w))

# # matrix /vector product; both produce the rank 1 array [29,67]
# print(x.dot(v))
# print(np.dot(x, v))

# # matrix/matrix product; both produce the rank 2 array
# print(x.dot(y))
# print(np.dot(x, y))

'''Functions on Arrays'''
# x = np.array([[1, 2], [3, 4]])
# print(np.sum(x))
# # sum of each column
# print(np.sum(x, axis=0))
# # sum of each row
# print(np.sum(x, axis=1))

# # transpose
# print(x.T)

'''Broadcasting'''
# its a powerful mechanism that allows numpy to work with arrays of different shapes
# when performing arithmetic operations

# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# v = np.array([1, 0, 1])
# y = np.empty_like(x)   # Create an empty matrix with the same shape as x
# print(y)

# # add vector v to each row of martix x
# # this uses a literal loop
# for i in range(4):
#     y[i, :] = x[i, :] + v

# print(y)

# however the above approach wont work for big arrays since conventional for loop is slow

# lets use tile to do the above thing
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1))  # stack 4 copies of v on top of each other
print(vv)
y = x + vv
print(y)

# now lets use broadcasting to do this
# it allows us to perform this computation without actually creating multiple copies of v
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])

'''
the below line works even though x has (4,3) shape and v has (3,) shape.
this works as if v actually had shape (4,3) where each row was a copy of v
and the sum was performed elementwise
'''
y = x + v  # Add v to each row of x using broadcasting
print(y)
