from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    self.__list = Linked_List()

    '''
      This function is O(1). This is because it calls 
      the linked list constuctor which is also O(1) 
      and regardless, the deque will always start
      empty and the constructor will only run once.
      Therefore, this function is O(1).
    '''

  def __str__(self):
    return str(self.__list)

    '''
      This function is O(n^2). This is because, it 
      calls the Linked List str function which is 
      O(n^2), because it iterates the Linked List
      then has to iterate the string to concatinate
      the new values making it O(n^2).
    '''

  def __len__(self):
    return len(self.__list)
  
    '''
      This function is O(1). This is because, 
      this function calls the Linked List len
      function which is O(1), because it returns
      a pre-computed value and since that always
      takes the same number of steps it is O(1).
    '''
  
  # DO NOT CHANGE ANYTHING ABOVE THIS LINE
  
  def push_front(self, val):
    self.__list.append_element(val) if len(self.__list) == 0 else self.__list.insert_element_at(val, 0)

    '''
      This function is O(1). Since, this function always inserts 
      at the first value and that will take the same number of steps
      regardless of the size of the deque this function is O(1).
    '''
  
  def pop_front(self):
    if len(self) == 0:
      return
    return self.__list.remove_element_at(0)
  
    '''
      This function is O(1). Since, this function always pops 
      the first value and that will take the same number of steps
      regardless of the size of the deque this function is O(1).
    '''

  def peek_front(self):
    if len(self) == 0:
      return
    return self.__list.get_element_at(0)
  
    '''
      This function is O(1). Since, this function always return 
      the first value and that will take the same number of steps
      regardless of the size of the deque this function is O(1).
    '''

  def push_back(self, val):
    self.__list.append_element(val)

    '''
      This function is O(1). Since, this function always inserts 
      at the last value and that will take the same number of steps
      regardless of the size of the deque, since our linked list
      is doubly-linked. Therefore, this function is O(1).
    '''
  
  def pop_back(self):
    if len(self) == 0:
      return
    return self.__list.remove_element_at(len(self.__list)-1)
  
    '''
      This function is O(1). Since, this function always removes 
      the last value and that will take the same number of steps
      regardless of the size of the deque, since our linked list
      is doubly-linked. Therefore, this function is O(1).
    '''

  def peek_back(self):
    if len(self) == 0:
      return
    return self.__list.get_element_at(len(self.__list)-1)
  
    '''
      This function is O(1). Since, this function always returns 
      the last value and that will take the same number of steps
      regardless of the size of the deque, since our linked list
      is doubly-linked. Therefore, this function is O(1).
    '''

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
