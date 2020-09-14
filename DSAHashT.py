#DSA1002 --- CoronaVirus Simulation
#DSAHashT.py -- Hash Table Implementation for CoronaVirus Simulation
#Curtin Campus

"""package imports"""

import numpy as np
import copy
import random
import csv
import math
import time


"""Hash Table Class: Holds All Methods in respect to manipulating Hash Table"""
"""This Hash Table was heavily derived from my HashTable within Practical 7 submission"""

class DSA_Hash_Table(object):

    def __init__(self, count = 11):
        """ Contructor Variables """

        self.MAXLF = 0.75
        self.MINLF = 0.25
        self.min_count = count
        self.count = count
        self.items_total = 0
        self.hash_array = [None] * self.count
        self.hash_slots = [None] * self.count


    def hash(self, key):
        """ determines index value of hash_array for a specific key string """

        if isinstance(key, int):
            return key % self.count
        else:
            key_str = str(key)
            return sum([ord(character) for character in key_str]) % self.count
    
    def re_hash(self, prev_hash, count):
        """ re hashes a already hashed data item """

        return (prev_hash + 1) % count

    def put(self, key, value):
        """ add/put a value to our hash_array by its specific key"""

        key_hash = self.hash(key)
        key_val = [key, value]

        if self.hash_slots[key_hash] == None: # **data is new**
            self.hash_slots[key_hash] = key
            self.hash_array[key_hash] = value
            self.items_total += 1
            self.growth_check()

        else:
            if self.hash_slots[key_hash] == key:
                self.hash_array[key_hash] == value # **replacing current value**
            else:
                next_hslot = self.re_hash(key_hash, len(self.hash_slots))
                while self.hash_slots[next_hslot] != None and self.hash_slots[next_hslot] != key:
                    next_hslot = self.re_hash(next_hslot, len(self.hash_slots))
                
                if self.hash_slots[next_hslot] == None: # **data is new**
                    self.hash_slots[next_hslot] = key
                    self.hash_array[next_hslot] = value
                    self.items_total += 1
                    self.growth_check()
                else:
                    self.hash_array[next_hslot] = value # **replacing current value**


    def get(self, key):
        """ returns a value by its specific key"""

        key_start = self.hash(key)
        value = None
        end = False
        located = False
        position = key_start

        while self.hash_slots[position] != None and not located and not end:
            if self.hash_slots[position] == key:
                located = True
                value = self.hash_array[position]
            else:
                position = self.re_hash(position, len(self.hash_slots))
                if position == key_start:
                    end = True

        return value


    def remove(self, key):
        """ removes a hash table value by indexing via until given key matches existing key """

        key_hash = self.hash(key)

        if self.hash_slots[key_hash] is None:
            return False

        else:
            if self.hash_slots[key_hash] == key:
                self.hash_slots[key_hash] == None
                self.hash_array[key_hash] == None
                self.items_total -= 1
                self.shrink_check()
            else:
                next_hslot = self.re_hash(key_hash, len(self.hash_slots))
                while self.hash_slots[next_hslot] != None and self.hash_slots[next_hslot] != key:
                    next_hslot = self.re_hash(next_hslot, len(self.hash_slots))
                
                if self.hash_slots[next_hslot] == None:
                    return False
                else:
                    self.hash_slots[next_hslot] = None
                    self.hash_array[next_hslot] = None
                    self.items_total -= 1
                    self.shrink_check()
    
    def growth_check(self):
        """ checks if total items are greater than max load factor """

        if self.items_total > self.MAXLF * self.count:
            self.grow()
        else:
            pass
    
    def shrink_check(self):
        """ checks if total items is less than min load factor """

        if self.items_total < self.MINLF * self.count and self.count >= self.min_count * 2:
            self.shrink()
        else:
            pass
    
    def grow(self):
        """ resizes the hash table in respect to making it of greater size (growing) """
        
        new_count = 2 * self.count
        new_hash_table = DSA_Hash_Table(new_count)

        for key in self.hash_slots:
            if key != None:
                new_hash_table.put(key, self.get(key))
        
        self.count = new_count
        self.hash_slots = copy.deepcopy(new_hash_table.hash_slots)
        self.hash_array = copy.deepcopy(new_hash_table.hash_array)

        del new_hash_table # ** deletes newly made hash_table due to current hash_table values being updated**
    
    def shrink(self):
        """ resizes the hash table in respect to making it of smaller size (shrinking) """

        new_count = self.count // 2
        new_hash_table = DSA_Hash_Table(new_count)

        for key in self.hash_slots:
            if key != None:
                new_hash_table.put(key, self.get(key))
        
        self.count = new_count
        self.hash_slots = copy.deepcopy(new_hash_table.hash_slots)
        self.hash_array = copy.deepcopy(new_hash_table.hash_array)

        del new_hash_table # ** deletes newly made hash_table due to current hash_table values being updated**


    def keys(self):
        """ displays all current keys within hash table """

        key_array = []
        for key in range(0, len(self.hash_slots)):
            if self.hash_slots[key]:
                key_array.append(self.hash_slots[key])
        
        print("Current Keys: ")
        return key_array

    def get_load_factor(self):
        """ determines and returns how **under stress** the hash table is by determining
            how much of its max load is currently under load """

        items = self.items_total

        if self.hash_slots is not None:
            load = float(items / self.count) # **gives decimal of range 0 < load <= 1.0**
            print("Current Load: ", int(load * 100), "%")

            if load > self.MAXLF or load < self.MINLF:
                return True
            else:
                return False
        else:
            return None

    def export(self):
        """ displays to terminal current hash table contents """

        ht_array = []

        print("Current Hash Table Contents")
        for key in range(0, len(self.hash_slots)):
            if self.hash_slots[key]:
                if self.hash_array[key]:
                    element = (self.hash_slots[key], self.hash_array[key])
                    ht_array.append(element)
        
        return ht_array
    
    def is_prime(self, prime):
        """determines if value is prime """
        
        if prime <= 1:
            return False
        if prime <= 3:
            return True

        if (prime % 2 == 0 or prime % 3 == 0):
            return False

        for ii in range(5, int(math.sqrt(prime) + 1), 6):
            if(prime % ii == 0 or prime % (ii + 2) == 0):
                return False

        return True 

    
    def next_prime(self):
        """ finds next prime value larger than self.count and returns to terminal """

        if self.count <= 1:
            return 2
        
        prime = self.count
        located = False

        while (not located):
            prime += 1

            if (self.is_prime(prime) == True):
                located = True
        
        return "Next Prime of Count: " + str(prime)
   
    # methods to allow Hash_table[key] retrieval and assignment
    def __getitem__(self, key):
        """ gets (fetches) an item when user calls by hash_table["key"] method """

        return self.get(key)
    
    def __setitem__(self, key, value):
        """ sets (puts/adds) an item when user sets by hash_table["key"] = "value" method """

        self.put(key, value)


""" file i/o support method """

def file_io(filename):

    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            student_id = str(row[0])
            student_name = str(row[1])
            student_table.put(student_name, student_id)

            #with open("output.csv", 'w', newline='') as f: **optional code for saving to external file**
                #writer = csv.writer(f)
                #writer.writerow(student_table.export())


if __name__ == "__main__":

    hash_table = DSA_Hash_Table()

    hash_table.put('Bob', '4304-3333')
    hash_table.put('Ming', '293-6753')
    hash_table.put('Ming', '333-8233')
    hash_table.put('Ankit', '293-8625')  
    hash_table.put('Aditya', '852-6551')
    hash_table.put('Alicia', '632-4123')
    hash_table.put('Mike', '567-2188')
    hash_table.put('Aditya', '777-8888')
    hash_table.put('Len', '20202-1313')
    hash_table.remove('Bob')
    hash_table.remove('Alicia')


    """ File I/O driver code (coded to support CSV over other file types) """

    intiate = input(str("Would You Like To Open a File?:  "))

    if intiate == "Y" or intiate == "y" or intiate == "yes":

        student_table = DSA_Hash_Table()

        filename = input(str("Please input the file name: "))

        file_io(filename)

        """ Main Test Harness for File I/O functionality """

        print(student_table.export())
        print(student_table.keys())
        student_table.get_load_factor()

    else:
        pass