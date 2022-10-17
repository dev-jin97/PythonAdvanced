# List Allocation

x = [1, 2, 3, 4, 5]
y = x
y[2] = 0

# y는 x의 위치를 같이 가리키는 것이나 마찬가지다. 그렇기에 y의 값을 바꾸면 x의 값을 바꾸는 것과 같은 맥락이 된다.
print(x)
print(y)

# 같은 주소값을 가지고 있다.
print(id(x))
print(id(y))

# List Copy

a = [5, 6, 7, 8, 9]
b = a.copy()
b[2] = 0
print(a)
print(b)

print(id(a))
print(id(b))

# deepcopy
import copy
c = [[1, 2], [3, 4, 5]]
d = copy.deepcopy(c)
d[0][0] = 0
print(c)
print(d)