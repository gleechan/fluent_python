import numpy
a = numpy.arange(12)
a.shape = 3, 4
# print(a[2, 0])
print(a.transpose())