
# from queue import PriorityQueue

# # This is the most prefered way of using priiority queue
# pq = PriorityQueue()

# pq.put((0, "highest priority"))
# pq.put((3, "very low priority "))
# pq.put((2, "low priority priority"))
# pq.put((1, "medium priority"))

# while not pq.empty():
#     priority, task = pq.get()
#     print(priority, task)


# Another way of using it 

import heapq

q = [] # The Priority 

heapq.heappush(q, (0, "HIghest Priority"))
heapq.heappush(q, (1, "Slightlly lowest Priority"))

while q:
    num, task = heapq.heappop(q)
    print(num, task)

print(q)


