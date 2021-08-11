class Node:
    def __init__(self,data):
        self.data =data
        self.next= None
class linkedlist:
    def __init__(self):
        self.head =None

    def printlist(self):
        temp = self.head
        while(temp is not None):
            print(temp.data)
            temp = temp.next

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
            self.head = prev

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

llist = linkedlist()
llist.push(5)
llist.push(10)
llist.push(15)


print("Given linkedlist ") 
llist.printlist()
llist.reverse()
print("\n Reverse linked list is")
llist.printlist()

