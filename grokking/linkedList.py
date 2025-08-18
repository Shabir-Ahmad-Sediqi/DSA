# Double LinkedList


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None # Initialize the next and previous address
        self.prev = None # of nodes
    
class LinkedList:

    def __init__(self):
        self.head = None # Initialize head and tail of a node
        self.tail = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def add_at_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    # function to check the length of the LinkedList
    def lengthOfList(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def add_at_arbitrary_position(self, data, position):
        new_node = Node(data)
        if position < 0 : return
        if position == 0:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        if position > self.lengthOfList(): return "Index exeeded"

        # traverse until the desired position
        temp = self.head
        count= 0
        while temp and count < position - 1:
            temp = temp.next
            count += 1
        next_node = temp.next
        temp.next = new_node
        new_node.prev = temp
        new_node.next = next_node

    def delete_from_end(self):
        if self.tail is None:  # empty list
            print("List is empty")
            return
        
        if self.tail.prev is None:  # only 1 node
            self.head = None
            self.tail = None
        else:
            second_last_node = self.tail.prev
            second_last_node.next = None
            self.tail = second_last_node

    def delete_from_arbitrary_position(self, position):
        if self.tail is None:  # empty list
            print("List is empty")
            return
        if position == 0:
            next_node = self.head.next
            next_node.prev = None
            self.head = next_node
        else:
            temp = self.head
            count = 0
            while temp and count < position:
                count += 1
                temp = temp.next
            prev_node = temp.prev
            next_node = temp.next
            prev_node.next = next_node
            next_node.prev = prev_node

    def upto(self, n): # Add Nodes for a specific range of numbers
        for i in range(n):
            self.add(i)

    def display(self):
        if self.head is None:
            return "LinkedList is empty"
        else:
            temp = self.head
            while temp:
                if temp.data is not None:
                    print(F"{temp.data} --> ", end="")
                else:
                    print("--> ", end="")
                temp = temp.next

DLL = LinkedList()
DLL.upto(10)
DLL.append(11)
DLL.add_at_first(-1)
DLL.append(12)
DLL.add_at_arbitrary_position(50, 5)
DLL.add_at_arbitrary_position(100, 10)
DLL.delete_from_end()
DLL.delete_from_arbitrary_position(6)
DLL.delete_from_arbitrary_position(0)
DLL.delete_from_arbitrary_position(0)
DLL.display()