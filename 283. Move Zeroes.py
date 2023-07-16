from typing import List

def pop_and_push_zeros(nums):
    i = 0
    count = nums.count(0)

    while count > 0:
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
            count -= 1
        else:
            i += 1
    return nums



# Create an instance of the Solution class
# Example input for testing
nums = [0,1,0,3,12]

# Call the pop_and_push_zeros function
result = pop_and_push_zeros(nums)

# Print the result
print(result)
