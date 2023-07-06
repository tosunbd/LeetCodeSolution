class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        length = self.gcd(len(str1), len(str2))
        return str1[:length]
    
    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

# Create an instance of the Solution class
# Create an instance of the Solution class
solution = Solution()

# Example inputs
str1 = "LEET"
str2 = "CODE"

# Call the gcdOfStrings method
result = solution.gcdOfStrings(str1, str2)

# Print the result
print(result)

# another solution using recursion
    # if(len(str1) < len(str2)):
    #         return self.gcdOfStrings(str2, str1)
    #     elif(not str1.startswith(str2)):
    #         return ""
    #     elif(len(str2) == 0):
    #         return str1
    #     else:        
    #         return self.gcdOfStrings(str1[len(str2):], str2)
