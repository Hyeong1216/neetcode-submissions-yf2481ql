class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        res = []
        for i in range(len(temperatures)):
            count = 0

            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    count = j-i
                    break


            res.append(count)
        return res