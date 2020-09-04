class Node:
    def __init__(self,key=None,value=None):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=Node(0)
        self.tail=Node(0)
        self.cache=dict()
        self.size=0
        
        self.head.next=self.tail
        self.tail.prev=self.head

    def add_to_head(self, node):
        node.prev=self.head
        node.next=self.head.next
        
        self.head.next.prev=node
        self.head.next=node
    
    def remove_from_tail(self):
        node_to_remove=self.tail.prev
        self.remove_node(node_to_remove)
        return node_to_remove
        
    def remove_node(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev
        
    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node=self.cache[key]
        self.move_to_head(node)
        
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key,None):
            node=self.cache.get(key,None)
            node.value=value
            self.move_to_head(node)
        else:
            new_node=Node(key=key,value=value)
            self.cache[key]=new_node
            self.add_to_head(new_node)
            self.size+=1
            
            if self.size>self.capacity:
                node_to_remove=self.remove_from_tail()
                del self.cache[node_to_remove.key]
                self.size-=1
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)