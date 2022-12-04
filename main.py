class linkedlist:
  def __init__(self):
    self.head=None
  def createhead(self,x):
    if self.head==None:
      node(x)
      self.head=node(x)
    else:
      current =node(x)
      current.next=self.head
      self.head=current
  def printlinkedlist(self):
    if self.head==None:
      print('there are 0 items in linked list')
    else:
      current=self.head
      while current!=None:
        print(current.value,'',end='')
        current=current.next
      print(' ')
      print('yours linked list printed')
  def createtail(self,x):
    if self.head==None:
      node(x)
      self.head=node(x)
    else:
      current=self.head
      while current.next!=None:
        current=current.next
      node(x)
      current.next=node(x)
  def length(self):
    if self.head==None:
      return 0
    else:
      current=self.head
      i=1
      while current.next !=None:
        i=i+1
        current=current.next
      return i
  def printlength(self):
    print(self.length())
  def inserting(self,x,i):
    if self.length()==1 or self.length==0:
      print('There are no items to insert between')
    else:
      if i<1 or i>(self.length()-1):
        print('u set incorrect index to insert item')
      else:
        current=self.head
        j=1
        while j!=i:
          current=current.next
          j=j+1
        new=node(x)
        new.next=current.next
        current.next=new
  def deletehead(self):
    if self.head==None:
      print('there are no items to delete')
    else:
      current=self.head
      self.head=current.next
      del current
  def deletetail(self):
    if self.head==None:
      print('there are no items to delete')
    else:
      if self.head.next==None:
        del self.head
      else:
        current=self.head
        while current.next.next!=None:
          current=current.next
        del current.next
        current.next=None
  def deleteindex(self,i):
    if self.head==None:
      print('there are no items to delete')
    elif i<1 or i>self.length():
      print('u set incorrect index')
    elif i==1:
      self.deletehead()
    elif i==self.length():
      self.deletetail()
    else:
      j=1
      current=self.head
      while j!=i-1:
        current=current.next
        j=j+1
      deleted=current.next
      current.next=deleted.next
      del deleted
  
class node:
  def __init__(self,a):
    self.value=a
    self.next=None
miwa=linkedlist()
miwa.createhead(3)
miwa.createhead(6)
miwa.createhead(5)
miwa.createtail(7)
miwa.inserting(8,3)
miwa.printlinkedlist()
miwa.printlength()
miwa.deletehead()
miwa.printlinkedlist()
miwa.deletetail()
miwa.printlinkedlist()
miwa.printlength()
miwa.createtail(10)
miwa.createtail(11)
miwa.createtail(12)
miwa.createtail(13)
miwa.printlinkedlist()
miwa.printlength()
miwa.deleteindex(6)
miwa.printlinkedlist()
  
  

        