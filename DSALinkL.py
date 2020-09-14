#DSA1002 -- CoronaVirus Simulation

"""Package Imports"""

import timeit
import sys
import random
import pickle

# global Variables
max_c = 100
spacer = "~~~~~~~~~~~~~~~~~~~~~"
node_remove = "Node Removal Complete"
node_insertion = "Node Insertion Complete"

""" Node Class """
class Node:

    """Constructor"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

"""Linked List Class"""
class LinkL:

    """Constructor"""
    def __init__(self):
        self.head = None

    def addPerson_start(self, new_data):
        """adds a new head node"""
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node
    
    def addPerson_end(self, new_data):
        """adds a new tail node"""
        new_node = Node(new_data)
        if self.head is None:
            self.head - new_node
            return
        
        tail = self.head
        while(tail.next):
            tail = tail.next
        tail.next = new_node
    

    def addPerson_inb(self, mid_node, new_data):
        """add a node inbetween existing nodes"""

        try:
            if mid_node is None:
                raise AttributeError

            new_node = Node(new_data)
            new_node.next = mid_node.next
            mid_node.next = new_node
        
        except AttributeError:
            print("middle person(node) requested is non-existant within linked list")
    

    def delete_person(self, remove_key):
        """Deletes node from linked list"""

        head_val = self.head

        if (head_val is not None):
            if (head_val.data == remove_key):
                self.head = head_val.next
                head_val = None
                return 
        
        while (head_val is not None):
            if head_val.data == remove_key:
                break
            prev = head_val
            head_val = head_val.next
        
        if (head_val == None):
            return
        
        prev.next = head_val.next

        head_val = None
    
    def getPerson(self, given_key):
        """Determines a persons existence within the linked list"""

        current_node = self.head

        while current_node != None:
            if current_node.data == given_key:
                return True
            
            current_node = current_node.next
        
        return False
    
    def size(self):
        """integer size of linked list"""

        return len(self.export())
    

    def isEmpty(self):
        """Determines if the linked list is empty or not"""

        if self.head is None:
            return True
        else:
            return False
    
        
    def export(self):
        """displays linked list as list to terminal"""
        
        array = []

        print_node = self.head
        while print_node is not None:
            array.append(print_node.data)
            print_node = print_node.next

        return array


if __name__ == "__main__":

    """Small Testing"""

    ll = LinkL()
    ll.head = Node("mary")
    e2 = Node("john")
    e3 = Node("susan")

    ll.head.next = e2
    e2.next = e3

    ll.addPerson_start("harold")
    ll.addPerson_inb(ll.head.next, "bob")
    ll.addPerson_end("don")
    ll.delete_person("john")
    print(ll.getPerson("mary"))

    print(ll.size())
    print(ll.isEmpty())

    print(ll.export())
            











    

    


