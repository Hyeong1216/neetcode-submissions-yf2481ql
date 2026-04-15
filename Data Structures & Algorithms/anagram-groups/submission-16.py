class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Sorting
        # res = defaultdict(list)
        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     res[sortedS].append(s)
        # return list(res.values())


        # 2. Hash Table: O(m*n)
        # ans = defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c)-ord('a')] += 1
        #     ans[tuple(count)].append(s)
        # return list(ans.values())

        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())















        #-----------------------------------------
        # ans = defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     ans[tuple(count)].append(s)

        # return list(ans.values())