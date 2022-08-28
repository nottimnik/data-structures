class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head 

    #insert at the beginning of the linked lists 
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    #print the linked list
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + ' -> '
            itr = itr.next

        print(llstr)

    #insert at the end of the linked list
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return

        itr = self.head 

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    #create a linked list from a given array
    def insert_array(self, array):
        self.head = None 
        for i in array:
            self.insert_at_end(i) 

    #get the length of the linked list
    def get_length(self):
        length = 0
        itr = self.head
        while itr:
            length += 1
            itr = itr.next

        return length

    #remove a node from a specific index from the linked list
    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            count += 1
            itr = itr.next

    #insert a new node with a given value at a specific index in the linked list
    def insert_at(self, data, index):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            node = Node(data, self.head)
            self.head = node
        
        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break

            itr = itr.next
            count += 1

    #remove a given value from the linked list
    def remove_value(self, value):
        
        itr = self.head
        while itr:
            if itr.next.data == value:
                itr.next = itr.next.next

            itr = itr.next
