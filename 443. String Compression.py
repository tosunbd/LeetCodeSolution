from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        cnt = 0
        c = 1        
        for i in range(1, n):
            if chars[i] == chars[i-1]:
                c += 1
            else:
                chars[cnt] = chars[i-1]
                cnt += 1
                
                if c > 1:
                    for char in str(c):
                        chars[cnt] = char
                        cnt += 1                
                c = 1
        chars[cnt] = chars[n-1]
        cnt += 1        
        if c > 1:
            for char in str(c):
                chars[cnt] = char
                cnt += 1
        
        return cnt
    
    # def compress(self, chars: List[str]) -> int:
    #     dictionary=[]
    #     c=1
    #     for i in range(1,len(chars)):
    #         if chars[i]==chars[i-1]:
    #             c+=1
    #         else:              
    #             dictionary.append([chars[i-1],c])
    #             c=1              
    #     dictionary.append([chars[-1],c])
    #     cnt=0
    #     for key,value in dictionary:
    #         chars[cnt]=key
    #         cnt += 1
    #         if value>1:
    #             for char in str(value):
    #                 chars[cnt]=str(char)
    #                 cnt += 1
    #     return cnt

# Sample input for testing
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

# Create an instance of the Solution class
solution = Solution()

# Call the canPlaceFlowers function
result = solution.compress(chars)

# Print the result
print(result)
