from typing import List

class Solution(object):
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        answer = [0 for _ in range(numsLen)]
        product = 1

        for i in range(numsLen):
            answer[i] = product
            product *= nums[i]

        product = 1
        for i in range(numsLen - 1, -1, -1):
            answer[i] *= product
            product *= nums[i]

        return answer

# Example input
<<<<<<< HEAD
nums = [-1, 1, 0, -3, 3]
=======
nums = [-1,1,0,-3,3]
>>>>>>> e6e485ac1e7d301931f6ddfb1da313fd65a3e786

# Create an instance of the Solution class
solution = Solution()

# Call the productExceptSelf method
result = solution.productExceptSelf(nums)

# Print the result
print(result)
