class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group -> use the counter map or list tuple
        # use counter tuple as a key and value as a orinal words
        
        Map = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            if tuple(count) not in Map:
                Map[tuple(count)] = [s]
            else:
                Map.get(tuple(count)).append(s)
        # print(Map)

        # for key, value in Map.items():
        return list(Map.values())




































# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # group -> use the counter map or list tuple
#         # use counter tuple as a key and value as a orinal words
        
#         Map = {}
#         for i in range(len(strs)):
#             temp_counter = [0] * 26

#             for c in range(len(strs[i])):
#                 curr_char = strs[i][c]
#                 temp_counter[ord(curr_char) - ord('a')] += 1

#             if tuple(temp_counter) not in Map:
#                 Map[tuple(temp_counter)] = [strs[i]]
#             else:
#                 Map.get(tuple(temp_counter)).append(strs[i])

#         return list(Map.values())
            
            




























# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # Questions
#         # 1. can input string be empty?
#         # 2. are the strings case sensitive?
#         # 3. Can strings contain special characters or numbers?

#         # Approach
#         # 1. sorting
#         # crete a dictionary -> sort the string and use as a key, and store original as valye
#         # res = defaultdict(list)
#         # for s in strs:
#         #     sortedS = tuple(sorted(s))
#         #     res[sortedS].append(s)
#         # return list(res.values())
#         # # BigO -> O(N * k log k)


#         # 2. Hash Table O(m*n)
#         # use hashtable and count as a key, store s as a value
#         ans = defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c)-ord('a')] += 1
#             ans[tuple(count)].append(s)
#         return list(ans.values())

# # N = len(strs), K = 평균 문자열 길이

# # Sorting:    O(N * K log K) — 각 문자열 정렬
# # Hash Table: O(N * K)       — 각 문자열 한 번씩 순회
        