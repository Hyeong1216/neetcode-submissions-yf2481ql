class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for digit in digits:
            num += str(digit)
        num = str(int(num) + 1)
        res = []
        for i in range(len(num)):
            res.append(num[i])
        return res

