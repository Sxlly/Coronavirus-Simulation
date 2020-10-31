#DSA1002 -- CoronaVirus Simulation
#CVSimulationGUI.py -- GUI Codebase
#Shae Sullivan -- 90016419
#Curtin Campus

import sys
import csv
import time
import tkinter as tk
import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure 
from matplotlib import style
from DSANetwork import Network
from DSALinkL import Node, LinkL
from DSAHashT import DSA_Hash_Table

""" Creating Social Network """
""" Calling on Network SuperClass [all methods in chain are of NetworkClass] """
""" Network Top Level Class Associates: DSA_Linked_List, DSA_Hash_Table """
""" network setter --> MAIN DRIVER for social network"""
"""Interactive menu Main"""
"""GUI build"""

matplotlib.use('TkAgg')
style.use("ggplot")


LARGE_FONT = ("Courier", 14)
QUICK_FONT = ("Times", 12)
style.use("ggplot")

HEIGHT = 25
WIDTH = 60

"""declaring network variable"""
graph = Network()

class interactive_menu(tk.Tk, Network):


    global HEIGHT
    global WIDTH

    """Interactive menu class"""
    """Inherits from Network class"""

    def __init__(self, *args, **kwargs):
        self.graph = Network()

        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Covid')
        self.geometry("800x650")
        self.resizable(0,0)
        self.list = tk.Listbox(self)

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for f in (LaunchPage, StartPage, PageOne, PageTwo, PageThree):

            frame = f(container, self)

            self.frames[f] = frame

            frame.grid(row = 0, column = 0, sticky="nsew")

        self.show_frame(LaunchPage)
    
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class LaunchPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image = Image.open("CVBGUI.gif")
        self.img_cp = self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image = self.background_image)
        self.background.pack(fill = BOTH, expand = YES)
        label = tk.Label(self, text= "CoronaVirus Social Network Spread Simulator", font= LARGE_FONT)
        label.place(x = 165, y = 250)

        filename_input = tk.Text(self, height = 2, width = 35, bg= "light pink")
        open_command = tk.Button(self, text= "Open", command=lambda: self.load_network(filename_input, controller), fg= "black", bg= "green", height= 2, width = 10)

        button1 = ttk.Button(self, text="Load Network", command=lambda: self.load_network_prompt(filename_input, open_command))
        button1.place(x = 350, y = 335)

        button2 = ttk.Button(self, text= "Use Demo Network", command=lambda: self.demo_network(controller))
        button2.place(x = 335, y = 400)


    def load_network_prompt(self, filename_input, open_command):

        filename_input.place(x = 245, y = 500)
        open_command.place(x = 345, y = 580) 

    def load_network(self, filename_input, controller):

        filename = str(filename_input.get("1.0", "end-1c"))

        try:

            graph.network_loader(filename)

            controller.show_frame(StartPage)

            return

        except FileNotFoundError:

            print("This file was not found in the current search path")
            return
    
    def demo_network(self, controller):
        
        try:

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

            controller.show_frame(StartPage)

            return

        except ValueError:
            print("An Error Occured :( ")
            return


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image = Image.open("CVBGUI.gif")
        self.img_cp = self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image = self.background_image)
        self.background.pack(fill = BOTH, expand = YES)

        label = tk.Label(self, text="Main Menu", font=LARGE_FONT)
        label.place(x = 350, y = 50)

        button1 = ttk.Button(self, text="Person Add/Deletion Support", command=lambda: controller.show_frame(PageOne)) 
        button1.place(x = 320, y = 100)

        button2 = ttk.Button(self, text="Statistics", command=lambda: controller.show_frame(PageTwo)) 
        button2.place(x = 360, y = 150)

        button3 = ttk.Button(self, text="Simulate Support", command=lambda: controller.show_frame(PageThree)) 
        button3.place(x = 348, y = 200)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image = Image.open("CVBGUI.gif")
        self.img_cp = self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image = self.background_image)
        self.background.pack(fill = BOTH, expand = YES)
        label = tk.Label(self, text="Person Add/Deletion Support", font=LARGE_FONT)
        label.place(x=250, y=50)
        self.pr = tk.Listbox(self, height = 20, width = 35, font = QUICK_FONT)

        pr_text = tk.Label(self, text="Personal Records", font = LARGE_FONT)

        person_input = tk.Text(self, height = 2, width = 35, bg= 'light green')
        age_input = tk.Text(self, height = 2, width = 15, bg = 'light green')

        person1_connection = tk.Text(self, height = 2, width = 35, bg = 'light green')
        person2_connection = tk.Text(self, height = 2, width = 35, bg = 'light green')

        button1 = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(StartPage)) 
        button1.place(x = 345, y = 75)

        button2 = ttk.Button(self, text="Statistics", command=lambda: controller.show_frame(PageTwo)) 
        button2.place(x = 360, y = 100)

        button3  = ttk.Button(self, text="Add Person", command=lambda: self.addition_person(person_input, age_input, add_commmand, delete_command, find_command, person1_connection, person2_connection, add_connection_command, del_connection_command))
        button3.place(x = 360, y = 125)

        button7 = ttk.Button(self, text="Find Person", command=lambda: self.find_person(person_input, find_command, age_input, add_commmand, delete_command, person1_connection, person2_connection, add_connection_command, del_connection_command))
        button7.place(x = 360, y = 150)

        button4 = ttk.Button(self, text="Delete Person", command=lambda: self.deletion_person(person_input, delete_command, add_commmand, age_input, find_command, person1_connection, person2_connection, add_connection_command, del_connection_command))
        button4.place(x = 357, y = 175)

        button5 = ttk.Button(self, text="Add Connection Between 2 People", command=lambda: self.add_connection(person1_connection, person2_connection, add_connection_command, person_input, find_command, age_input, add_commmand, delete_command, del_connection_command))
        button5.place(x = 320, y = 200)

        button6 = ttk.Button(self, text="Delete Connection Between 2 People", command=lambda: self.del_connection(person1_connection, person2_connection, del_connection_command, add_connection_command, person_input, find_command, age_input, add_commmand, delete_command))
        button6.place(x = 315, y = 225)

        button7 = ttk.Button(self, text="Print Personal Records", command=lambda: self.personal_rec_print(pr_text, person1_connection, person2_connection, del_connection_command, add_connection_command, person_input, find_command, age_input, add_commmand, delete_command, button8))
        button7.place(x = 340, y = 250)

        csv_download = tk.Label(self, text = "Enter File Name", font = LARGE_FONT)
        csv_input = tk.Text(self, height = 1, width = 15, bg = 'light pink')
        save_csv_command = ttk.Button(self, text= "Save", command=lambda: self.save_record_process(csv_input))

        button8 = ttk.Button(self, text="Save CSV", command=lambda: self.save_record(csv_download, csv_input, save_csv_command))


        add_commmand = tk.Button(self, text="Add", fg= 'black', bg= 'green', command=lambda: self.addition_process(person_input, age_input), height = 3, width = 25)
        delete_command = tk.Button(self, text="Delete", fg= 'black', bg= 'red', command=lambda: self.deletion_process(person_input), height = 3, width = 25)
        add_connection_command = tk.Button(self, text="Add Connection", fg= 'black', bg= 'green', command=lambda: self.connection_add_process(person1_connection, person2_connection), height = 3, width = 25)
        del_connection_command = tk.Button(self, text="Delete Connection", fg= 'black', bg= 'red', command=lambda: self.connection_del_process(person1_connection, person2_connection), height = 3, width = 25)
        find_command = tk.Button(self, text="Find", fg= 'black', bg= 'purple', command=lambda: self.finding_process(person_input))

    def addition_person(self, person_input, age_input, add_commmand, delete_command, find_command, person1_connection, person2_connection, add_connection_command, del_connection_command):

        find_command.place_forget()
        delete_command.place_forget()
        person1_connection.place_forget()
        person2_connection.place_forget()
        add_connection_command.place_forget()
        del_connection_command.place_forget()

        person_input.place(x = 250, y = 300)
        age_input.place(x = 330, y = 350)
        add_commmand.place(x = 300, y = 400)
    
    def addition_process(self, person_input, age_input):

        person = person_input.get("1.0", "end-1c")
        info = age_input.get("1.0", "end-1c")

        graph.add_person(str(person), info)

        added_finish = tk.Label(self, text = "Added Complete!", font = QUICK_FONT)
        added_finish.place(x = 300, y = 600)

        return
    
    def deletion_person(self, person_input, delete_command, add_commmand, age_input, find_command, person1_connection, person2_connection, add_connection_command, del_connection_command):

        add_commmand.place_forget()
        find_command.place_forget()
        age_input.place_forget()
        person1_connection.place_forget()
        person2_connection.place_forget()
        add_connection_command.place_forget()
        del_connection_command.place_forget()

        person_input.place(x = 250, y = 350)
        delete_command.place(x = 300, y = 400)

    def deletion_process(self, person_input):

        person = person_input.get("1.0", "end-1c")

        graph.delete_person(str(person))

        delete_finish = tk.Label(self, text = "Deletion Complete", font = QUICK_FONT)
        delete_finish.place(x = 300, y = 600)

        return
    
    def find_person(self, person_input, find_command, age_input, add_commmand, delete_command, person1_connection, person2_connection, add_connection_command, del_connection_command):

        age_input.place_forget()
        add_commmand.place_forget()
        delete_command.place_forget()
        person1_connection.place_forget()
        person2_connection.place_forget()
        add_connection_command.place_forget()
        del_connection_command.place_forget()

        person_input.place(x = 250, y = 350)
        find_command.place(x = 375, y = 400)
    
    def finding_process(self, person_input):

        person = person_input.get("1.0", "end-1c")

        if graph.get_person(person):

            found_person = tk.Label(self, text = "This Person is Within Social Network :)", font = QUICK_FONT)
            found_person.place(x = 300, y = 600)
            return

        else:

            found_person = tk.Label(self, text = "This Person is not Within Social Network :(", font = QUICK_FONT)
            found_person.place(x = 300, y = 600)
            return
            
        
    def add_connection(self, person1_connection, person2_connection, add_connection_command, person_input, find_command, age_input, add_commmand, delete_command, del_connection_command):

        person_input.place_forget()
        find_command.place_forget()
        age_input.place_forget()
        add_commmand.place_forget()
        delete_command.place_forget()
        del_connection_command.place_forget()

        person1_connection.place(x = 260, y = 300)
        person2_connection.place(x = 260, y = 350)
        add_connection_command.place(x = 310, y = 400)
    
    def connection_add_process(self, person1_connection, person2_connection):

        person1 = person1_connection.get("1.0", "end-1c")
        person2 = person2_connection.get("1.0", "end-1c")

        try:
            graph.add_connection({str(person1), str(person2)})

            connectionadd_finish = tk.Label(self, text = "Connection Added!", font = QUICK_FONT)
            connectionadd_finish.place(x = 300, y = 600)


            return

        except ValueError:
            print("one or both people don't exits within the social network")
            return
    
    def del_connection(self, person1_connection, person2_connection, del_connection_command, add_connection_command, person_input, find_command, age_input, add_commmand, delete_command):


        person_input.place_forget()
        find_command.place_forget()
        age_input.place_forget()
        add_commmand.place_forget()
        delete_command.place_forget()
        add_connection_command.place_forget()

        person1_connection.place(x = 260, y = 300)
        person2_connection.place(x = 260, y = 350)
        del_connection_command.place(x = 310, y = 400)
    
    def connection_del_process(self, person1_connection, person2_connection):

        person1 = person1_connection.get("1.0", "end-1c")
        person2 = person2_connection.get("1.0", "end-1c")

        try:
            graph.delete_connection(str(person1), str(person2))


            connectiondel_finish = tk.Label(self, text = "Connection Deleted!", font = QUICK_FONT)
            connectiondel_finish.place(x = 300, y = 600)
            return

        except ValueError:
            print("one or both people don't exist within the social network")
            return
    
    def personal_rec_print(self, pr_text, person1_connection, person2_connection, del_connection_command, add_connection_command, person_input, find_command, age_input, add_commmand, delete_command, button8):
        
        person_input.place_forget()
        find_command.place_forget()
        age_input.place_forget()
        add_commmand.place_forget()
        delete_command.place_forget()
        add_connection_command.place_forget()
        del_connection_command.place_forget()
        person1_connection.place_forget()
        person2_connection.place_forget()


        pr = self.pr

        for record in graph.personal_record.export():
            pr.insert(0, str(record))
        
        pr_text.place(x = 305, y = 350)
        pr.place(x = 400, y = 375, anchor = 'n')
        button8.place(x = 450, y = 475)

        return
    

    def save_record(self, csv_download, csv_input, save_csv_command):

        csv_download.place(x = 450, y = 650)
        csv_input.place(x = 475, y = 700)
        save_csv_command.place(x = 500, y = 750)
    
    def save_record_process(self, csv_input):

        filename = csv_input.get("1.0", "end-1c")

        try:

            with open(str(filename), 'w', newline = '') as f:
                writer = csv.writer(f, quoting = csv.QUOTE_ALL)
                writer.writerow(["PERSONAL RECORD"])
                for item in graph.personal_record.export():
                    writer.writerow(item)

                return

        except FileNotFoundError:
            print("Sorry, this file can't be found in current path")
            return


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image = Image.open("CVBGUI.gif")
        self.img_cp = self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image = self.background_image)
        self.background.pack(fill = BOTH, expand = YES)
        label = tk.Label(self, text="Statistics", font=LARGE_FONT)
        label.place(x= 340, y = 25)
        self.list1 = tk.Listbox(self, height = 15, width = 20, font= QUICK_FONT)
        self.list2 = tk.Listbox(self, height = 15, width = 20, font = QUICK_FONT)
        self.list3 = tk.Listbox(self, height = 15, width = 20, font = QUICK_FONT)
        self.list4 = tk.Listbox(self, height = 15, width = 20, font = QUICK_FONT)

        s_header = tk.Label(self, text= "** Suspectables **", font = QUICK_FONT)
        i_header = tk.Label(self, text= "** Infected **", font= QUICK_FONT)
        r_header = tk.Label(self, text= "** Recovered **", font= QUICK_FONT)
        d_header = tk.Label(self, text = "** Dead **", font = QUICK_FONT)

        csv_download = tk.Label(self, text = "Enter File Name **(filename.csv)** to download as csv", font = LARGE_FONT)
        csv_input = tk.Text(self, height = 2, width = 35, bg = 'light pink')

        save_csv_command = ttk.Button(self, text= "Save", command=lambda: self.download_csv_command(csv_input))

        button1 = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(StartPage)) 
        button1.place(x = 340, y = 55)

        button2 = ttk.Button(self, text="To Person Add/Deletion Support", command=lambda: controller.show_frame(PageOne)) 
        button2.place(x = 310, y = 80)

        button3 = tk.Button(self, text="Print Suspects", command=lambda: self.suspectable_current(s_header), fg='yellow', bg= 'black', height = 2, width = 25)
        button3.place(x = 310, y = 105)

        button4 = tk.Button(self, text="Print Infected", command=lambda: self.infected_current(i_header), fg='green', bg= 'black', height = 2, width = 25)
        button4.place(x = 310, y = 145)

        button5 = tk.Button(self, text="Print Recovered", command=lambda: self.recovered_current(r_header), fg='blue', bg= 'black', height = 2, width = 25)
        button5.place(x = 310, y = 185)

        button6 = tk.Button(self, text="Print Dead", command=lambda: self.dead_current(d_header), fg = 'grey', bg = 'black', height = 2, width = 25)
        button6.place(x = 310, y = 225)

        button7 = ttk.Button(self, text="Save CSV", command=lambda: self.download_csv(csv_download, csv_input, save_csv_command))
        button7.place(x = 360, y = 265)


    def suspectable_current(self, s_header):

        suspects_box = self.list1

        for person in graph.suspectable.export():
            suspects_box.insert(0, str(person))

        s_header.place(x = 60, y = 315)
        suspects_box.place(x = 120, y=345, anchor= 'n')

        return
    
    def infected_current(self, i_header):

        infected_box = self.list2

        for person in graph.infected.export():
            infected_box.insert(0, str(person))
        
        i_header.place(x = 255, y = 315)
        infected_box.place(x = 300, y = 345, anchor= 'n')

        return
    
    def recovered_current(self, r_header):

        recovered_box = self.list3

        for person in graph.recovered.export():
            recovered_box.insert(0, str(person))

        r_header.place(x = 445, y = 315)
        recovered_box.place(x = 500, y = 345, anchor= 'n')

        return
    
    def dead_current(self, d_header):

        dead_box = self.list4

        for person in graph.dead.export():
            dead_box.insert(0, str(person))
        
        d_header.place(x = 640, y = 315)
        dead_box.place(x = 680, y = 345, anchor= 'n')

        return
    

    def download_csv(self, csv_download, csv_input, save_csv_command):

        csv_download.place(x = 125, y = 655)
        csv_input.place(x = 250, y = 705)
        save_csv_command.place(x = 350, y = 755)
    
    def download_csv_command(self, csv_input):

        filename = csv_input.get("1.0", "end-1c")

        try:

            with open(str(filename), 'w', newline = '') as f:
                writer = csv.writer(f, quoting = csv.QUOTE_ALL)
                writer.writerow(["SUSPECTS"])
                writer.writerow(graph.suspectable.export())
                writer.writerow(["INFECTED"])
                writer.writerow(graph.infected.export())
                writer.writerow(["RECOVERED"])
                writer.writerow(graph.recovered.export())
                writer.writerow(["DEAD"])
                writer.writerow(graph.dead.export())
                return

        except FileNotFoundError:
            print("Sorry, this file can't be found in current path")
            return



class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.image = Image.open("CVBGUI.gif")
        self.img_cp = self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image = self.background_image)
        self.background.pack(fill = BOTH, expand = YES)
        label = tk.Label(self, text="Simulation Support", font=LARGE_FONT)
        label.place(x = 300, y = 25)
        self.result_array = np.zeros((10+1,4))
        self.results = tk.Listbox(self, height = 15, width = 20, font= QUICK_FONT)

        """Simulation Value Widgets"""
        trans_text = tk.Label(self, text="Transmission Rate", font = QUICK_FONT)
        trans_input = tk.Text(self, height =  2, width = 8, bg = "light green")
        trans_text.place(x = 180, y = 125)
        trans_input.place(x = 200, y = 150)
        recov_text = tk.Label(self, text="Recovery Rate", font = QUICK_FONT)
        recov_input = tk.Text(self, height = 2, width = 8, bg= "light blue")
        recov_text.place(x = 350, y = 125)
        recov_input.place(x = 360, y = 150)
        death_text = tk.Label(self, text="Death Rate", font = QUICK_FONT)
        death_input = tk.Text(self, height = 2, width =  8, bg = "light grey")
        death_text.place(x = 520, y = 125)
        death_input.place(x = 525, y = 150)
        days_text = tk.Label(self, text="Days", font = QUICK_FONT)
        days_input = tk.Text(self, height = 2, width = 6, bg = "azure")
        days_text.place(x = 375, y = 200)
        days_input.place(x = 370, y = 225)

        """Intervention Menu Prompt Button"""
        interventions_text = ttk.Button(self, text="Interventions Menu", command=lambda: self.intervention_menu(inf_int_title, inf_int_rate, inf_int_time, inf_int_title2, death_int_title, death_int_title2, death_int_time, death_int_rate, rec_int_title, rec_int_title2, rec_int_time, rec_int_rate, interventions_text, intervention_command, trans_input, recov_input, death_input, button5, button3, button4, trans_text, recov_text, death_text, initial_infect, initial_infect_title, days_input, days_text))
        interventions_text.place(x = 340, y = 425)

        """Intervention Layout Widgets"""

        death_int_title = tk.Label(self, text = "Start Day", font = QUICK_FONT)
        death_int_title2 = tk.Label(self, text = "Death Rate", font = QUICK_FONT)
        death_int_time = tk.Text(self, height = 2, width = 8, bg = "light grey")
        death_int_rate = tk.Text(self, height = 2, width = 8, bg = "light grey")


        inf_int_title = tk.Label(self, text="Start Day", font = QUICK_FONT)
        inf_int_title2 = tk.Label(self, text="Transmission Rate", font = QUICK_FONT)
        inf_int_time = tk.Text(self, height = 2, width = 8, bg= "light green")
        inf_int_rate = tk.Text(self, height = 2, width = 8, bg = "light green")

        rec_int_title = tk.Label(self, text = "Start Day", font = QUICK_FONT)
        rec_int_title2 = tk.Label(self, text = "Recovery Rate", font = QUICK_FONT)
        rec_int_time = tk.Text(self, height = 2, width = 8, bg = "light blue")
        rec_int_rate = tk.Text(self, height = 2, width = 8, bg = "light blue")

        """Initial Infect Widgets"""
        initial_infect_title = tk.Label(self, text= "Enter Name Of Initial Infected Person", font = QUICK_FONT)
        initial_infect = tk.Text(self, height = 2, width = 15, bg = "azure")
        initial_infect_title.place(x = 280, y = 300)
        initial_infect.place(x = 335, y = 350)

        """Results SIRD Title"""
        sird_title = tk.Label(self, text= "S, I, R, D", font = LARGE_FONT)

        """Main Simulation Widgets"""
        button1 = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(StartPage))
        button1.place(x = 345, y = 50)
        button2 = ttk.Button(self, text="To Statistics", command=lambda: controller.show_frame(PageTwo)) 
        button2.place(x = 362.5, y = 75)
        intervention_command = ttk.Button(self, text="Run With Intervention", command=lambda: self.activate_intervention(inf_int_time, inf_int_rate, death_int_rate, death_int_time, rec_int_rate, rec_int_time))
        button3 = ttk.Button(self, text="Run Simulation", command=lambda: self.plot(initial_infect, trans_input, recov_input, death_input, days_input))
        button3.place(x = 350, y = 700)
        button4 = ttk.Button(self, text="See Results Of Past Simulation", command=lambda: self.result_run(trans_input, recov_input, death_input, button5, button3, button4, intervention_command, trans_text, recov_text, death_text, interventions_text, inf_int_title, inf_int_title2, inf_int_time, inf_int_rate, initial_infect, initial_infect_title, days_input, days_text, sird_title))
        button4.place(x = 310, y = 750)
        button5 = ttk.Button(self, text="Reset", command=lambda: self.reset_sim(trans_input, recov_input, death_input, button5, button3, button4, intervention_command, trans_text, recov_text, death_text, interventions_text, inf_int_title, inf_int_title2, inf_int_time, inf_int_rate, initial_infect, initial_infect_title, days_input, days_text, sird_title))

        """Intervention Support Extra Widgets"""
        self.g_trans_rate = 0
        self.g_recov_rate = 0
        self.g_death_rate = 0
        self.g_days = 0
        self.g_initial_infect = ""

        """Slow/Fast Motion Support Widgets"""

        ex_slow = ttk.Button(self, text = "Extreme SlowMotion", command=lambda: NotImplementedError)
        slow = ttk.Button(self, text = "SlowMotion", command=lambda: NotImplementedError)
        reg_speed = ttk.Button(self, text = "Normal Speed", command=lambda: NotImplementedError)
        fast = ttk.Button(self, text = "FastMotion", command=lambda: NotImplementedError)
        ex_fast = ttk.Button(self, text = "Extreme FastMotion", command=lambda: NotImplementedError)


    def intervention_menu(self, inf_int_title, inf_int_rate, inf_int_time, inf_int_title2, death_int_title, death_int_title2, death_int_time, death_int_rate, rec_int_title, rec_int_title2, rec_int_time, rec_int_rate, interventions_text, intervention_command, trans_input, recov_input, death_input, button5, button3, button4, trans_text, recov_text, death_text, initial_infect, initial_infect_title, days_input, days_text):
        
        """Holding Original Rates From Simulation Main Page"""
        
        self.g_trans_rate = float(trans_input.get("1.0", "end-1c"))
        self.g_death_rate = float(death_input.get("1.0", "end-1c"))
        self.g_recov_rate = float(recov_input.get("1.0", "end-1c"))
        self.g_days = int(days_input.get("1.0", "end-1c"))
        self.g_initial_infect = str(initial_infect.get("1.0", "end-1c"))

        """Clear Home Page Simulation Buttons"""
        trans_input.place_forget()
        recov_input.place_forget()
        death_input.place_forget()
        button3.place_forget()
        button4.place_forget()
        intervention_command.place_forget()
        trans_text.place_forget()
        recov_text.place_forget()
        death_text.place_forget()
        interventions_text.place_forget()
        inf_int_title.place_forget()
        inf_int_title2.place_forget()
        inf_int_time.place_forget()
        inf_int_rate.place_forget()
        initial_infect.place_forget()
        initial_infect_title.place_forget()
        days_input.place_forget()
        days_text.place_forget()

        inf_int_rate.place(x = 420, y = 200)
        inf_int_time.place(x = 300, y = 200)
        inf_int_title.place(x = 300, y = 150)
        inf_int_title2.place(x = 400, y = 150)

        intervention_command.place(x = 335, y = 600)

        death_int_title.place(x = 300, y = 250)
        death_int_title2.place(x = 415, y = 250)
        death_int_time.place(x = 300, y = 300)
        death_int_rate.place(x = 420, y = 300)

        rec_int_title.place(x = 300, y = 350)
        rec_int_title2.place(x = 407.5, y = 350)
        rec_int_time.place(x = 300, y = 400)
        rec_int_rate.place(x = 420, y = 400)

        

        return


    def activate_intervention(self, inf_int_time, inf_int_rate, death_int_rate, death_int_time, rec_int_rate, rec_int_time):
        
        """Added Intervention Support"""

        """Intervention Settings Obtainer"""

        """Infected Intervention"""
        if inf_int_time.index("end") != 0:  
            inf_intervention_day = int(inf_int_time.get("1.0", "end-1c"))
            inf_intervention_rate = float(inf_int_rate.get("1.0", "end-1c"))
            pass
        else:
            pass

        """Death Interention"""
        if death_int_time.index("end") != 0:
            death_intervention_day = int(death_int_time.get("1.0", "end-1c"))
            death_intervention_rate = float(death_int_rate.get("1.0", "end-1c"))
            pass
        else:
            pass

        """Recovery Intervention"""
        if rec_int_time.index("end") != 0:
            rec_intervention_day = int(rec_int_time.get("1.0", "end-1c"))
            rec_intervention_rate = float(rec_int_rate.get("1.0", "end-1c"))
            pass
        else:
            pass

        """Original Simulation Rates and Settings"""
        person = self.g_initial_infect
        recov_rate = self.g_recov_rate
        trans_const = self.g_trans_rate
        death_rate = self.g_death_rate
        days = self.g_days

        """SIRD Simulation Results Array"""
        self.result_array = np.zeros((days+1, 4))

        graph.add_initial(person)

        for tt in range(1, days+1):

            """Intervention Activation"""

            """Transmission Rate Intervention Driver"""
            if inf_intervention_day:
                while tt >= inf_intervention_day:
                    trans_const = graph.inf_intervention(inf_intervention_rate, trans_const)
                    break
                pass

            """Death Rate Intervention Driver"""
            if death_intervention_day:
                while tt >= death_intervention_day:
                    death_rate = graph.death_intervention(death_intervention_rate, death_rate)
                    break
                pass

            """Recovery Rate Intervention Driver"""
            
            if rec_intervention_day:
                while tt >= rec_intervention_day:
                    recov_rate = graph.recov_intervention(rec_intervention_rate, recov_rate)
                    break
                pass


            graph.interact(person, tt, trans_const, recov_rate, death_rate)

            S = graph.suspectable.size()
            I = graph.infected.size()
            R = graph.recovered.size()
            D = graph.dead.size()

            self.result_array[tt,:] = S, I, R, D

            while tt == 1:

                plt.figure(figsize=(10,7))
                break
            
            """Pause Support For MatPlotLib"""
            plt.pause(0.5)
            plt.subplot(1, 3, 1)

            if inf_intervention_day:
                while tt == inf_intervention_day:
                    plt.text(tt, 4, s = "--> INTERVENTION ACTIVE", color = 'green')
                    break
                pass

            if death_intervention_day:
                while tt == death_intervention_day:
                    plt.text(tt, 6, s = "--> INTERVENTION ACTIVE", color = 'grey')
                    break
                pass

            if rec_intervention_day:
                while tt == rec_intervention_day:
                    plt.text(tt, 8, s = "--> INTERVENTION ACTIVE", color = 'blue')
                    break
                pass

            """Main Line Graph Support"""

            plt.title("STATS GRAPH")
            plt.xlabel("DAYS")
            plt.ylabel("PEOPLE")
            plt.plot(tt, self.result_array[tt, 0], 'yo', label = "Suspects")
            plt.plot(tt, self.result_array[tt, 1], 'go', label = "Infected") 
            plt.plot(tt, self.result_array[tt, 2], 'bo', label = "Recovered")
            plt.plot(tt, self.result_array[tt, 3], 'ko', label = "Died")
            plt.subplots_adjust(wspace = 0.75)


            while tt <= 1:

                plt.legend(bbox_to_anchor = [0.5, 0.85], bbox_transform = plt.gcf().transFigure, fontsize = "x-small", loc = 'center')
                death_text = plt.text(0.45, 0.75, "DEATH RATE: " + str(death_rate * 100) + "%",  transform = plt.gcf().transFigure, fontsize = 10)
                inf_text = plt.text(0.45, 0.725, "INF RATE: " + str(trans_const * 100) + "%", transform = plt.gcf().transFigure, fontsize = 10)
                recov_text = plt.text(0.45, 0.70, "RECOV RATE: " + str(recov_rate * 100) + "%", transform = plt.gcf().transFigure, fontsize = 10)
                break

            if inf_intervention_day:
                while tt >= inf_intervention_day:
                    inf_text.set_text("INF RATE: " + str(trans_const * 100) + "%")
                    break
                pass

            if death_intervention_day:
                while tt >= death_intervention_day:
                    death_text.set_text("DEATH RATE: " + str(death_rate * 100) + "%")
                    break
                pass

            if rec_intervention_day:
                while tt >= rec_intervention_day:
                    recov_text.set_text("RECOV RATE: " + str(recov_rate * 100) + "%")
                    break
                pass
            

            """Networkx Social Network Graph Visualisation Support"""

            plt.subplot(1, 3, 3)
            plt.title("SOCIAL NETWORK")
            nx.draw_networkx(graph.graph_visual(), pos=nx.spring_layout(graph.graph_visual()), node_color = graph.color_set(), node_size=300, node_shape='d')
            plt.cla()
            plt.title("SOCIAL NETWORK")
            nx.draw_networkx(graph.graph_visual(), pos=nx.spring_layout(graph.graph_visual()), node_color = graph.color_set(), node_size=300, node_shape='d')



            """Pi Chart Support"""

            pi_labels = 'Suspects', 'Infected', 'Recovered', 'Dead'
            pi_colors = ['yellow', 'green', 'blue', 'grey']
            pi_sizes = [graph.suspectable.size(), graph.infected.size(), graph.recovered.size(), graph.dead.size()]

            pi_g_labels = 'Male', 'Female'
            pi_g_colors = ['skyblue', 'lightpink']
            pi_g_sizes = [graph.gender_search_m(), graph.gender_search_f()]
            
            """Exploding Largest Health Category Within Pie Chart at Iteration (day)"""
            if max(pi_sizes) == graph.suspectable.size():
                pi_explode = (0.15, 0, 0, 0)
                pass
            if max(pi_sizes) == graph.infected.size():
                pi_explode = (0, 0.15, 0, 0)
                pass
            if max(pi_sizes) == graph.recovered.size():
                pi_explode = (0, 0, 0.15, 0)
                pass
            if max(pi_sizes) == graph.dead.size():
                pi_explode = (0, 0, 0, 0.15)
                pass

            plt.subplot(1, 3, 2)
            plt.pie(pi_sizes, explode = pi_explode, labels = pi_labels, colors = pi_colors, autopct = "%1.1f%%", shadow = True, pctdistance = 1.5, startangle = 90)
            plt.pie(pi_g_sizes, labels = pi_g_labels, colors = pi_g_colors, autopct = "%1.1f%%", shadow = True, radius = 0.75, startangle = 90)
            pi_circle = plt.Circle((0,0), 0.7, color = 'white')
            p = plt.gcf()
            p.gca().add_artist(pi_circle)
            plt.axis('equal')

            plt.cla()

            plt.pie(pi_sizes, explode = pi_explode, labels = pi_labels, colors = pi_colors,  autopct = "%1.1f%%", shadow = True, pctdistance = 1.5, startangle = 90)
            plt.pie(pi_g_sizes, labels = pi_g_labels, colors = pi_g_colors, autopct = "%1.1f%%", shadow = True, radius = 0.75, startangle = 90)
            pi_circle = plt.Circle((0,0), 0.3, color = 'white')
            p = plt.gcf()
            p.gca().add_artist(pi_circle)
            plt.axis('equal')

        plt.show()

        return


    def plot(self, initial_infect, trans_input, recov_input, death_input, days_input):
        
        person = str(initial_infect.get("1.0", "end-1c"))
        recov_rate = float(recov_input.get("1.0", "end-1c"))
        trans_const = float(trans_input.get("1.0", "end-1c"))
        death_rate = float(death_input.get("1.0", "end-1c"))
        days = int(days_input.get("1.0", "end-1c"))

        self.result_array = np.zeros((days+1, 4))

        graph.add_initial(person)

        for tt in range(1, days+1):

            graph.interact(person, tt, trans_const, recov_rate, death_rate)

            S = graph.suspectable.size()
            I = graph.infected.size()
            R = graph.recovered.size()
            D = graph.dead.size()

            self.result_array[tt,:] = S, I, R, D

            plt.pause(0.5)
            plt.subplot(1, 2, 1)
            plt.plot(tt, self.result_array[tt, 0], 'yo')
            plt.plot(tt, self.result_array[tt, 1], 'go') 
            plt.plot(tt, self.result_array[tt, 2], 'bo')
            plt.plot(tt, self.result_array[tt, 3], 'ko')

            plt.subplot(1, 2, 2)
            nx.draw_networkx(graph.graph_visual(), pos=nx.spring_layout(graph.graph_visual()), node_color = graph.color_set(), node_size=300, node_shape='d')
            plt.cla()
            nx.draw_networkx(graph.graph_visual(), pos=nx.spring_layout(graph.graph_visual()), node_color = graph.color_set(), node_size=300, node_shape='d')

        plt.show()

        return

    def result_run(self, trans_input, recov_input, death_input, button5, button3, button4, intervention_command, trans_text, recov_text, death_text, interventions_text, inf_int_title, inf_int_title2, inf_int_time, inf_int_rate, initial_infect, initial_infect_title, days_input, days_text, sird_title):

        
        trans_input.place_forget()
        recov_input.place_forget()
        death_input.place_forget()
        button3.place_forget()
        button4.place_forget()
        intervention_command.place_forget()
        trans_text.place_forget()
        recov_text.place_forget()
        death_text.place_forget()
        interventions_text.place_forget()
        inf_int_title.place_forget()
        inf_int_title2.place_forget()
        inf_int_time.place_forget()
        inf_int_rate.place_forget()
        initial_infect.place_forget()
        initial_infect_title.place_forget()
        days_input.place_forget()
        days_text.place_forget()


        results = self.results

        for result in self.result_array:
            results.insert(0, str(result))

        results.place(x = 400, y = 200, anchor= 'n')
        button5.place(x = 355, y = 750)
        sird_title.place(x = 340, y = 150)

        return


    def reset_sim(self, trans_input, recov_input, death_input, button5, button3, button4, intervention_command, trans_text, recov_text, death_text, interventions_text, inf_int_title, inf_int_title2, inf_int_time, inf_int_rate, initial_infect, initial_infect_title, days_input, days_text, sird_title):

        self.results.place_forget()
        trans_input.place_forget()
        recov_input.place_forget()
        death_input.place_forget()
        button3.place_forget()
        button5.place_forget()
        intervention_command.place_forget()
        trans_text.place_forget()
        recov_text.place_forget()
        death_text.place_forget()
        interventions_text.place_forget()
        inf_int_title.place_forget()
        inf_int_title2.place_forget()
        inf_int_time.place_forget()
        inf_int_rate.place_forget()
        initial_infect.place_forget()
        initial_infect_title.place_forget()
        sird_title.place_forget()


        button4.place(x = 310, y = 750)
        button3.place(x = 350, y = 700)
        intervention_command.place(x = 335, y = 650)
        trans_text.place(x = 150, y = 125)
        trans_input.place(x = 175, y = 150)
        recov_text.place(x = 360, y = 125)
        recov_input.place(x = 375, y = 150)
        death_text.place(x = 570, y = 125)
        death_input.place(x = 575, y = 150)
        days_text.place(x = 370, y = 200)
        days_input.place(x = 365, y = 225)
        interventions_text.place(x = 355, y = 300)
        inf_int_rate.place(x = 465, y = 375)
        inf_int_time.place(x = 255, y = 375)
        inf_int_title.place(x = 225, y = 340)
        inf_int_title2.place(x = 450, y = 340)
        initial_infect_title.place(x = 280, y = 450)
        initial_infect.place(x = 335, y = 500)


        for person in graph.infected.export():
            graph.suspectable.addPerson_start(person)
            graph.infected.delete_person(person)
        for person in graph.recovered.export():
            graph.suspectable.addPerson_start(person)
            graph.recovered.delete_person(person)
        for person in graph.dead.export():
            graph.suspectable.addPerson_start(person)
            graph.dead.delete_person(person)

    
"""Test Harness"""

app = interactive_menu()
app.mainloop()


