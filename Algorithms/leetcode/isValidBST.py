# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return checkNode(root, -math.inf, math.inf)
        
        
def checkNode(node: TreeNode, min: int, max: int) -> bool:
    if node is None:
        return True
    if node.val <= min or node.val >= max:
        return False
    
    return checkNode(node.right, node.val, max) and checkNode(node.left, min, node.val)