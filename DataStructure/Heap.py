
# coding: utf-8

# We would like to implement heap just insertaion function

# In[5]:



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

  def heapsort(self):
    a=self.pointer
    a=a-1
    #print("salam", a)
    while (a > 0):
      #print(a)
      temp=self.heap[0]
      self.heap[0]=self.heap[a]
      self.heap[a]=temp
      k=1
      j=0
      i=0
      print(self.heap, "bbb")
      while (k==1):
        if(self.heap[j] < self.heap [2*j+1] and self.heap[2*j+1] >= self.heap[2*j+2] and j<(a-1)/2):
          self.swap(j, 2*j+1)
          j=2*j+1
        elif(self.heap[j] < self.heap [2*j+2] and self.heap[2*j+2] >= self.heap[2*j+1] and j<(a-2)/2):
          self.swap(j, 2*j+2)
          j=2*j+2
        else:
          k=0
        print(self.heap, "aaaa")
        i=i+1
      if(a==1):
        if(self.heap[0] > self.heap[1]):
          self.swap(0,1)
      a=a-1
      j=0
    
  
  
  

h=Heap()
h.insert(10)
h.insert(-20)
h.insert(0)
h.insert(2)
#h.insert(210)
h.show()
h.heapsort()
h.show()
    


# In[ ]:



