# Brute force
class MyHashSet:

    def __init__(self):
        self.data = []
        

    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.data else False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
#---------------------------------------------------------------------
# class MyHashSet:

#     def __init__(self):
        

#     def add(self, key: int) -> None:
        

#     def remove(self, key: int) -> None:
        

#     def contains(self, key: int) -> bool:
        


# # Your MyHashSet object will be instantiated and called as such:
# # obj = MyHashSet()
# # obj.add(key)
# # obj.remove(key)
# # param_3 = obj.contains(key)