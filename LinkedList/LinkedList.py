class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def traversal(self):
        
        if self.length == 0:
            return 'Empty'
        
        while self.tail.next is not None:
            head = self.head
            print(head.value)
            

myLL = LinkedList(1)
myLL.insert(2)
myLL.insert(3)

print(myLL.length)
print(myLL.head.value)
print(myLL.tail.value)

