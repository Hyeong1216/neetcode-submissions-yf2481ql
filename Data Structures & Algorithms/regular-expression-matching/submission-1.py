class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Top down
        # memo = {}

        # def dp(i, j):
        #     if j == len(p):
        #         return i == len(s)
            
        #     if (i, j) in memo:
        #         return memo[(i, j)]
            

        #     match = i < len(s) and (s[i] == p[j] or p[j] == '.')
        #     print(match)
        #     if j+1 < len(p) and p[j+1] == '*':
        #         result = dp(i, j+2) or (match and dp(i+1, j))
        #     else:
        #         result = match and dp(i+1, j+1)



        #     memo[(i, j)] = result
        #     return result

        # return dp(0, 0)
        #-----------------------------------
        # top down
        memo = {}

        def dp(i, j):
            if j == len(p):
                return i == len(s)
            
            if (i, j) in memo:
                return memo[(i, j)]

            match = i < len(s) and ((s[i] == p[j]) or (p[j] == "."))

            if j+1 < len(p) and p[j+1] == "*":
                result = dp(i, j+2) or (match and dp(i+1, j))
            else:
                result = match and dp(i+1, j+1)


            memo[(i, j)] = result

            return result


        
        return dp(0, 0)


        
        # bottom up