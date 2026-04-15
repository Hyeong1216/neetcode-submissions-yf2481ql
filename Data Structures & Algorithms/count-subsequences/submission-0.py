class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # top down
        memo = {}

        def helper(s_idx, t_idx):
            if len(t) == t_idx:
                return 1
            
            if len(s) == s_idx:
                return 0

            if (s_idx, t_idx) in memo:
                return memo[(s_idx, t_idx)]
            
            result = 0
            if s[s_idx] == t[t_idx]:
                result += helper(s_idx+1, t_idx+1)
                result += helper(s_idx+1, t_idx)
            else:
                result += helper(s_idx+1, t_idx)

            memo[(s_idx, t_idx)] = result
            return result
        return helper(0, 0)