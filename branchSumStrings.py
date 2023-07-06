from typing import Optional

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sums = []
        self.calculateBranchSums(root, "", sums)
        return sum(int(branch) for branch in sums)
    
    def calculateBranchSums(self, node, runningSum, sums):
        if node is None:
            return
        newRunningSum = runningSum + str(node.val)
        if node.left is None and node.right is None:
            sums.append(newRunningSum)
            return
        self.calculateBranchSums(node.left, newRunningSum, sums)
        self.calculateBranchSums(node.right, newRunningSum, sums)


# Sample input for testing
root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

# Create an instance of the Solution class
solution = Solution()

# Call the sumNumbers function
result = solution.sumNumbers(root)

# Print the result
print(result)
