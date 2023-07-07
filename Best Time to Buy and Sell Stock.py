from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0

        for right in range(1, len(prices)):
            if prices[right] > prices[left]:
                profit = max(profit, prices[right] - prices[left])
            else:
                left = right
        return profit


# Example input for testing
prices = [7, 1, 5, 3, 6, 4]

# Create an instance of the Solution class
solution = Solution()

# Call the maxProfit function
result = solution.maxProfit(prices)

# Print the result
print(result)
