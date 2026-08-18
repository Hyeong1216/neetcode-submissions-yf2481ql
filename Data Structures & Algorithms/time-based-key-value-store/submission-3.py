class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        l, r = 0, len(self.data[key])-1
        res = ""
        while l <= r:
            m = l + (r-l)//2
        
            if self.data[key][m][0] <= timestamp:
                res = self.data[key][m][1]
                l = m + 1
            else:
                r = m - 1

        return res
        


        
