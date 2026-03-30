class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node: Node) -> None:
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node    

    def add_to_end(self, node: Node) -> None:
        prev_last = self.tail.prev
        prev_last.next = node
        node.prev = prev_last
        node.next = self.tail
        self.tail.prev = node
        

    def get(self, key: int) -> int:
        if key not in self.cache_map:
            return -1

        curr_node = self.cache_map[key]
        self.remove_node(curr_node)
        self.add_to_end(curr_node)

        return curr_node.value


    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            old_node = self.cache_map[key]
            self.remove_node(old_node)

        curr_node = Node(key, value)
        self.cache_map[key]=curr_node
        self.add_to_end(curr_node)

        if len(self.cache_map)> self.capacity:
            left_node = self.head.next    
            del self.cache_map[left_node.key]
            self.remove_node(left_node)
           
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)