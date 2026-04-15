class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)
        
        for i in range(len(s2)):
            for j in range(i+1, len(s2)+1):
                s2_sorted = sorted(s2[i:j])
                print(f"{s1_sorted} : {s2_sorted}")
                if s1_sorted == s2_sorted:
                    return True
        return False
