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

def lca(root, v1, v2):
    v1root = findPointer(root, v1)
    v2root = findPointer(root, v2)
    common = []
    for item in v1root:
        if item in v2root:
            common.append(item)
    ret = Node(common.pop())
    return ret
    
  #Enter your code here

def findPointer(node, val):
    cur = node
    roots = []
    while True:
        roots.append(cur.info)
        if cur.info < val:
            cur = cur.right
        elif cur.info > val:
            cur = cur.left
        elif cur.info == val:
            return roots

tree = BinarySearchTree()
t = int(8)

arr = [8,4,9,1,2,3,6,5]

for i in range(t):
    tree.create(arr[i])

v = [1,2]

ans = lca(tree.root, v[0], v[1])
print (ans.info)
