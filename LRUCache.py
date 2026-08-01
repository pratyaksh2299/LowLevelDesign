
# Node class for the doubly linked list
class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):

        self.head = Node(None ,None)
        self.tail = Node(None , None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node_to_head(self, node : Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self,node :Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_node_from_tail(self):
        if self.tail.prev ==self.head:
            return None
        node_to_remove = self.tail.prev
        self.remove_node(node_to_remove)
        return node_to_remove

    def move_node_to_head(self, node : Node):
        self.remove_node(node)
        self.add_node_to_head(node)

# LRU Cache class
class LRUCache:

    def __init__(self,capacity: int):
      self.capacity = capacity
      self.cache = {}
      self.dll = DoublyLinkedList()

    def get(self,key):
        if key in self.cache:
            node = self.cache[key]
            self.dll.move_node_to_head(node)
            return node.value
        return -1

    def put(self,key,value):
        if key in self.cache :
            node = self.cache[key]
            node.value = value
            self.dll.move_node_to_head(node)
        else :
            if len(self.cache)>= self.capacity:
                node_to_remove = self.dll.remove_node_from_tail()
                if node_to_remove :
                    del self.cache[node_to_remove.key]
        new_node = Node(key,value)
        self.dll.add_node_to_head(new_node)
        self.cache[key] = new_node

if __name__ == "__main__":
    lru_cache = LRUCache(3)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    lru_cache.put(3, 3)
    print(lru_cache.get(1))  # Output: 1
    lru_cache.put(4, 4)  # This will evict key 2
    print(lru_cache.get(2))  # Output: -1 (not found)
    print(lru_cache.get(3))  # Output: 3
    print(lru_cache.get(4))  # Output: 4
    