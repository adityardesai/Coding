import heapq

class MyObject(object):
  def __init__(self, val):
    self.val=val
  def __lt__(self, other):
    #return self.val > other.val # Descending order
    return self.val < other.val # Ascending order
  def __repr__(self):
    return str(self.val)

q = []
heapq.heappush(q, MyObject(50))
heapq.heappush(q, MyObject(40))
heapq.heappush(q, MyObject(30))
heapq.heappush(q, MyObject(20))
heapq.heappush(q, MyObject(200))
print(heapq.heappop(q))
print(heapq.heappop(q))
print(heapq.heappop(q))
print(heapq.heappop(q))
print(heapq.heappop(q))

#############################################################################################################

class MyStrObject(object):
  def __init__(self, val):
    self.val=val
  def __lt__(self, other):
    #return self.val > other.val # Descending order
    return self.val < other.val # Ascending order
  def __repr__(self):
    return str(self.val)

q = []
heapq.heappush(q, MyStrObject('a'))
heapq.heappush(q, MyStrObject('x'))
heapq.heappush(q, MyStrObject('aab'))
heapq.heappush(q, MyStrObject('aac'))
heapq.heappush(q, MyStrObject('aad'))
print(heapq.heappop(q))
print(heapq.heappop(q))
print(heapq.heappop(q))
print(heapq.heappop(q))
print(heapq.heappop(q))
