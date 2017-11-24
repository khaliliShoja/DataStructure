
# coding: utf-8

# We would like to implement heap just insertaion function

# In[3]:


class Heap:
  HEAP_SIZE=10
  def __init__(self):
    self.heap=[0]*self.HEAP_SIZE
    self.pointer=0
  def insert(self, data):
    self.heap[self.pointer]=data
    a=self.pointer
    b=a//2
    k=1
    while (k==1):
      if(self.heap[b] < self.heap[a]):
        self.swap(b,a)
        a=b
        b=a//2
      else:
        k=0
    self.pointer=self.pointer+1    
  def swap(self, b,a):
    temp=self.heap[b]
    self.heap[b]=self.heap[a]
    self.heap[a]=temp
  def show(self):
    print(self.heap)
h=Heap()
h.insert(23)
h.insert(5)
h.insert(100)
h.insert(2)
h.insert(210)
h.show()
          
    


# In[ ]:



