from typing import Optional

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        currentNode = root
        while currentNode is not None:
            if val < currentNode.val:
                currentNode = currentNode.left
            elif val > currentNode.val:
                currentNode = currentNode.right
            else:
                return currentNode
        return None


# Sample input for testing
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

val = 5

# Create an instance of the Solution class
solution = Solution()

# Call the searchBST function
result = solution.searchBST(root, val)

# Print the result
if result is not None:
    print(result.val)
else:
    print([])  # Return an empty list if the desired value is not found
