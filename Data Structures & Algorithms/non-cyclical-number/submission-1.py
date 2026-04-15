class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        num = n
        while num not in visited:
            visited.add(num)

            digits = [int(d) for d in str(abs(num))]
            temp = 0
            for digit in digits:
                temp += (digit ** 2)
            if temp == 1:
                return True
            num = temp
        return False