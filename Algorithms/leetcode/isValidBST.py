# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return checkNode(root, -9999, -9999)
        
        
def checkNode(node: TreeNode, min: int, max: int) -> bool:
    if node is None:
        return True
    if node.val >= min and node.val <= max:
        return False
    
    return checkNode(node.right, min, node.val) and checkNode(node.left, node.val, max)