class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def remove(self,node:Node):
        prevN= node.prev
        nextN=node.next
        node.prev.next=nextN
        node.next.prev=prevN
    def insert(self, node:Node):
        oldN=self.head.next

        node.next=oldN
        node.prev=self.head
        self.head.next=node
        oldN.prev=node  


    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1    
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self.remove(node)
            self.insert(node)
        else:
            newN = Node(key, value)
            self.cache[key]=newN
            self.insert(newN)

            if len(self.cache) > self.capacity:
                oldNode=self.tail.prev
                self.remove(oldNode)  
                del self.cache[oldNode.key]
        
          
        

    