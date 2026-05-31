class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Questions
        # 1. can input string be empty?
        # 2. are the strings case sensitive?
        # 3. Can strings contain special characters or numbers?

        # Approach
        # 1. sorting
        # crete a dictionary -> sort the string and use as a key, and store original as valye
        # res = defaultdict(list)
        # for s in strs:
        #     sortedS = tuple(sorted(s))
        #     res[sortedS].append(s)
        # return list(res.values())
        # # BigO -> O(N + n log n)


        # 2. Hash Table O(m*n)
        # use hashtable and count as a key, store s as a value
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())


        