class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class double_linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n = n.nref

    def printlist_reverse(self):
        print()
        if self.head is None:
            print("linked list is empty")
        else:
            n =self.head
            while n.nref is not None:
                n =n.nref
            while n is not None:
                print(n.data)
                n =n.pref

    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("linkedlist is not empty!")

    def insert_begin(self,data):
        new_node = Node(data)
        if self.head is None:
           self.head =new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:
           self.head =new_node
        else:
            n =self.head
            while n.nref is not None:
                n = n.nref
                n.nref = new_node
                new_node.pref = n

    def insert_specific_position(self,pos,data):
        new_node = Node(data)
        n =self.head
        for i in range(1,pos-1):
            n.nref=n
            n.pref =n
            n.nref =n.nref
            n.nref.pref=n
            n.nref=n




linkedlist = double_linkedlist()
#linkedlist.insert_empty(40)
linkedlist.insert_begin(10)
#linkedlist.insert_begin(20)
#linkedlist.insert_begin(30)
#linkedlist.insert_begin(40)
#linkedlist.insert_begin(50)
#linkedlist.insert_end(60)
#linkedlist.insert_specific_position(3,25)
linkedlist.printlist()





            
                