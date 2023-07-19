from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        length = len(nums)
        if(length < 0): return False
        left = float('inf')
        mid = float('inf')

        for i in range(length):
            if nums[i] > mid: return True
            if nums[i] > left and nums[i] < mid:
                mid = nums[i]
            if nums[i] < left:
                left = nums[i]
        return False


# Sample input for testing
nums = [2,1,5,0,4,6]

# Create an instance of the Solution class
solution = Solution()

# Call the canPlaceFlowers function
result = solution.increasingTriplet(nums)

# Print the result
print(result)
