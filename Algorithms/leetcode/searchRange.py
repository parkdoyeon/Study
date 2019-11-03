class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for idx, n in enumerate(nums):
            if n == target:
                answer.append(idx)
            elif n > target:
                break
        if len(answer) == 0:
            return [-1, -1]
        else:
            return [answer[0], answer[-1]]