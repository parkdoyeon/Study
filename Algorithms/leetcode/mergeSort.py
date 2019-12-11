class Solution:
    
    def sortArray(self, nums: List[int]) -> List[int]:
        self.findMid(nums, 0, len(nums))
        return nums
    
    def findMid(self, arr, low, high):
        if high-low < 2:
            return
        mid = (low+high)//2
        self.findMid(arr, low, mid)
        self.findMid(arr, mid, high)
        self.merge(arr, low, mid, high)
    
    def merge(self, arr, low, mid, high):
        tmp = []
        l, h = low, mid
        while l < mid and h < high:
            if arr[l] < arr[h]:
                tmp.append(arr[l])
                l += 1
            else:
                tmp.append(arr[h])
                h += 1
        while l < mid:
            tmp.append(arr[l])
            l += 1
        while h < high:
            tmp.append(arr[h])
            h += 1
        for i in range(low, high):
            arr[i] = tmp[i-low]
        return