class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtrack
        res = []

        def bt(start, curr):
            if start > len(nums):
                return
            res.append(curr[:])

            for i in range(start, len(nums)):
                curr.append(nums[i])
                bt(i+1, curr)
                curr.pop()              
        bt(0, [])
        return res
















# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         #backtrack
#         res = []
#         def bt(start, subset):
#             res.append(subset[:])
#             for i in range(start, len(nums)):
#                 subset.append(nums[i])
#                 bt(i+1, subset)
#                 subset.pop()


#         bt(0, [])
#         return res

























# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         # iterative solution 한번 더 보기


#         # backtrack
#         res = []
#         def bt(start, curr):
#             res.append(curr[:])
#             for i in range(start, len(nums)):
#                 curr.append(nums[i])
#                 bt(i+1, curr)
#                 curr.pop()

#         bt(0, [])
#         return res





















#--------------------------------------------------------------------------------

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         #iterative
#         # res = [[]]  # 빈 집합부터 시작
#         # for num in nums:
#         #     temp = []
#         #     for i in range(len(res)):
#         #         # 기존에 만들어둔 모든 부분집합에 현재 num을 추가한 새 부분집합 생성
#         #         temp.append(res[i] + [num])
#         #     # 새로 만든 부분집합들을 기존 res에 추가
#         #     # (num을 안 쓴 것 + num을 쓴 것 모두 남게 됨)
#         #     res.extend(temp)
#         # return res

#         # backtracking
#         res = []
#         def bt(start, subset):
#             # 현재까지 만든 subset을 결과에 추가
#             # (재귀 호출마다 매번 추가하므로, 모든 크기의 부분집합이 다 담김)
#             res.append(subset[:])  # subset[:]로 복사본을 넣어야 함
#                                     # (그냥 subset을 넣으면 나중에 pop 될 때 값이 같이 변함)

#             for i in range(start, len(nums)):
#                 # nums[i]를 현재 부분집합에 포함시켜보기
#                 subset.append(nums[i])

#                 # nums[i] 다음 인덱스(i+1)부터 다시 탐색
#                 # -> 같은 원소를 두 번 쓰지 않고, 순서도 항상 오름차순으로 유지
#                 bt(i+1, subset)

#                 # 되돌아와서(백트래킹) nums[i]를 뺀 상태로 복원
#                 # -> 다음 반복(i+1번째 원소)을 시도하기 위해 원상복구
#                 subset.pop()

#         bt(0, [])
#         return res