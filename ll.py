class Node:
    def __init__(self,Data):
        self.data=Data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertBegin(self,Data):
        newNode=Node(Data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    def display(self):
        if self.head is None:
            print("LL is empty")
        else:
            current=self.head
            while current:
                print(current.data,end=" ")
                current=current.next
ll=LinkedList()
ll.display()
ll.insertBegin(100)
ll.insertBegin(200)
ll.insertBegin(300)
ll.display()
