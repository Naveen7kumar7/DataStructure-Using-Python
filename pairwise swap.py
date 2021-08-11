class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp = self.head
        while(temp is not None):
            print(temp.data)
            temp = temp.next

    def pairwaise_swap(self):
        temp = self.head
        if (temp is None):
            return

        while(temp is not  None and temp.next is not None):

            if(temp.data == temp.next.data):

                temp = temp.next.next
            else:
                 temp.data,temp.next.data == temp.next.data,temp.data

                 temp =temp.next.next

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

llist =linkedlist()
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print("linked list before calling pairwise swap")
llist.printlist()
llist.pairwaise_swap()
print("\nlinked list after calling pairwise swap")
llist.printlist()