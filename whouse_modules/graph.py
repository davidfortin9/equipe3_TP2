import whouse
import networkx as nx
import whousedesign as wsd 
import matplotlib.pyplot as plt

def nx_create(arcs, nodes):
        arcs = arcs
        nodes = nodes
        node_keys = nodes.keys()
        G = nx.Graph()

        # Adding edges with weight
        for key in arcs.keys():
            G.add_edge(arcs[key][1], arcs[key][2], weight=arcs[key][0])

        # Adding nodes
        G.add_nodes_from(node_keys)
        print ("NetworkX graph created")
        return G 

def nx_draw(arcs, nodes):
        G = nx_create(arcs, nodes)
        
        nx.draw(G, with_labels = True)
        plt.show()


    
 