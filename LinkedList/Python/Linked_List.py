class Linked_List:
    
    class __Node:
        
        def __init__(self, val):

            '''
                This function is O(1), because when called the constructor is called and its a constant number of step every time.
                Thus, this function is O(1) since it will always have the same number of step when called for a linked list.
            '''

            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation

        '''
            This function is O(1), because when called the constructor is called and its a constant number of step every time.
            Thus, this function is O(1) since it will always have the same number of step when called for a linked list.
        '''

        self.__header = Linked_List.__Node(None)
        self.__trailer = Linked_List.__Node(None)
        self.__size = 0

        self.__header.next = self.__trailer
        self.__header.prev = self.__header

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation

        '''
            This function is O(1), because wehn called it returns the atribute size to the caller.
            Since its returning an already computed value it will always take 1 step to run.
        '''

        return self.__size

    def __get_current_node(self, index):

        '''
            This function is O(n), because at a worst case scenario it will have to walk the 
            length of the list to reach the node to return.
        '''

        if self.__size-index >= self.__size/2:
            current = self.__header
            for _ in range(1,index+1):
                current = current.next
        else:
            current = self.__trailer
            for _ in range(0, self.__size-index+1):
                current = current.prev

        return current

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation

        '''
            This function is O(1), because regardless of the size of the list it 
            will always have to move the same distance to get to the node need
            to do the appending operation. This means that the function will
            operate in constant time regardless of the size of the list
            making it O(1).
        '''

        new_node = self.__Node(val)
        if self.__size == 0:
            self.__header.next = new_node
            self.__trailer.prev = new_node
            new_node.next = self.__trailer
            new_node.prev = self.__header
        else:
            new_node.next = self.__trailer
            new_node.prev = self.__trailer.prev
            self.__trailer.prev.next = new_node
            self.__trailer.prev = new_node
        self.__size += 1

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation

        '''
            This function is O(n), because in a worst case senerio it would 
            have to walk the length of the list to reach the postion to do
            the insertion operation. Since the process of added the node is
            constant this function is O(n), because it take linear time
            to reach the node to do the insertion.
        '''

        if index >= self.__size or index < 0:
            raise IndexError
        
        new_node = self.__Node(val)
        if self.__size-index >= self.__size/2:
            current = self.__header
            for _ in range(1,index+1):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
        else:
            current = self.__trailer
            for _ in range(0, self.__size-index):
                current = current.prev
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node

        self.__size += 1 
        
    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation

        '''
            This function is O(n), because in its worst case senario this function
            would have to walk the entire length of the list to reach the node that
            is being removed. Therefore, this function is O(n).
        '''

        if index >= self.__size or index < 0:
            raise IndexError

        if index == self.__size - 1:
            current = self.__get_current_node(index)
            deletedValue = current.next.val
            current.next = current.next.next
            self.__trailer.prev = current
        else:
            current = self.__get_current_node(index)
            deletedValue = current.next.val
            current.next = current.next.next
            current.next.prev = current
        self.__size -= 1

        return deletedValue

    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation

        '''
            This function is O(n), because in a worst case senario this function
            would have to walk the length of the list in order to get the value
            that the caller is trying to retrieve. Therefore, this would make
            this function O(n).
        '''

        if index+1 > self.__size or index < 0:
            raise IndexError
        
        current = self.__get_current_node(index+1)
        return current.val


    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.

        '''
            This function is O(1), because the called remove function is
            O(1) for remove an element at the front of the list since 
            the same distance has to be traveled every time grab and remove
            that index. Then the append function is also O(1), therefore, 
            this rotate left function is O(1) since it will always take
            the same number of steps to complete.
        '''

        if self.__size <= 0:
            return
        node_to_rotate = self.remove_element_at(0)
        self.append_element(node_to_rotate)
        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation

        '''
            This fuction is O(n), because it need to walk the list once 
            to get all the element of the list in order to return the 
            desired string. Since element indexing and string concatination
            are O(1) in python, then this function is O(n) since the only thing
            that needs to happen is for the function to walk the list.
        '''

        if self.__size == 0:
            return "[ ]"
        
        current = self.__header
        contents = "["
        while current.next is not self.__trailer:
            current = current.next
            contents += f" {current.val},"
        return f"{contents[:-1]} ]"

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.

        '''
            This function is O(1), because it is constant time to initalize a
            variable to a pre-existing varible. Also, it only get initalized
            once, therefore, it always takes the same number of steps always
            making it O(1).
        '''

        self.__iter_node = self.__header
        return self

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation

        '''
            This function is O(1), because it is constant time to initalize a
            variable to a pre-existing varible. Also, it only get initalized
            once, therefore, it always takes the same number of steps always
            making it O(1).
        '''

        if self.__iter_node.next is self.__trailer:
            raise StopIteration
        

        self.__iter_node = self.__iter_node.next
        return self.__iter_node.val


    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.

        '''
            This function is O(n), because the list has to get walked once
            in order to get all the values to be reversed. Since it appends 
            on each element and appending is O(1), then this reversed function
            is O(n).
        '''

        reversedLinkedList = Linked_List()
        if self.__size == 0:
            return reversedLinkedList
        
        current = self.__trailer
        while current.prev is not self.__header:
            current = current.prev
            reversedLinkedList.append_element(current.val)
        return reversedLinkedList

if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from head to tail? Does a for loop
    # iterate through your reversed list from tail to head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests
    linkedList = Linked_List()
    emptyLinkedList = Linked_List()

    #Testing Append Function 
    print("______________Testing append function:______________\n")
    print("Appending Value 1: ")
    try:
        linkedList.append_element(1)
    except:
        print("Error: Failed to append value")
    print(linkedList)
    print(f"Size: {len(linkedList)}\n")


    print("Appending Value 2: ")
    try:
        linkedList.append_element(2)
    except:
        print("Error: Failed to append value")
    print(linkedList)
    print(f"Size: {len(linkedList)}\n")

    print("Appending Value 3: ")
    try:
        linkedList.append_element(3)
    except:
        print("Error: Failed to append value")
    print(linkedList)
    print(f"Size: {len(linkedList)}\n")

    print("Appending Value 4: ")
    try:
        linkedList.append_element(4)
    except:
        print("Error: Failed to append value")
    print(linkedList)
    print(f"Size: {len(linkedList)}\n")

    #Testing insert element function
    print("______________Testing insert_element_at function:______________\n")
    try:
        print("Inserting Value: 5 at Index: 0")
        linkedList.insert_element_at(5, 0)
    except IndexError:
        print("Error: Index out of bounds")
    print(linkedList)
    print(f"Size: {len(linkedList)}\n")
    
    try:
        print("Inserting Value: 6 at Index: 10")
        linkedList.insert_element_at(6,10)
    except IndexError:
        print("Error: Index out of bounds")
    print(linkedList)
    print(f"Size: {len(linkedList)}\n")

    try:
        print("Inserting Value: 5 at Index: -1")
        linkedList.insert_element_at(5,-1)
    except IndexError:
        print("Error: Index out of bound (Negative Index)")
    print(linkedList)
    print(f"Size: {len(linkedList)}\n")

    try:
        print("Inserting Value: 6 at Index: last")
        linkedList.insert_element_at(6,len(linkedList))
    except IndexError:
        print("Error: Can't insert at tail")
    print(linkedList)
    print(f"Size: {len(linkedList)}\n")

    try:
        print("Testing 2 appends followed by an insert at index 1")
        testList = Linked_List()
        testList.append_element("One")
        testList.append_element("Three")
        testList.insert_element_at("Two", 1)
        print(testList)
        print(f"Size: {len(testList)}\n")
    except IndexError:
        print("Error: Failed to insert at index 1")



    #Testing remove element function
    print("______________Testing remove_element_at function:______________\n")
    print("Removing element at index 0")
    try:
        print(linkedList.remove_element_at(0))
    except IndexError:
        print("Error: Index out of bounds")
    print(linkedList)
    print(f"Size: {len(linkedList)}\n")

    print("Removing element at index -1")
    try:
        linkedList.remove_element_at(-1)
    except IndexError:
        print("Error: Index out of bounds (Negative Index)")
    print(linkedList)
    print(f"Size: {len(linkedList)}\n")

    print("Removing element at last index")
    try:
        print(linkedList.remove_element_at(len(linkedList)-1))
    except IndexError:
        print("Error: Index out of bounds")
    print(linkedList)
    print(f"Size: {len(linkedList)}\n")

    print("Removing element from empty list:")
    try:
        emptyLinkedList.remove_element_at(1)
    except:
        print("Error: Index out of bounds (Empty List)\n")

    try:
        print("Testing 2 appends followed by an insert at\nindex 1 followed by remove at index 1")
        testList = Linked_List()
        testList.append_element("One")
        testList.append_element("Three")
        testList.insert_element_at("Two", 1)
        print(testList.remove_element_at(1))
        print(testList)
        print(f"Size: {len(testList)}\n")
    except IndexError:
        print("Error: Failed to insert at index 1")


    print("______________Testing get_element_at function:______________\n")
    print("Getting element at index 0")
    try:
        print(f"Element at index 0: {linkedList.get_element_at(0)}\n")
    except IndexError:
        print("Error: Index out of bounds\n")

    print("Getting element at index -1")
    try:
        print(f"Element at index -1: {linkedList.get_element_at(-1)}\n")
    except IndexError:
        print("Error: Index out of bounds (Negative Index)\n")

    print("Getting element at index 10")
    try:
        print(f"Element at index 10: {linkedList.get_element_at(10)}\n")
    except IndexError:
        print("Error: Index out of bounds\n")

    print("Getting element from empty list:\n")
    try:
        print(f"Element at index 0 {emptyLinkedList.get_element_at(0)}")
    except IndexError:
        print("Error: Index out of bounds (Empty List)")

    print("______________Testing rotate_left function:______________\n")
    print("Rotating linkedList left:")
    try:
        linkedList.rotate_left()
    except:
        print("Error: Failed to rotate list left")
    print(linkedList)
    print(f"Size: {len(linkedList)}\n")

    print("Rotating emptyList left:")
    try:
        emptyLinkedList.rotate_left()
    except:
        print("Error: Failed to rotate empty list left")
    print(emptyLinkedList)
    print(f"Size: {len(emptyLinkedList)}\n")

    print("Rotating list of length 1:")
    try:
        oneList = Linked_List()
        oneList.append_element(1)
        oneList.rotate_left()
    except:
        print("Error: Failed to rotate list of length 1 left")
    print(oneList)
    print(f"Size: {len(oneList)}\n")


    print("______________Testing reversed function:______________\n")
    print(f"Reversed linked list:\n{reversed(linkedList)}\n")

    try:
        print(f"Reversed empty list:\n{reversed(emptyLinkedList)}\n")
    except:
        print("Error: Failed to rotate empty list")

    print("Reversed List Interated:")
    for val in reversed(linkedList):
        print(str(val))

    print("______________Testing iterator function:______________\n")
    print("Iterating over linkedList:")
    try:
        for val in linkedList:
            print(str(val))
    except:
        print("Error: Failed to iterate over list")

    print("Iterating over emptyList:")
    try:
        for val in emptyLinkedList:
            print(str(val))
    except:
        print("Error: Failed to iterate over empty list")