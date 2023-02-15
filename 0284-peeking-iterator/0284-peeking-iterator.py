class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.pointer = -1
        if self.iterator.hasNext():
            self.pointer = self.iterator.next()
        

    def peek(self):
        return self.pointer
        
        
    def next(self):
        temp = self.pointer
        if self.iterator.hasNext():
            self.pointer = self.iterator.next()
        else:
            self.pointer = -1
            
        return temp 
        

    def hasNext(self):
        return self.pointer != -1
    
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].