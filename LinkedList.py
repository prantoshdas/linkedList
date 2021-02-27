class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None #initializes head as empty#

    def insert_front(self,new_node):
        new_node = node(new_node)
        new_node.next = self.head
        self.head = new_node

    def append(self,new_node):
        new_node = node(new_node)
        if self.head is None:
            self.head = new_node
        temp = self.head
        while(temp.next):
            temp = temp.next

        temp.next = new_node

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next



llist=linkedList()
# Node = node(1)
# llist.head = Node
llist.insert_front(7)
llist.append(5)
llist.append(9)
llist.append(4)
llist.insert_front(3)
llist.printlist()