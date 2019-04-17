import pdb
import sys

# Graph Definition
class Node:
    def __init__(self,val, child = [], leftbank = [], rightbank = []):     # Node("",[Node(4),Node(5)])
        self.val = val
        self.child = child
        self.leftbank = []      # C, W, B
        self.rightbank = []     # C, W, B

class Graph:
    def __init__(self, val, children):
        self.state = Node(val, children)
        

    def add_successor_nodes(self,nodes):
        for node in nodes:
            self.state.child.append(Node(node))

# Reading Files for Start State
sys.argv = [sys.argv[0], 'start1.txt']
start_file = open(sys.argv[1], "r")
x = start_file.readline()
leftbank = []
leftbank.append(x[0])
leftbank.append(x[2])
leftbank.append(x[4])
x = start_file.readline()
rightbank = []
rightbank.append(x[0])
rightbank.append(x[2])
rightbank.append(x[4])

# x  = Graph(3,[Node(5,[Node(3)])])       # Syntax similar to functional programming
# alternatively can use a dict mapping for denoting relationships on a graph
pdb.set_trace()
def graph_search (problem, fringe):
    closed = []
    fringe = []     # Is kinda like the fifo queue
