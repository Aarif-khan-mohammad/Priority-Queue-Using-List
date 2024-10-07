class PriorityQueue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,data,priority):
        index = 0
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index ,(data,priority))
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Empty")
        else:
            return self.items.pop(0)[0] #deleting the highest priority tuple of data and returing the data 
    
    def size(self):
        return len(self.items)

pq = PriorityQueue()

pq.push(10,0)
pq.push(30,2)
pq.push(20,1)
pq.push(40,3)
print(pq.items)
pq.pop()
print(pq.items)

for x in pq.items:
    print(x[0])
#or 

while not pq.is_empty():
    print(pq.pop())