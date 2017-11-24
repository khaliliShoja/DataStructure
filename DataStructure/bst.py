
# coding: utf-8

# BST

# In[1]:

class Node:
  def __init__(self, data):
    self.data=data
    self.leftChild=None
    self.rightChild=None
    
class BinarySearchTree:
  def __init__(self):
    self.root=None
  def insert(self, data):
    node=Node(data)
    if(self.root==None):
      self.root=node
    else:
      self.insertNode(self.root, data)
  
  def insertNode(self, node1, data):
    node=Node(data)
    if(data < node1.data):
      if(node1.leftChild==None):
        node1.leftChild=node
      else:
        self.insertNode(node1.leftChild, data) #Note that self is needed
    else:
      if(node1.rightChild==None):
        node1.rightChild=node
      else:
        self.insertNode(node1.rightChild, data)
  
  
  def findMinMaster(self):
    node=self.root
    a=self.findMin(node)
    return a
  def findMin(self,node):
    if(node.leftChild==None):
      return node.data
    else:
      b=self.findMin(node.leftChild)
    return b
  def traversein(self):
    if(self.root==None):
      return 
    else:
      a=self.traverse(self.root, [])
    return a  
  def traverse(self, node1, l):
    if(node1==None):
      return 
   
    if(node1.leftChild!=None):
      self.traverse(node1.leftChild,l)
    print(node1.data)
    l.append(node1.data)
    if(node1.rightChild!=None):
      self.traverse(node1.rightChild,l)
    return l
bst=BinarySearchTree()
bst.insert(10)
bst.insert(13)
bst.insert(5)
bst.insert(14)


#a=bst.findMinMaster()
#print(a)
a=bst.traversein()



print(a)



    
        
        
      


# In[ ]:



