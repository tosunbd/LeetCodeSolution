class Solution(object):
    @staticmethod
    def reverseWords(s):
        words = s.strip().split()
        reverse = ' '.join(reversed(words))
        return reverse

# Example input sentence
input_sentence = "  the sky is blue  "

# Create an instance of the Solution class
solution = Solution()

# Call the reverseWords method
result = solution.reverseWords(input_sentence)

# Print the result
print(result)
