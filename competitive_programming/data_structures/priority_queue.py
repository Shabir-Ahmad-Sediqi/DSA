import heapq

priority_queue = []

heapq.heappush(priority_queue, (3, "Low Priority"))
heapq.heappush(priority_queue, (2, "medium Priority"))
heapq.heappush(priority_queue, (1, "High Priority"))

while priority_queue:
    num, text = heapq.heappop(priority_queue)
    print(f"{num} {text}")



