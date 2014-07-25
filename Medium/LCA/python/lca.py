import sys

class Node:
 
      def __init__(self,info): #constructor of class
 
          self.info = info  #information for node
          self.left = None  #left leef
          self.right = None #right leef
          self.level = None #level none defined
 
      def __str__(self):
 
          return str(self.info) #return as string
 
 
class searchtree:
 
      def __init__(self): #constructor of class
 
          self.root = None
 
 
      def create(self,val):  #create binary search tree nodes
 
          if self.root == None:
 
             self.root = Node(val)
 
          else:
 
             current = self.root
 
             while 1:
 
                 if val < current.info:
 
                   if current.left:
                      current = current.left
                   else:
                      current.left = Node(val)
                      break;      
 
                 elif val > current.info:
                 
                    if current.right:
                       current = current.right
                    else:
                       current.right = Node(val)
                       break;      
 
                 else:
                    break   
      
      def lca(self, node, a, b):
        if (a.info < node.info and b.info > node.info) or (a.info > node.info and b.info < node.info):
          return node.info
        elif a.info < node.info:
          node = node.left
        elif a.info > node.info:
          node = node.right


                        
tree = searchtree()
arr = [30,8,52,3,20,10,29]
for i in arr:
    tree.create(i)


with open(sys.argv[1], 'r') as input:
  test_cases = input.read().strip().splitlines()

for test in test_cases:     
  if len(test) == 0:
    continue

  alpha, beta = test.split(" ")
  alpha, beta = int(alpha), int(beta)
  
  a = Node(alpha)
  b = Node(beta)

  print (tree.lca(tree.root, a, b))
