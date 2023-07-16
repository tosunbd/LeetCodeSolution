from typing import List

class Solution(object):
    # def thirdMax(self, nums: List[int]) -> int:
    #     first = second = third = float('-inf')

    #     for num in nums:
    #         if num > first:
    #             third = second
    #             second = first
    #             first = num
    #         elif num > second and num != first:
    #             third = second
    #             second = num
    #         elif num > third and num != second and num != first:
    #             third = num

    #     return third if third != float('-inf') else first
        # return [first, second, third]
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) > 2:
            return nums[-3]
        return nums[-1]

# Example input
nums = [2, 2, 3, 1]

# Create an instance of the Solution class
solution = Solution()

# Call the thirdMax method
result = solution.thirdMax(nums)

# Print the result
print(result)
