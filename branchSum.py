from typing import Optional

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sums = []
        self.calculateBranchSums(root, 0, sums)
        return targetSum in sums
    
    def calculateBranchSums(self, node, runningSum, sums):
        if node is None:
            return
        newRunningSum = runningSum + node.val
        if node.left is None and node.right is None:
            sums.append(newRunningSum)
            return
        self.calculateBranchSums(node.left, newRunningSum, sums)
        self.calculateBranchSums(node.right, newRunningSum, sums)


# Sample input for testing
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

targetSum = 22

# Create an instance of the Solution class
solution = Solution()

# Call the hasPathSum function
result = solution.hasPathSum(root, targetSum)

# Print the result
print(result)
