class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)
        
        for i in range(len(s2)):
            for j in range(i, len(s2)):
                s2_sorted = sorted(s2[i:j+1])
                print(f"i:{i}:j:{j} | {s1_sorted} : {s2_sorted}")
                if s1_sorted == s2_sorted:
                    return True
        return False
