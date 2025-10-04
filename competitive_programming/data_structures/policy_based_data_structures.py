# We have some data structures that are not part of g++ c++ compiler by default
# we can import it from another library so now i want to implement it in python
# in case you needed to have it in c++ you can convert python to c++ 

# first install sortedcontainers

from sortedcontainers import SortedList

s = SortedList()

s.add(10)
s.add(15)
s.add(20)

print(s[1]) # c++ -> find_by_order
print(s.bisect_left(10)) # c++ ->  order_of_key