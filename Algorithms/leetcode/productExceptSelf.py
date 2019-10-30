#https://leetcode.com/problems/product-of-array-except-self/submissions/
#[24, 12, 8, 6]
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        arrlen = len(nums)
        ret = [1]*arrlen
        t1 = [1]*arrlen
        t2 = [1]*arrlen

        #left-right
        for i in range(arrlen-1):
            t1[i+1] = nums[i]*t1[i]
        print(t1)

        #right-left
        for i in range(arrlen-1,0,-1):
            t2[i-1] = t2[i]*nums[i]
        print(t2)

        for i in range(arrlen):
            ret[i] = t2[i]*t1[i]

        return ret
        
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))