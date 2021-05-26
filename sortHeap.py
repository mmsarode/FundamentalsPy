# sort numbers using heap
# heap structure: Add, delete
import sys



class maxHeap:
    def __init__(self):
        self.data = []

    def addToHeap(self, value:int):
        self.data.append(value)
        self.heapify()

    def getMax(self):
        if self.data:
            return self.data[0]
        else:
            return -sys.maxsize - 1


    def deleteMax(self)->int:
        if self.data:
            #         0
            #     1       2 
            #   3   4   5   6

            #         6
            #     1       2 
            #   3   4   5   
            
            maxValue = self.data[0]
            n = len(self.data)

            self.data[0] = self.data.pop(-1)
            currNode = 0
            leftChildNode = 2*currNode + 1
            rightChildNode = 2*currNode + 2

            if leftChildNode > n:

            while leftChildNode < n:
                if rightChildNode > n - 1 or (self.data[leftChildNode] > self.data[rightChildNode]):
                    self.data[currNode] = self.data[leftChildNode]
                    currNode = leftChildNode                   
                    # update current Node
                elif rightChildNode < n:
                    self.data[currNode] = self.data[rightChildNode]
                    currNode = rightChildNode
                    # update current Node

                leftChildNode = 2*currNode + 1
                rightChildNode = 2*currNode + 2
            self.data.pop(-1)
            return maxValue            

    def heapify(self):
        #         0
        #     1       2 
        #   3   4   5   6

         #         0
        #     1       2 
        #   3   4   5   
        #   indices: [0, 1, 2, 3, 4, 5, 6]
        #   parentNode: 2, childNodes: 5, 6: (node - 1) // 2
        n = len(self.data)
        currentIdx = n - 1
        parentIdx = (currentIdx - 1)//2

        while parentIdx >= 0:
            if self.data[currentIdx] > self.data[parentIdx]:
                tempValue = self.data[parentIdx]
                self.data[parentIdx] = self.data[currentIdx]
                self.data[currentIdx] = tempValue
            else:
                break
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1)//2

    def printHeap(self):
        print(self.data)

    def isEmpty(self):
        return len(self.data) == 0 

if __name__ == "__main__":
    
    input00 = [ 3, 4, 2, 99, 34, 11, 67, 0 ]

    myMaxHeap = maxHeap()

    for item in input00:
        myMaxHeap.addToHeap(item)
        myMaxHeap.printHeap()

    # Sorted list
    while not myMaxHeap.isEmpty():
        print(myMaxHeap.deleteMax())
        myMaxHeap.printHeap()

    







        





    