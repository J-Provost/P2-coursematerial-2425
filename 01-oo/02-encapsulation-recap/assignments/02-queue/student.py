class Queue:
    def __init__(self):
        self.__queue = []

    def add(self,item):
        self.__queue.append(item)
    
    def next(self):
        next = self.__queue[0]
        del self.__queue[0]
        # if self.is_empty() == True:
        #     return print("Queue is completed")
        # print(f'{self.__queue[0]} is next')
        return next

    def is_empty(self):
        if len(self.__queue) == 0:
            return True
        return False

queue = Queue()

queue.add('Alice')   # Alice arrives first
queue.add('Bob')     # Then Bob
queue.add('Charlie') # And Charlie as third

print(queue.next())   # Alice arrived first, so she's the first to be served next
print(queue.next())   # This must return Bob
print(queue.next())