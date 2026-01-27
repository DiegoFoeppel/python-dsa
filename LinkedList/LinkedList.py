class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next 

        return result

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
        self.length += 1
    
    def insert(self, value, index):
        new_node = Node(value)
        
        temp_node = self.head

        for i in range(index - 1):
            print(i)
            temp_node = temp_node.next

        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length += 1 

    def traversal(self):

        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next 

    def search(self, target):
        #  verify  if value is in linked list
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return index
            current_node = current_node.next
            index += 1
        return -1
    
    def get(self, index):
        #  return value at specified index
        current_node = self.head
        
        for i in range(index):
            if i == index:
                return current_node
            current_node = current_node.next
        
        return None

    def set(self, index, value):

        node = self.get(index)
        if (node):
            node.value = value
            return True
    
        return False 
        
    def pop_first(self):
        popped_node = self.head 
        self.head = self.head.next
        popped_node.next = None
        self.length -= 1
    
    def pop(self):

        popped_node = self.tail
        current_node = self.head

        while current_node.next is not self.tail:
            current_node = current_node.next
        
        self.tail = current_node
        current_node.next = None
        self.length -= 1

        return popped_node        

        # current_node = self.head
        # for i in range(self.length):
        #     if i == self.length - 2:
        #         print(current_node.value)
        #         self.tail = current_node
        #         current_node.next = None
        #     else:
        #         current_node = current_node.next

    def remove(self, index):
        prev_node = self.get(index - 1)
        popped_node = prev_node.next 
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        # while current.next:
        #     print(current, current.next.value, current.next.next)

        #     if current.next.value == target:
        #         if current.next == self.tail:
        #             self.tail = current
        #             current.next = None 
        #         else:
        #             current.next = current.next.next 
        #         self.length -= 1
            
        #     current = current.next 
        return self.head
    
    def deleteAllNodes(self):
        self.head = None
        self.tail = None
        self.length = 0
    
myLL = LinkedList()
myLL.append(1)
myLL.append(2)
myLL.append(6)
myLL.append(3)
myLL.append(4)
myLL.append(5)
# myLL.append(6)
print(myLL)

myLL.remove(6)
print(myLL)

# myLL.insert(50, 4)
# print(myLL)