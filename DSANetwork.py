#DSA1002 -- Assignment Corona Virus SIR Model
#Curtin Campus
#DSANetwork.py -- Main file for SIR model 
#Shae Sullivan -- SID: 90016419

"""package imports"""

import sys
import csv
import math
import random
import time
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from DSALinkL import Node, LinkL
from DSAHashT import DSA_Hash_Table


""" network of population (social network) """
""" implemented via Graph Theory DS """

# *** global variables defined ***
spacer = "------------------"
loader = "Processing..."


class Network:
    """Social network class [top level class] superclass"""

    """constructor"""
    def __init__(self, social_network = None):
        if social_network == None: #if the social network values arent pre given
            social_network = {} #create empty social network 

        """private class parameter that allows social network to be accessed and manipulated by class methods"""
        self.__social_network__ = social_network


        self.population = 0 # total population [N of all linked lists combined]
        self.connections = 0 # total number of social connections within the network
        self.infected = LinkL() # infected person list
        self.suspectable = LinkL() # suspectable person list
        self.recovered = LinkL() # recovered person list
        self.dead = LinkL() # dead person list


        """Hash Table that holds personal data for individuals in social network"""
        """This is done by calling on (key) which == 'name' == person"""
        self.personal_record = DSA_Hash_Table()

        global spacer # terminal formatter
        global loader # terminal formatter
    

    def network_loader(self, filename):
        """Supports uploading of external pre formed networks"""
        """This method is built to open a csv file containing the network"""

        try:


            with open(filename, 'r', newline= '') as f:
                reader = csv.reader(f)
                for line in reader:
                    self.add_person(str(line[0]), line[1])
            
            for person in self.get_adjacent_people():
                current_person = person
                for neighbour in self.get_adjacent_people():
                    if neighbour == current_person:
                        continue
                    else:
                        self.add_connection({current_person, neighbour})


                        
        except FileNotFoundError:
            print("The requested file cannot be located in current search path")

  
    def add_person(self, person, info):
        """adds a individual person as a new node to the social network graph"""

        if person not in self.__social_network__:
            self.__social_network__[person] = []
            self.suspectable.addPerson_start(person)
            self.personal_record.put(str(person), str(info))
    
    def delete_person(self, person):
        """Deletes a individual person from the social network graph"""

        try:

            if self.has_person(person) == True:
                self.personal_record.remove(str(person))
                self.__social_network__.pop(str(person))
                if self.suspectable.getPerson(person) == True:
                    self.suspectable.delete_person(person)
                    return
                elif self.infected.getPerson(person) == True:
                    self.infected.delete_person(person)
                    return
                elif self.recovered.getPerson(person) == True:
                    self.recovered.delete_person(person)
                    return
                else:
                    raise ValueError
            else:
                raise ValueError

        except ValueError:
            print("Person Does not exist within the social network")
            return


    def get_person(self, person):
        """finds and returns person within social network"""

        try:
            if self.has_person(person) == True:
                if person in self.suspectable.export():
                    return person
                if person in self.infected.export():
                    return person
                if person in self.recovered.export():
                    return person
                else:
                    raise ValueError
            else:
                raise ValueError

        except ValueError:
            print("Person does not exist within network")
    
    def add_connection(self, edge):
        """adds a connection between two people as an edge of the social network graph"""

        edge = set(edge)

        (person1, person2) = tuple(edge)
        
        if person1 in self.__social_network__:
            self.__social_network__[person1].append(person2)
            return
        else:
            self.__social_network__[person1] = [person2]
            return
    
    def get_connection(self, person):
        """gets a persons connections within the social network"""

        try:
            if self.__social_network__ is not None:
                if self.has_person(person) == True:
                    return self.__social_network__[person]
                else:
                    raise ValueError
            else:
                raise ValueError

        except ValueError:
            print("ValueError! Either Network is Empty or Person does not reside within network")
    
    def delete_connection(self, person1, person2):

        """deleted connection one way in terms of the two people given to this method will no longer have connections to one another 
            but one may still have a solo connection to the other"""

        try:
            if self.has_person(person1) == True:
                if self.has_person(person2) ==  True:

                    for person in self.__social_network__[person1]:
                        if (person == person2):
                            self.__social_network__[person1].remove(person2)

                    for person in self.__social_network__[person2]:
                        if (person == person1):
                            self.__social_network__[person2].remove(person1)
                else:
                    raise ValueError
            else:
                raise ValueError

        except ValueError:
            print("one or both people within the connection do not exist")
            return

    def has_person(self, person):
        """determines if social network has person given"""

        person_set = set(self.get_adjacent_people())

        if person in person_set:
            return True
        else:
            return False

    def get_adjacent_people(self):
        """adjacency list of people"""

        return list(self.__social_network__.keys())
    
    def get_adjacent_connections(self):
        """adjacency list of connections"""

        return list(self.__edgeform__())
    
    def population_calc(self):
        """calculates population integer"""
        """people that have died to coronavirus within the network are removed from population count"""

        for person in self.get_adjacent_people():
            self.population += 1

        return self.population
    
    def connections_calc(self):
        """calculates number of edges within social network"""

        for edge in self.__edgeform__():
            self.connections += 1

        return self.connections
    
    def gender_search_f(self):
        """Calculates the number of females within social network"""

        n_females = 0

        for person in self.get_adjacent_people():
            for attribute in self.personal_record.get(person):
                if attribute == 'f':
                    n_females += 1
                    pass

        return n_females
    
    def gender_search_m(self):
        """Calculates the number of males withint the social network"""

        n_males = 0

        for person in self.get_adjacent_people():
            n_males += 1

        for person in self.get_adjacent_people():
            for attribute in self.personal_record.get(person):
                if attribute == 'f':
                    n_males -= 1
        
        return n_males
                    
    
    def __edgeform__(self):
        """forms edges(connections) for social network"""
        edges = []
        self.edge_array = []

        for person in self.__social_network__:
            for neighbour in self.__social_network__[person]:
                if {neighbour, person} not in edges:
                    edges.append({person, neighbour})
                    self.edge_array.append([person, neighbour])
        return edges

    
    def graph_visual(self):
        """visualization of social network via networkx graph being plotted via matplotlib.pylot"""

        visual = nx.MultiDiGraph()

        for person in self.__social_network__:
            visual.add_node(person)
            for neighbour in self.__social_network__[person]:
                visual.add_node(neighbour)
                visual.add_edge(person, neighbour)
        
        return visual


    def add_initial(self, person):
        """add first person"""

        if person not in self.infected.export():
            self.infected.addPerson_start(person)
        if person in self.suspectable.export():
            self.suspectable.delete_person(person)
        else:
            return

    def interact(self, person, tt, trans_rate, recov_rate, death_rate):
        """prompts an iteraction between two people within the social network"""
        """main method --> disease spread through social network"""

        """Real time edges --> needed incase of person insertion or deletion"""
        self.__edgeform__() #updates edges and accquires edge(conneciton) array

        """Stop section --> End Simulation when: a) everyone is infected, b) everyone is recovered, c) everyone is dead"""
        if self.infected.size() == self.population_calc():
            return
        if self.recovered.size() == self.population_calc():
            return
        if self.dead.size() == self.population_calc():
            return
        
        """if current day < total_days and infected Linked List is Empty Continue"""
        if int(tt) > 5:
            if self.infected.isEmpty() == True:
                return
            else:
                pass
        else:
            pass

        """Death Loop"""
        if np.random.randint(0, 100) <= death_rate * 100:
            if self.infected.isEmpty() == False:
                if int(tt) > 5:
                    dead_person = self.infected.export()[-1]
                    self.dead.addPerson_start(dead_person)
                    self.infected.delete_person(dead_person)
                    return
                else:
                    pass
            else:
                pass
        else:
            pass


        """Recovery Loop"""
        if np.random.randint(0, 100) <= recov_rate * 100:
            if self.infected.isEmpty() == False:
                if int(tt) > 5:
                    recovered_person = random.choice(self.infected.export())
                    self.recovered.addPerson_start(recovered_person)
                    self.infected.delete_person(recovered_person)
                    return
                else:
                    pass
            else:
                pass
        else:
            pass

        """selects a random connection between 2 people(vertexs) within the social network"""
        current_connection = list(random.choice(self.get_adjacent_connections()))

        """this while loop raises in simple terms "are both people in current connection infected?" If so: choose new conneciton"""
        """why this loop? Because this iteract method is purely made to give a chance of new infection occuring 
            within social network, therefore we dont want to select a connection in which both people are already infected"""

        while all(element in current_connection for element in self.infected.export()) == True:
            current_connection = list(random.choice(self.get_adjacent_connections()))
        else:
            """this while loop is quite similiat to the above loop, although it ensures that at least one of the people within the choosen connection
                is infected, Why? because if neither person in connection is infected, they have no chance of infecting one another"""

            while any(element in current_connection for element in self.infected.export()) == False:
                current_connection = list(random.choice(self.get_adjacent_connections()))

            else:

                """if method progresses onto this else statement, we have a current connection of 1 infected person and 1 non infected person"""

                print("Choosen Connection:  ", current_connection) #prints to terminal current connection
                infected_person = next(element for element in self.infected.export() if element in current_connection) #acquires the infected person(vertex) from current_connection
                current_connection.remove(infected_person) #removes this infected_person(vertex) from current_connection, leaving us with just non-infected person(vertex)
                if np.random.randint(0, 100) <= trans_rate * 100: #chance calculation in respect to transmission rate 
                    for item in current_connection: #looping through the only person in current_conneciton list now
                        if item not in self.infected.export(): #verifies this person is not in infected linked list 
                            if item not in self.recovered.export(): #verifies this person is not in recovered linked list
                                if item not in self.dead.export(): #verifies this person is not in dead linked list 
                                    self.infected.addPerson_start(str(item)) #adds person as head of infected linked list 
                                    self.suspectable.delete_person(item) #deletes person from suspectable linked list
                                    return
                                else:
                                    return
                            else:
                                return
                        else:
                            return
                else:
                    return
            

    def interaction_loop(self, person, times, trans_rate, recov_rate, death_rate):
        """runs iteract method on all current people within social network, once per time_step"""

        self.add_initial(person)

        for tt in range(0, times-1):

            self.interact(person, tt, trans_rate, recov_rate, death_rate)

            print("S:  ", self.suspectable.export(), self.suspectable.size())
            print("I:  ", self.infected.export(), self.infected.size())
            print("R:  ", self.recovered.export(), self.recovered.size())
            print("D:  ", self.dead.export(), self.dead.size())

            plt.pause(0.5)
            plt.title("Covid through social network")
            nx.draw_networkx(graph.graph_visual(), pos=nx.spring_layout(graph.graph_visual()), node_color = graph.color_set(), node_size=300, node_shape='s')
            plt.cla()
            plt.title("Covid through social network")
            nx.draw_networkx(graph.graph_visual(), pos=nx.spring_layout(graph.graph_visual()), node_color = graph.color_set(), node_size=300, node_shape='s')
            

    def color_set(self):
        """setting colors of nodes within networkx display"""

        self.color_map = [] #array of colours in respect to networkx nodes

        for node in self.graph_visual(): #color changing for networkx

            try:
                if str(node) in self.infected.export():
                    node = self.color_map.append('green')
                elif str(node) in self.suspectable.export():
                    node = self.color_map.append('yellow')
                elif str(node) in self.recovered.export():
                    node = self.color_map.append('blue')
                elif str(node) in self.dead.export():
                    node = self.color_map.append('grey')
                else:
                    raise ValueError
                
            except ValueError:
                pass

        return self.color_map
    
    def death_intervention(self, new_rate, death_rate):

        death_rate = new_rate

        return death_rate
    
    def recov_intervention(self, new_rate, recov_rate):

        recov_rate = new_rate

        return recov_rate
    
    def inf_intervention(self, new_rate, trans_rate):

        trans_rate = new_rate

        return trans_rate
            


"""MTH"""
if __name__ == '__main__':

    graph = Network()

    graph.add_person('mary', [58, 'female'])
    graph.add_person('john', [87, 'male'])
    graph.add_person('susan', [55, 'female'])
    graph.add_person('bob', [40, 'male'])
    graph.add_person('len', [19, 'male'])
    graph.add_person('mike', [45, 'male'])
    graph.add_person('don', [22, 'male'])
    graph.add_person('harold', [16, 'male'])
    graph.add_person('michelle', [43, 'female'])
    graph.add_person('logan', [24, 'male'])
    graph.add_person('julie', [44, 'female'])
    graph.add_person('harry', [67, 'male'])
    graph.add_person('isla', [66, 'female'])
    graph.add_person('sam', [8, 'male'])

    graph.add_connection({'john', 'susan'})
    graph.add_connection({'mary', 'bob'})
    graph.add_connection({'john', 'mary'})
    graph.add_connection({'susan', 'john'})
    graph.add_connection({'bob', 'mary'})
    graph.add_connection({'susan', 'bob'})
    graph.add_connection({'susan', 'mary'})
    graph.add_connection({'mary', 'john'})
    graph.add_connection({'john', 'bob'})
    graph.add_connection({'bob', 'susan'})
    graph.add_connection({'bob', 'john'})
    graph.add_connection({'mary', 'susan'})
    graph.add_connection({'john', 'susan'})
    graph.add_connection({'mary', 'bob'})
    graph.add_connection({'john', 'mary'})
    graph.add_connection({'susan', 'john'})
    graph.add_connection({'bob', 'mary'})
    graph.add_connection({'susan', 'bob'})
    graph.add_connection({'susan', 'mary'})
    graph.add_connection({'mary', 'john'})
    graph.add_connection({'john', 'bob'})
    graph.add_connection({'len', 'mary'})
    graph.add_connection({'harold', 'len'})
    graph.add_connection({'len', 'john'})
    graph.add_connection({'susan', 'len'})
    graph.add_connection({'mike', 'len'})
    graph.add_connection({'mike', 'mary'})
    graph.add_connection({'don', 'john'})
    graph.add_connection({'don', 'harold'})
    graph.add_connection({'len', 'mike'})
    graph.add_connection({'mary', 'don'})
    graph.add_connection({'susan', 'mike'})
    graph.add_connection({'john','harold'})
    graph.add_connection({'harold', 'bob'})
    graph.add_connection({'harold', 'mary'})
    graph.add_connection({'harold', 'susan'})
    graph.add_connection({'mary', 'michelle'})
    graph.add_connection({'michelle', 'mary'})
    graph.add_connection({'bob', 'michelle'})
    graph.add_connection({'susan', 'michelle'})
    graph.add_connection({'michelle', 'bob'})
    graph.add_connection({'michelle', 'susan'})
    graph.add_connection({'mary', 'logan'})
    graph.add_connection({'john', 'logan'})
    graph.add_connection({'susan', 'logan'})
    graph.add_connection({'logan', 'mary'})
    graph.add_connection({'logan', 'harold'})
    graph.add_connection({'julie', 'mary'})
    graph.add_connection({'bob', 'sam'})
    graph.add_connection({'sam', 'michelle'})
    graph.add_connection({'isla', 'bob'})
    graph.add_connection({'michelle', 'isla'})
    graph.add_connection({'mary', 'harry'})
    graph.add_connection({'harry', 'logan'})
    graph.add_connection({'susan', 'harry'})
    graph.add_connection({'julie', 'mary'})
    graph.add_connection({'logan', 'sam'})

    print(graph.get_adjacent_people())

    print(graph.gender_search_f())
    print(graph.gender_search_m())



    















    

    









