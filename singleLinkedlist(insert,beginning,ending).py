class  Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singlelinkedlist:
    def __init__(self):
        self.head =None

    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb

    def insert_ending(self,data):
        ie=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ie

    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
            np.data=data
            np.next=temp.next
            temp.next=np


    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"--->",end=" ")
                temp=temp.next

L =singlelinkedlist()
n1 =Node(10)
L.head=n1
n2 =Node(20)
L.head.next=n2
L.insert_beginning(5)
L.insert_ending(25)
L.insert_position(2,23)

L.display()


