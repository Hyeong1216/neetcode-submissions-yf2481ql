class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        curr_map = {} # val > index
        for i, n in enumerate(nums):
            # print("i: ", i, ", n: ", n)
            diff = target - n
            if diff in curr_map:
                return [curr_map[diff], i]
            curr_map[n] = i