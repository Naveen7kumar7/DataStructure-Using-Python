class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DLL:
    def __init__(self):
        self.head =None

    def printlist(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,">>>>>",end="")
                temp = temp.next

    def deletion_at_beginning(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = None

    def deletion_at_ending(self):
        temp = self.head.next
        before = self.head
        while temp.next is not None:
            temp = temp.next
            before = before.next
        before.next = None
        temp.prev = None

    def deletion_specific_position(self,pos):
        temp = self.head.next
        before = self.head
        for i in range(1,pos-1):
            temp = temp.next
            before = before.next
        before.next = temp.next
        temp.next.prev = before
        
        temp.prev = None
        temp.next = None
        

linkedlist = DLL()
n1 = Node(10)
linkedlist.head = n1

n2 = Node(20)
n1.next = n2
n2.prev = n1

n3 = Node(30)
n2.next = n3
n3.prev = n2

n4 = Node(40)
n3.next = n4
n4.prev = n3

n5 = Node(50)
n4.next = n5
n5.prev = n4

#linkedlist.deletion_at_beginning()
#linkedlist.deletion_at_ending()
#linkedlist.deletion_specific_position(3)

linkedlist.printlist()
