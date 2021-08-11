class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def reverse(self):
        if(self.head==None):
            return self.head
        curr = self.head
        prev = None
        while(curr != None):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    def pallin(self):
        fast = self.head
        slow = self.head
        while(fast != None and fast.next != None):
            fast = fast.next.next
            if(fast is None):
                mid = slow.next
                break
            if (fast.next is None):
                mid = slow.next.next
                break
            slow = slow.next
        slow.next = None
        mid = reversed(mid)
        return mid,self.head
    def compare(self,head,mid_reverse):
        while(self.head != None or mid_reverse != None):
            if(self.head.data != mid_reverse.data):
                return -1
            self.head = self.head.next
            mid_reverse = mid_reverse.next
        return 1
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    head =  Node('R')
    nodeB = Node('A')
    nodeC = Node('D')

    nodeD = Node('T')
    nodeE = Node('A')
    nodeF = Node('R')

    head.next = nodeB
    nodeB.next = nodeC
    nodeC.next = nodeD
    nodeD.next = nodeE
    nodeE.next = nodeF

    a,r = pallin(head)
    a = compare(a,r)
    if(a==1):
        print("PALLINDROME")
    else:
        print("NOT PALLINDROME")