
# Here we will see how we can achieve the same thing in python

from collections import deque

dq = deque([2,4])

print(dq)

dq.append(3)
dq.appendleft(0)

print(dq)

dq.pop()
dq.popleft()

print(dq)

dq.extend([2,3])
print(*dq)