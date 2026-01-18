import networkx as nx
import pandas as pd 
import matplotlib.pyplot as plt 

df  = pd.read_csv("Data\Processed-Data.csv")

def Make_Graph():
    G = nx.Graph()
    for _,data in df.iterrows():
        G.add_edge(data["DoctorID"],data["Specialization"])
        G.add_edge(data["DoctorID"],data["PatientID"])
    return G

def Visualization():
    pass 

G = Make_Graph()

print(G)

color_map = []
for node in G:
    if node == "Specialization":
        color_map.append('blue')
    elif node == "DoctorID": 
        color_map.append('green')
    elif node == "Patient":
        color_map.append('black')



nx.draw(G, node_color=color_map, with_labels=True)
plt.show()
