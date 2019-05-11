import numpy as np
import matplotlib.pyplot as plt

# 1d plotting
# x = np.linspace(0, 3, 20)
# y = np.linspace(0, 9, 20)
# plt.plot(x, y)
# plt.plot(x, y, 'o')
# plt.show()

'''Use boolean masks'''
# a = np.random.randint(0, 21, 15)
# print(a)

# mask = (a % 3 == 0)
# print(mask)
# extractFromA = a[mask]
# print(extractFromA)

'''# indexing with array of integers'''
# indexing can be done with an array of integers where same index is
# repeated several times
# a = np.arange(0, 100, 10)
# b = a[[2, 3, 2, 4, 2]]
# print(a, b)
# # new values can be assigned with this kind of indexing also
# a[[9, 7]] = -100

'''Numerical operations on arrays'''
# a = np.array([1, 2, 3, 4])
# print(a+1)
# print(2**a)

# b = np.ones(4) + 1
# print(a-b)
# print(a+b)

# # warning array multiplication is elementwise not matrix multiplication
# c = np.ones((3, 3))
# print(c * c)

# # matrix mult is done using dot
# print(c.dot(c))

# # transcendental functions
# a = np.arange(5)
# print(np.sin(a))
# print(np.cos(a))
# print(np.tan(a))
# print(np.log(a))
# print(np.exp(a))

# # transpose
# # doesnt work for rank 1 matrix
# print(a, a.T)
# b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print("\n", b, "\n", b.T)


'''reductions'''
# x = np.array([1, 2, 3, 4])
# print(np.sum(x), x.sum())

# # axes: axis = 0 , first dimension, columns
# # axes: axis = 1 , second dimension, rows and so on
# x = np.array([[1, 1], [2, 2]])
# print(x.sum(axis=0))
# print(x.sum(axis=1))
# print(x[0, :].sum(), x[1, :].sum())

# # same idea for higher dims
# x = np.random.rand(2, 2, 2)
# print(x.sum(axis=2))
# print(x[0, 1, :].sum())

# other reductions
x = np.array([1, 3, 2])
# min value, max value, index of min value, index of max value
print(x.min(), x.max(), x.argmin(), x.argmax())

# logical operations
# all in the array should be true, only then will print true
print(np.all([True, True, False]))
# any one can be true, no need for all to be true to get it to print true
print(np.any([True, True, False]))

# statistics
x = np.array([1, 2, 3, 4])
y = np.array([[1, 2, 3], [5, 6, 1]])
print(x.mean(), np.median(x), np.median(y, axis=1), x.std())
