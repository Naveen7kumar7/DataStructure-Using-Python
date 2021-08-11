class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def sortedlist(self):
        count =[0,0,0]

        temp = self.head
        while temp != None:
            count[temp.data] += 1
            temp = temp.next
        i = 0
        temp = self.head
        while temp != None:
            if count[i] == 0:
                i += 1
            else:
                temp.data = i
                count[i] -=  1
                temp = temp.next
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def printlist(self):
        if self.head is None:
            print("item not presented in linkedlist")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next
llist = linkedlist()
llist.push(0)
llist.push(1)
llist.push(0)
llist.push(2)
llist.push(1)
llist.push(2)
llist.push(2)
llist.push(1)
llist.push(2)
print("linkedlist before sorting ")
llist.printlist()
llist.sortedlist()


print("linkedlist after sorting ")
llist.printlist()
