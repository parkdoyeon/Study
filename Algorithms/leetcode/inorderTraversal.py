# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 중위순회: 왼->중->오

class Solution:
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []
        self._inorderTraversal(root, answer)
        return answer
        
    def _inorderTraversal(self, node: TreeNode, ans: List[int]) -> None:
        if node is None:
            pass
        else:
            self._inorderTraversal(node.left, ans)
            ans.append(node.val)
            self._inorderTraversal(node.right, ans)