class Node(object):

    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self,data):
        if data < self.data:
            if not self.leftChild:
                self.leftChild = Node(data)
            else:
                self.leftChild.insert(data)
        else:
            if not self.rightChild:
                self.rightChild = Node(data)
            else:
                self.rightChild.insert(data)

    def minValue(self):
        if( self.leftChild == None ):
            return self.data
        else:
            return self.leftChild.minValue()

    def remove(self, data, parentNode):

        if( data < self.data ):
            if( self.leftChild is not None ):
                self.leftChild.remove(data, self)
        elif( data > self.data ):
            if( self.rightChild is not None ):
                self.rightChild.remove(data, self)
        else:
            if( self.leftChild is not None and self.rightChild is not None ):
                self.data = self.rightChild.minValue()
                self.rightChild.remove(self.data, self)
            elif( parentNode.leftChild == self ):
                if( self.leftChild is not None):
                    tempNode = self.leftChild
                else:
                    tempNode = self.rightChild

                parentNode.leftChild = tempNode
            elif( parentNode.rightChild == self ):
                if( self.leftChild is not None):
                    tempNode = self.leftChild
                else:
                    tempNode = self.rightChild

                parentNode.rightChild = tempNode




    def traverseInOrder(self):

        if self.leftChild:
            self.leftChild.traverseInOrder()

        print(self.data)

        if self.rightChild:
            self.rightChild.traverseInOrder()

        print(self.data)

class BinarySearchTree(object):

    def __init__(self):
        self.rootNode = None

    def insert(self,data):
        if( not self.rootNode ):
            self.rootNode = Node(data)
        else:
            self.rootNode.insert(data)

    def remove(self, dataToRemove):
        if( self.rootNode ):
            if( self.rootNode.data == dataToRemove ):
                tempNode = Node(None)
                tempNode.leftChild = self.rootNode
                self.rootNode.remove(dataToRemove,tempNode)
				self.rootNode = tempNode.leftChild
            else:
                self.rootNode.remove(dataToRemove,None)



    def getMax(self):

        maxNode = self.rootNode

        while maxNode.rightChild:
            maxNode = maxNode.rightChild

        return maxNode.data

    def getMin(self):

        minNode = self.rootNode

        while minNode.leftChild:
            minNode = minNode.leftChild

        return minNode.data

    def traverseInOrder(self):
        if self.rootNode:
            self.rootNode.traverseInOrder()
