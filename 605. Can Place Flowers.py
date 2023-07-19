from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0)and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                flowerbed[i]=1
                n-=1
                if n==0:
                    return True
        return False


# Sample input for testing
flowerbed = [1,0,0,0,1,0,0]
n = 2

# Create an instance of the Solution class
solution = Solution()

# Call the canPlaceFlowers function
result = solution.canPlaceFlowers(flowerbed, n)

# Print the result
print(result)
