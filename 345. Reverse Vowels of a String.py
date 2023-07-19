from typing import List

class Solution:
    def reverseVowels(self, s: str) -> str:
        # vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left].lower() not in vowels:
                left += 1
            elif s[right].lower() not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)


# Create an instance of the Solution class
solution = Solution()

# Example input for testing
# input_string = "hello world"
input_string = "leetcode"

# Call the reverseVowels function
result = solution.reverseVowels(input_string)

# Print the result
print(result)
