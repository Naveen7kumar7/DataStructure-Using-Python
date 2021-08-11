class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class doublelinkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,">>>>>",end="")
                temp = temp.next

    def insert_begin(self,data):
        n =Node(data)
        temp = self.head
        temp.prev = n
        n.next = temp
        self.head = n

    def insert_end(self,data):
        n = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = n
        n.prev = temp

    def insert_position(self,pos,data):
        n = Node(data)
        temp = self.head
        for i in range(1,pos-1):
            temp =temp.next
        n.prev = temp
        n.next = temp.next
        temp.next.prev = n
        temp.next = n

    def length_of_the_linkedlist(self):
        temp = self.head
        count = 0
        while temp is not None:
            count+=1
            temp = temp.next
            return count

l = doublelinkedlist()
n1 =Node(10)
l.head =n1
n2 = Node(20)
n2.prev =n1
n1.next = n2
n3 = Node(30)
n3.prev = n2
n2.next = n3
n4 = Node(40)
n4.prev = n3
n3.next = n4
#l.insert_begin(5)
#l.insert_end(45)
#l.insert_position(2,35)
l.printlist()
