from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numdict = defaultdict(list)
        numset = set(nums)
        for n in numset:
            numdict[n] = nums.count(n)
        answer = -1
        for k in numdict.keys():
            if numdict[k] > len(nums)//2:
                answer = k
                break
        return k