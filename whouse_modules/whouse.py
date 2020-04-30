import whouse_modules.whousedesign as wsd 
import whouse_modules.graph as graph

class whouse:

    def __init__(self, 
                warehouse_width=0, 
                warehouse_length=0, 
                arcs={}, 
                nodes={},
                slots=[],):
        self.warehouse_width = warehouse_width
        self.warehouse_length = warehouse_length
        self.arcs = arcs
        self.nodes = nodes
        self.slots = slots
        self.whouse_graph = graph.nx_create(arcs, nodes)
        

    
    
