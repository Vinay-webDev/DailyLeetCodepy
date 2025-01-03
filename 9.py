"""03/02/25"""
nums1 = [10,4,-8,7]
nums2 = [2,3,1,0]
class Solution:
    def waysToSplitArray(self, nums):
        right = sum(nums)
        left = 0
        count = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]
            if left >= right:
                count += 1
        return count
sol = Solution()
print(sol.waysToSplitArray(nums1))  #2
print(sol.waysToSplitArray(nums2))  #2

#✅✅✅✅✅






















