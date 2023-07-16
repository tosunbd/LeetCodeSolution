from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countVal = {}
        for i in range(len(nums)):
            if nums[i] in countVal:
                return True
            countVal[nums[i]] = 1
        return False


# Create an instance of the Solution class
solution = Solution()

# Example input for testing
nums = [1, 2, 3, 1]

# Call the containsDuplicate function
result = solution.containsDuplicate(nums)

# Print the result
print(result)
