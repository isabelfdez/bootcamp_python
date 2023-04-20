from vector import Vector
from vector import get_value
from vector import calc_shape



v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
v3 = Vector([[1.1, 1.2, 1.3, 1.4]])

#print(v1.dot(v3))
#print(v1.T().values)
#print(v2.T().values)
#print(v3.T().values)
#print(get_value(v1, 3))
#print(get_value(v3, 1))
#print(get_value(v3, 3))
#v4 = v1 + v2
#print(v4.values)
#
v5 = v3 + v3
print(v5.values)
print(v5.T().values)
#print(calc_shape(v1))
#print("hi")
#print(calc_shape(v2))
#print(calc_shape(v3))
