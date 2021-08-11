class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,">>>",end="")
                temp=temp.next
    def add_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head =new_node
    def add_ending(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp=self.head
            while temp is not None:
                temp=temp.next
                temp.next=new_node
    def get_count(self,node):
        if (node==None):
            return 0
        else:
            return 1 + self.get_count(node.next)
    
if __name__=='__main__':

     ssl=linkedlist()
ssl.add_begin(10)
ssl.add_begin(30)
ssl.add_begin(56)
ssl.add_begin(38)
ssl.add_begin(40)
print("list count",ssl.get_count())




ssl.display()