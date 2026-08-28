class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        out_deg = [0] * (n + 1)
        in_deg = [0] * (n + 1)

        for i in range(len(trust)):
            first, second = trust[i]
            out_deg[first] += 1
            in_deg[second] += 1
        print(out_deg)
        print(in_deg)

        for i in range(len(out_deg)):
            if out_deg[i] == 0 and in_deg[i] == (n-1):
                return i
        return -1            
