class Solution(object):
    def threeConsecutiveOdds(self, arr):
        count = 0        
        for num in arr:
            if num % 2 != 0:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
                
        return False

# Example input for testing
arr = [1,2,34,3,4,5,7,23,12]

# Create an instance of the Solution class
solution = Solution()

# Call the threeConsecutiveOdds method
result = solution.threeConsecutiveOdds(arr)

# Print the result
print(result)
