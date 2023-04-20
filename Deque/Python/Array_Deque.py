from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__front = None
    self.__back = None
    self.__size = 0

    '''
      This function is O(1). This because it would only get called
      for an object and it would take the same number of steps each
      time do to assigment operations taking constant time.
    '''
    
  def __str__(self):
    if len(self) == 0:
      return "[ ]"
    contents = "["
    for element in range(len(self)):
      contents += f" {self.__contents[(self.__front+element)%self.__capacity]},"
    return f"{contents[:-1]} ]"
  
    '''
      This function is O(n^2). This is because, in the worst case
      scenario this function would have to iterate the the entire
      length of the deque then the function would have to iterate 
      the entire sting in order to concatinate the new element.
      For these two reasons, since the string and deque have to 
      be interated this function is O(n^2).
    '''

    
  def __len__(self):
    return self.__size
  
    '''
      This function is O(1). This is, because regardless of the size 
      of the deque we are returning a precomputed value, therefore, 
      this works in constant time, meaning this function is O(1).
    '''

  def __grow(self):
    new_Deque = [None] * (self.__capacity * 2)
    new_Deque_size = 0
    for index in range(len(self)):
      new_Deque[index] = self.pop_front()
      new_Deque_size += 1
    
    self.__size = new_Deque_size
    self.__front = 0
    self.__back = new_Deque_size-1
    self.__capacity *= 2
    self.__contents = new_Deque

    '''
      This function is O(n). This because, in any case the function 
      would have to iterate the entire deque in order to copy it over.
      Since, the pop_front function operates in constant time it has no
      extra effects making this function O(n).
    '''

  def __push_empty(self, val):
    self.__front = 0
    self.__back = 0
    self.__contents[self.__front] = val
    self.__size += 1

    '''
      This function is O(1). This is, because the function is always
      inserting on a empty deque which is the same every time, therefore
      it takes the same number of instructions and thus the function 
      is O(1).
    '''
    
  def push_front(self, val):
    if self.__front == None:
      self.__push_empty(val)
      return
    if len(self) == self.__capacity:
      self.__grow()
    self.__front = (self.__front - 1 + self.__capacity) % self.__capacity
    self.__contents[self.__front] = val
    self.__size += 1

    '''
      This function is O(n). This is because pushing to the front would
      be constant time since assignment and math operations are constant
      time and in the worst case the grow function would 
      be called which is O(n), therefore, this function is O(n).
    '''

    
  def pop_front(self):
    if len(self) == 0:
      return
    val = self.__contents[self.__front]
    self.__front = (self.__front + 1) % self.__capacity
    self.__size -= 1
    return val
  
    '''
      This function is O(1). Since, array lookups are constant time
      and front is already computed this function would always
      take the same number of steps making it O(1).
    '''
    
  def peek_front(self):
    if len(self) != 0:
      return self.__contents[self.__front]
    
    '''
      This function is O(1). Since, array lookups are constant time
      and front is already computed this function would always
      take the same number of steps making it O(1).
    '''
    
  def push_back(self, val):
    if self.__back == None:
      self.__push_empty(val)
      return
    if len(self) == self.__capacity:
      self.__grow()
    self.__back = (self.__back + 1) % self.__capacity
    self.__contents[self.__back] = val
    self.__size += 1

    '''
      This function is O(n). This is because pushing to the back would
      be constant time since assignment and math operations are constant
      time and in the worst case the grow function would 
      be called which is O(n), therefore, this function is O(n).
    '''
  
  def pop_back(self):
    if len(self) == 0:
      return
    val = self.__contents[self.__back]
    self.__back = (self.__back - 1 + self.__capacity) % self.__capacity
    self.__size -= 1
    return val
  
    '''
      This function is O(1). Since, array lookups are constant time
      and back is already computed this function would always
      take the same number of steps making it O(1).
    '''

  def peek_back(self):
    if len(self):
      return self.__contents[self.__back]
    
    '''
      This function is O(1). Since, array lookups are constant time
      and back is already computed this function would always
      take the same number of steps making it O(1).
    '''

# No main section is necessary. Unit tests take its place.
# if __name__ == '__main__':
  # pass
    