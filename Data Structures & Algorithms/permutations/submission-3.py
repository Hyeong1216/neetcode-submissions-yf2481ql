class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        visited = set()
        def bt(visited, subset):
            if len(visited) == n:
                res.append(subset[:])
                return

            for i in range(n):
                if i not in visited:
                    subset.append(nums[i])
                    visited.add(i)
                    bt(visited, subset)
                    subset.pop()
                    visited.remove(i)

        bt(visited, [])
        return res