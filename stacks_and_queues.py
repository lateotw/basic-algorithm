class Stack(object):

	def __init__(self):
		self.stack = []
		self.numOfItems = 0

	def isEmpty(self):
		return self.stack == []

	def push(self, data):
		self.stack.insert(self.numOfItems,data)
		self.numOfItems = self.numOfItems+1

	def pop(self):
		self.numOfItems = self.numOfItems - 1
		dataToReturn = self.stack.pop(self.numOfItems)
		return dataToReturn

	def size(self):
		return len(self.stack)



class Queue(object):

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.insert(0,data)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)
