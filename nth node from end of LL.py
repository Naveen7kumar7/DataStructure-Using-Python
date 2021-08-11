class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def print(self):
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,">>>>",end =" ")
                temp = temp.next
    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def find_nth_node(self,n):
        p = self.head
        q = self.head
        count = 0
        while (count <= n-1):
            q = q.next
            count = count + 1
        if not q:
            print(str(n)+ "is greater than the no.of nodes in list")
            return
        while p and q:
            p = p.next
            q = q.next
        return p.data


LL =linkedlist()
LL.add_begin(10)
LL.add_begin(20)
LL.add_begin(30)
LL.add_begin(40)
LL.add_begin(50)
LL.add_begin(60)

LL.print(find_nth_node(4))