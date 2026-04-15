class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. sorting
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

        # 2. Hash Table O(m*n)


        