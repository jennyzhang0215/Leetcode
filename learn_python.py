def n_grams(a, n):
	z = [iter(a[i:]) for i in range(n)]
	return list(zip(*z))

a = [1, 2, 3, 4, 5, 6]
print(n_grams(a, 2))
print(n_grams(a, 3))
print(n_grams(a, 4))

print("====================\n")

a = [1, 2, 3, 4, 5, 6]
print([iter(a)] * 3)
print(list(zip(*([iter(a)] * 2))))

print("====================\n")

m = {x: x ** 2 for x in range(5)}
print(m)
m = {x: 'A' + str(x) for x in range(10)}
print(m)

print("====================\n")

m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(m)
for k, v in m.items():
	print(k,":",v)
m_reverse = {v: k for k, v in m.items()}
print(m_reverse)

print("====================\n")

import collections
Point = collections.namedtuple("Point", ['x','y'])
p = Point(x = 10.0, y = 2.0)
print(p.x)
print(p.y)

print("====================\n")

import collections
Q = collections.deque()
Q.append(1)
Q.appendleft(2)
Q.extend([3, 4])
Q.extendleft([5, 6])

print(Q) #deque([6, 5, 2, 1, 3, 4])
print(Q.pop()) #4
print(Q.popleft()) #6
print(Q) #deque([5, 2, 1, 3])

Q.rotate(3)
print(Q) #deque([2, 1, 3, 5])
Q.rotate(-3)
print(Q) #deque([5, 2, 1, 3])

last_three = collections.deque(maxlen=3)
for i in range(10):
	last_three.append(i)
	print(', '.join(str(x) for x in last_three))
