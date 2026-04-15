class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def dfs(i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            # First, case of adding the current element
            cur.append(nums[i])
            dfs(i+1)
            # Second, case of not adding the current element
            cur.pop()
            dfs(i+1)
        dfs(0)
        return res