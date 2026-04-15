class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        while l <= r:
            mid = l + (r-l) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p)/mid)
            if total_time <= h:
                res = mid
                r= mid -1
            else:
                l = mid + 1
        return res












        
        
        #---------------------------------------------------------
        # l, r = 1, max(piles)

        # while l <= r:
        #     mid = l + (r - l) // 2
        #     print(f"mid:{mid}")
        #     total_time = 0
        #     for p in piles:
        #         total_time += math.ceil(float(p)/mid)
        #         print(f"total_time:{total_time}")
        #     if total_time <= h:
        #         res = mid
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return res