class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"]":"[", ")":"(", "}":"{"}

        for c in s:
            if c not in d: #opening
                stack.append(c)
                continue
            
            if not stack or stack.pop() != d[c]:
                return False
        


        return not stack
            
            



































# class Solution:
#     def isValid(self, s: str) -> bool:
#         # Questions:
#         # 1. can there be special characters or numbers in input?
#         # 2. can the string be empty?
#         # 3. Is it always just three 3 pairs?


#         # Solution
#         Map = {"}":"{", ")":"(", "]":"["}
#         stack = []

#         for c in s:
#             if c not in Map: #means opening
#                 stack.append(c)
#                 continue
#             # when closing, because if it is closing
#             # stack should not be empty,  
#             # and it has to match the pair opening 
#             if not stack or stack[-1] != Map[c]:
#                 return False
#             stack.pop()
#         return not stack

#         #BigO -> O(N)













# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         dic = {"]":"[", ")":"(", "}":"{"}


#         for c in s:

#             if c in dic: # meaning closings
#                 if not stack or stack.pop() != dic[c]:
#                     return False
#                 continue # to next iteration

#             stack.append(c) # only appending openings
        
#         return True if not stack else False




































# # class Solution:
# #     def isValid(self, s: str) -> bool:
# #         # Questions:
# #         # 1. can there be special characters or numbers in input?
# #         # 2. can the string be empty?
# #         # 3. Is it always just three 3 pairs?


# #         # Solution
# #         Map = {"}":"{", ")":"(", "]":"["}
# #         stack = []

# #         for c in s:
# #             if c not in Map: #means opening
# #                 stack.append(c)
# #                 continue
# #             # when closing, because if it is closing
# #             # stack should not be empty,  
# #             # and it has to match the pair opening 
# #             if not stack or stack[-1] != Map[c]:
# #                 return False
# #             stack.pop()
# #         return not stack

# #         #BigO -> O(N)