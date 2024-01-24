class Solution:
    def sortedSquares(self, nums):
        left, right = 0, len(nums) - 1
        result = [0] * len(nums)
        i = len(nums) - 1

        while left <= right:
            if nums[left] ** 2 <= nums[right] ** 2:
                result[i] = nums[right] ** 2
                right -= 1
            else:
                result[i] = nums[left] ** 2
                left += 1
            i -= 1
        
        return result