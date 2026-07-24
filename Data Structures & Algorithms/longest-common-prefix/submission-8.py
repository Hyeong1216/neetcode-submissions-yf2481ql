class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for i in range(1, len(strs)):
            res = res[:len(strs[i])]
            for j in range(len(strs[i])):
                if j < len(res) and res[j] != strs[i][j]:
                    res = res[:j]
                    break


        return res