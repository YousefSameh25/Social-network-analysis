import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from tkinter import filedialog
import Algorithms
import GUI
import networkx as nx
import preprocessing

G = nx.DiGraph()

def homePage():
    root = tk.Tk()
    root.geometry("500x300")

    root.title("Social Network analysis")

    label = tk.Label(root, text= "Home Page" , font = 12)
    label.pack()


    def radio_click1():
        GUI.G = nx.Graph()

    def radio_click2():
        GUI.G = nx.DiGraph()

    # Create the radio buttons
    option1 = tk.Radiobutton(root, text="Undirected", value = "1", command = radio_click1)
    option2 = tk.Radiobutton(root, text="Directed", value = "2" , command = radio_click2)

    # Pack the radio buttons
    option1.pack(pady = 5)
    option2.pack(pady = 10)

    def button1_click():
        # Show a file dialog window and get the selected file path
        node_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        preprocessing.readNodes(G,node_path)

    def button2_click():
        # Show a file dialog window and get the selected file path
        edges_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        preprocessing.readEdges(G,edges_path)


    def Next():
        # Navigate to algorithms page
        print("Clicked")
        select_algorithm(root)


    button1 = tk.Button(root, text = "Browse Nodes", command = button1_click)
    button1.pack(pady = 5)

    button2 = tk.Button(root, text = "Browse Edges", command = button2_click)
    button2.pack(pady = 5)

    button3 = tk.Button(root, text = "Next", command = Next)
    button3.pack(pady = 5)

    root.mainloop()

def select_algorithm(root):
    ty = "Directed" if G.is_directed() else "Undirected"
    print("Type of the graph is " + ty)
    # Create a new top-level window
    new_window = tk.Toplevel(root)
    new_window.geometry("500x300")
    new_window.title("Techniques")
    #=====================================================

    label = tk.Label(new_window, text="Select an option", font=12)
    label.pack()

    # Create a list of options for the combobox
    options = ["Louvain algorithm", "Modularity", "Conductance" ,
               "NMI" , "Page rank" , "Degree centrality" , "Closeness centrality",
               "Betweenness centrality" , "Adjust graph"]

    # Create a StringVar object to store the selected option
    selected_option = tk.StringVar()

    # Create the combobox widget and pack it onto the window
    combobox = ttk.Combobox(new_window, values=options, textvariable=selected_option)
    combobox.pack()

    # Create a function to handle combobox selection events
    def combobox_selected(event):
        if selected_option.get() == options[0]:
            Algorithms.Louvain_algorithm(G)
        elif selected_option.get() == options[8]:
            Algorithms.adjust_graph(G)
        elif selected_option.get() == options[4]:
            Algorithms.Page_Rank(G)
        elif selected_option.get() == options[5]:
            Algorithms.Degree_Centrality(G)
        elif selected_option.get() == options[6]:
            Algorithms.Closeness_Centrality(G)
        elif selected_option.get() == options[7]:
            Algorithms.Betweenness_Centrality(G)
        elif selected_option.get() == options[1]:
            Algorithms.Modularity(G)
        elif selected_option.get() == options[2]:
            Algorithms.Conductance(G)
        elif selected_option.get() == options[3]:
            Algorithms.NMI(G)


    # Bind the combobox selection event to the combobox_selected function
    combobox.bind("<<ComboboxSelected>>", combobox_selected)
    combobox.pack(pady = 60)

    # Set the default option
    selected_option.set(options[0])

