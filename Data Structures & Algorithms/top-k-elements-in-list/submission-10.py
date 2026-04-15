class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. create a count map > populate key:num, value:occurrence
        # 2. create frequency bucket array of length (len(nums)+1), 
        #    sort of inverse map: frequency -> [nums]
        # 3. create result list, iterate freq from high to low and 
        #    add to result until k elements
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res












        #----------------------------------------------------------------------
        # count = {}
        # for num in nums:
        #     count[num] = count.get(num, 0) + 1
        
        # freq = [[] for i in range(len(nums) + 1)]
        # for num, cnt in count.items():
        #     freq[cnt].append(num)
        
        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res