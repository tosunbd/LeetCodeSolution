from typing import List

class Solution(object):
    def thirdMax(self, nums):       
        threelargest = [None, None, None]
        for num in nums:
            self.updateLargest(threelargest, num)

        return threelargest
    
    def updateLargest(self, threelargest, num):
        if threelargest[2] is None or num > threelargest[2]:
            self.shiftAndUpdate(threelargest, num, 2)
        elif threelargest[1] is None or num > threelargest[1]:
            self.shiftAndUpdate(threelargest, num, 1)
        elif threelargest[0] is None or num > threelargest[0]:
            self.shiftAndUpdate(threelargest, num, 0)

    def shiftAndUpdate(self, array, num, idx):
        for i in range(idx + 1):
            if i == idx:
                array[i] = num
            else:
                array[i] = array[i + 1]
                
# Example input
nums = [2, 2, 3, 1]

# Create an instance of the Solution class
solution = Solution()

# Call the thirdMax method
result = solution.thirdMax(nums)

# Print the result
print(result)
