"""
Write a program which
- Takes a list of integers (list ends with -1)
- Creates a linked list with input data
- Implement inplace reversal of linked list
- Implement print linked list
"""

# class Dog:
    
#     kind = 'canine'         # class variable shared by all instances

#     def __init__(self, name):
#         self.name = name    # instance variable unique to each instance
class LinkedListNode():
    # There can only be one constructor in Python
    # However, default values can be provided
    def __init__(self, val=None, nextNode=None):
        self.value = val
        self.next  = nextNode

class LinkedList():
    def __init__(self, headNode=None):
        self.head = headNode

    def printLinkedList(self):
        if self.head is not None:
            temp = self.head
            # print("In print, first val: ", temp.value)
            outList = []
            while temp is not None:
                outList.append(temp.value)
                temp = temp.next

            print(outList)
        else:
            print(self.head)

    def reverseInPlace(self):
        # main idea
        # [2] -> [3] -> [-1] -> [11]
        # [2] <- [3] <- [-1] <- [11]

        # Handle corner cases
        if self.head is None or self.head.next is None:
            return
     
         # normal case

        first = self.head
        second = first.next
        first.next = None

        while second is not None:
            temp = second.next
            second.next = first
            first = second
            second = temp

        self.head = first

def createLinkedList(inList : list)-> list:
    if inList:
        firstNode = LinkedListNode(inList[0])
        previousNode = firstNode

        for item in inList[1:]:
            # print("Current list val: ", item)
            currentNode =  LinkedListNode(item)
            previousNode.next = currentNode 
            previousNode = currentNode
        return LinkedList(firstNode)
    else:
        return LinkedList()

def testReverse(inList):

    print("Input list values: ", inList)

    linkedList = createLinkedList(inList)
    

    print("LinkedList created: ", end='')
    linkedList.printLinkedList()

    linkedList.reverseInPlace()

    
    print("LinkedList reverse: ", end='')
    linkedList.printLinkedList()

if __name__ == "__main__":

    input_00 = [2, 3, 5, 1, -10, 22, 11, 2]
    input_01 = [2]
    input_02 = []    

    testReverse(input_00)
    testReverse(input_01)
    testReverse(input_02)


 



