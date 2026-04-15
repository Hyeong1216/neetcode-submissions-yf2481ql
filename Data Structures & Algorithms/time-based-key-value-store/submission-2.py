class TimeMap:

    def __init__(self):
        self.data = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        # need to initialize the empty list for the key, if key does not exist
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        l, r = 0, len(self.data[key]) - 1
        res = ""
        while l <= r:
            mid = l + (r-l) // 2
            if self.data[key][mid][0] <= timestamp:
                res = self.data[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res








# class TimeMap:

#     def __init__(self):
#         self.data = {}

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         # need to initialize the empty list for the key, if key does not exist
#         if key not in self.data:
#             self.data[key] = []
#         self.data[key].append((timestamp, value))

#     def get(self, key: str, timestamp: int) -> str:
#         if key not in self.data:
#             return ""
#         l, r = 0, len(self.data[key]) - 1
#         result = ""

#         while l <= r:
#             mid = l + (r-l) // 2
#             if self.data[key][mid][0] <= timestamp:
#                 result = self.data[key][mid][1]
#                 l = mid + 1
#             else:
#                 r = mid - 1




#         return result
