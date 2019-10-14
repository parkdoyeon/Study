
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
# 내 코드
def height(root):
    leftheight = 0
    rightheight = 0
    lnode = root
    rnode = root
    while True:
        if lnode.left :
            leftheight += 1
            lnode = lnode.left
        elif lnode.right:
            leftheight += 1
            lnode = lnode.right
        else:
            break
    while True:
        if rnode.right:
            rightheight += 1
            rnode = rnode.right
        elif rnode.left:
            rightheight += 1
            rnode = rnode.left
        else:
            break
    return leftheight if leftheight > rightheight else rightheight
        
            
# 좋은코드!
def height(root):
    if root:
        return 1 + max(height(root.left), height(root.right))
    else:
        return -1