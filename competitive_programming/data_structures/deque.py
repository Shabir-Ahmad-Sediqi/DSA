
# Here we will see how we can achieve the same thing in python

from collections import deque

dq = deque([1,2,3])
dq.append(4)
dq.appendleft(0)
dq.pop()
dq.popleft()

print(dq)

print(dq)