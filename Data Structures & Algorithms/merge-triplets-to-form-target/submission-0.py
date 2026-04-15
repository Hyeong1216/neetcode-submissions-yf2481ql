class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target

        achieved = [False, False, False]

        for triplet in triplets:
            a, b, c = triplet

            # TODO: Check if this triplet is valid (doesn't exceed target)
            # If any value exceeds target, skip this triplet
            if a > x or b > y or c > z:
                continue
            
            # TODO: If valid, check which target values this triplet matches
            # Update 'achieved' accordingly
            if a == x:
                achieved[0] = True
            if b == y:
                achieved[1] = True
            if c == z:
                achieved[2] = True



        return all(achieved)