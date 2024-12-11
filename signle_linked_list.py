class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
l=Node(10)
l.next=Node(11)
l.next=Node(12)
print(l.next)
