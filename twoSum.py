class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None or target is None:
            return []
        numIndices = [(num, index) for index, num in enumerate(nums)]
        numIndices.sort(key=lambda x: x[0])
        left = 0
        right = len(numIndices) - 1
        while left < right:
            currentSum = numIndices[left][0] + numIndices[right][0]
            
            if currentSum == target:
                return [numIndices[left][1], numIndices[right][1]]
            elif currentSum < target:
                left += 1
            else:
                right -= 1
        
        return []