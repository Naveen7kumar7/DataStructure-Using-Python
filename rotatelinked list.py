 class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,">>>",end="")
            temp = temp.next
    def add_begin(self,data):
        node1 =Node(data)
        node1.next = self.head
        self.head = node1
    def rotate(self,k):
        p = self.head
        q = self.head

        prev = None
        count = 0

        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev

        while q:
            prev = q
            q = q.next
        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None
ssl = linkedlist()
ssl.add_begin(10)
ssl.add_begin(20)
ssl.add_begin(30)
ssl.add_begin(40)
ssl.display()
print("\n")
ssl.rotate(3)
ssl.display

