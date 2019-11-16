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
    
    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        # Recursive Soltion just for the heck of it
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        """
        # Iterative Solution
        res = []
        stack = []
        done = True
        if root is None:
            return []
        curr = root
        while done:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                if len(stack) >0:
                    curr = stack.pop()
                    res.append(curr.val)
                    curr = curr.right
                else:
                    done = False
        return res
            