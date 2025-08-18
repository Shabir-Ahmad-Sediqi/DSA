
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class LinkedList:

    def __init__(self):
        self.head = None
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
    
    def upto(self, n):
        for i in range(n):
            self.add(i)

    def display(self):
        if self.head is None:
            return "LinkedList is empty"
        else:
            temp = self.head
            while temp:
                print(F"{temp.data} --> ", end="")
                temp = temp.next

DLL = LinkedList()
DLL.upto(10)
DLL.append(11)
DLL.add_at_first(-1)
DLL.append(12)
print(DLL.display())