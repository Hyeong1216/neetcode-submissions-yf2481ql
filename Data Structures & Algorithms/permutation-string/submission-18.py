class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1. Brute force
        # s1_sorted = sorted(s1)
        # for i in range(len(s2)):
        #     for j in range(i, len(s2)):
        #         s2_sorted = sorted(s2[i:j+1])
        #         if s1_sorted == s2_sorted:
        #             return True
        # return False
        #-----------------------------------------------------
        # 2. Sliding window + alphabet count comparison
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for c in s1:
            count1[ord(c)-ord('a')] += 1
        
        for i in range(len(s1)):
            count2[ord(s2[i])-ord('a')] += 1

        if count1 == count2:
            return True
        
        for i in range(len(s1), len(s2)):
            count2[ord(s2[i])-ord('a')] += 1
            count2[ord(s2[i - len(s1)])-ord('a')] -= 1

            if count1 == count2:
                return True

        return False