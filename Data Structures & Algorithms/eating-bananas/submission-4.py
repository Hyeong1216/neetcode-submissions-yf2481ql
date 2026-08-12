class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        if len(piles) == h:
            return r
        
        while l <= r:
            m = l + (r-l) // 2
            total_time = 0

            for pile in piles:
                total_time += math.ceil(pile/m)
            
            if total_time <= h:
                res = m
                r = m - 1
                
            else:
                l = m + 1       





        return res







































# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         l, r = 1, max(piles)

#         while l <= r:
#             mid = l + (r-l) // 2
#             total_time = 0

#             for p in piles:
#                 total_time += math.ceil(float(p)/mid)
#             if total_time <= h:
#                 res = mid
#                 r = mid - 1
#             else:
#                 l = mid + 1



        
#         return res