class Node:
    def __init__(self,key):
        self.key=key
        self.freq=1
        self.prev=None
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
class AllOne:
    def __init__(self)-> None:
        self.keyNodeMap={}
        self.freqListMap=OrderedDict()
        self.freqListMap[1]=LinkedList()
        
    def addAtFront(self, node):
        if node.freq not in self.freqListMap:
            l1=LinkedList()
            self.freqListMap[node.freq]=l1
            l1.head=l1.tail=node
        else:
            l1=self.freqListMap[node.freq]
            if not l1.tail:
                l1.head=l1.tail=node
            else:
                node.next=l1.head
                l1.head.prev=node
                l1.head=node
                
    def deleteNode(self,node)-> None:
        l1=self.freqListMap[node.freq]
        if not node.prev: 
            l1.head=node.next
        else:
            node.prev.next=node.next
        if not node.next:
            l1.tail=node.prev
        else:
            node.next.prev=node.prev
        
    def inc(self, key: str) -> None:
        if key not in self.keyNodeMap:
            self.keyNodeMap[key]=node=Node(key)
        else:
            node=self.keyNodeMap[key]
            self.deleteNode(node)
            node.freq+=1
            node.prev=node.next=None
        self.addAtFront(node)
    ''
    def dec(self, key: str) -> None:
        node=self.keyNodeMap[key]
        self.deleteNode(node)
        node.freq-=1
        if node.freq:
            self.addAtFront(node)
        else:
            del self.keyNodeMap[key]
            del node
            
    def getMaxKey(self) -> str:
        for freq in reversed(self.freqListMap.keys()):
            l1=self.freqListMap[freq]
            if l1.head:
                return l1.head.key
        return ""
        
    def getMinKey(self) -> str:
        for freq in self.freqListMap.keys():
            l1=self.freqListMap[freq]
            if l1.head:
                return l1.head.key
        return ""