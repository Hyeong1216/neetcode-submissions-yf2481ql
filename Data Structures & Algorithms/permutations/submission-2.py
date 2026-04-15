class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        visited = set()
        def bt(visited, subset):
            if len(visited) == n:
                res.append(subset[:])

            for i in range(n):
                if nums[i] not in visited:
                    subset.append(nums[i])
                    visited.add(nums[i])
                    bt(visited, subset)
                    subset.pop()
                    visited.remove(nums[i])

        bt(visited, [])
        return res