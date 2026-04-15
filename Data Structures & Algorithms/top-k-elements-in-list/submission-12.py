class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #----------------------------------------------------------------------
        # 1. Count frequencies of all elements using a hash map.
        # 2. Create frequency buckets - array where index represents frequency, 
        #    and place elements into their corresponding frequency buckets.
        # 3. Collect results by iterating buckets from highest to lowest 
        #    frequency until k elements are found.
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        freq = []
        for num, cnt in count.items():
            freq.append([cnt, num])
        freq.sort()
        res = []
        while len(res) < k:
            res.append(freq.pop()[1])
        return res





        #---------------------------------------------------------
        # Bucket Sort
        # 1. create a count map > populate key:num, value:occurrence
        # 2. create frequency bucket array of length (len(nums)+1), 
        #    sort of inverse map: frequency -> [nums]
        # 3. create result list, iterate freq from high to low and 
        #    add to result until k elements
        # count = {}
        # for num in nums:
        #     count[num] = count.get(num, 0) + 1
        # freq = [[] for _ in range(len(nums) + 1)]
        # for num, cnt in count.items():
        #     freq[cnt].append(num)
        # res = []
        # for i in range(len(freq)-1, 0, -1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res

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