class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size=0

    def insertEnd(self,data):

        self.size=self.size+1
        newNode=Node(data)
        
        actualNode=self.head
        
        if not self.head:
            self.head=newNode
        else:
            while actualNode.nextNode is not None:
                actualNode=actualNode.nextNode
            actualNode.nextNode=newNode
    
    def reverse(self):
        previousNode=None
        currentNode=self.head
        while(currentNode is not None):
            nextNode=currentNode.nextNode
            currentNode.nextNode=previousNode
            previousNode=currentNode
            currentNode=nextNode
        self.head=previousNode

    def traverseList(self) :
        actualNode = self.head
        while actualNode is not None:
            print("%d " % actualNode.data,end=" ")
            actualNode = actualNode.nextNode


linkedlist=LinkedList()
b=1
while(b):
    b=int(input("\nEnter choice\n 1 to insert   \n 2 to traverse \n 3 to reverse \n 0 to exit: \n "))
    if b==1:
        a=int(input("Enter a number: "))
        linkedlist.insertEnd(a)
    elif b==2:
        linkedlist.traverseList()
    elif b==3:
        linkedlist.reverse()