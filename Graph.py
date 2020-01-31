# Import library for working with graphs
import time
import networkx as nx
import pylab as plt

# Function to build plot of my generated graph
def drawing():
    if n <= 15:  # Building graph with more than 15 vertex is disrespectful
        nx.draw(g, with_labels=True)
        plt.show()
    else:
        print("Are you sure?")
        keyDraw = input("y/n ? ")
        if keyDraw == "y":
            nx.draw(g, with_labels=True)
            plt.show()


def bfs_time():
    root = 0  # Vertex which will be a start vertex in bfs
    edges = nx.bfs_edges(g, root)
    nodes = [root] + [v for u, v in edges]


def bfs():
    root = int(input("Enter root vertex: "))  # Vertex which will be a start vertex in bfs
    # time.perf_counter()
    edges = nx.bfs_edges(g, root)
    nodes = [root] + [v for u, v in edges]
    # times = time.process_time()
    # print("BFS time is: ", time.process_time(), " seconds")
    if n <= 20:
        print("BFS way is:", nodes)
    else:
        print("Do you want to see bfs way?")
        keyWay = input("y/n ? ")
        if keyWay == "y":
            print(nodes)
    gnodes = g.nodes()
    if len(nodes) == 1:
        print("BFS has started from isolated vertex, try again")
    else:
        ivertex = gnodes - nodes
        livertex = list(ivertex)
        f = open('isolation.txt', 'w')
        for i in range(len(livertex)):
            out = str(livertex[i]) + ','
            f.write(out)
        f.close


def add_edge():
    val = int(input("How many edges do you want to add? "))
    for i in range(val):
        startV = int(input("Enter start vertex: "))
        endV = int(input("Enter end vertex: "))
        g.add_edges_from([(startV, endV)])


if __name__ == "__main__":  # Start of the program
    print("Welcome to my scientific work")
    flag = True
    while flag:
        n = int(input("To set the graph enter quantity of vertex: "))
        p = float(input("Enter probability of edge appearance: "))
        g = nx.fast_gnp_random_graph(n, p, None, False)
        key = 0
        while key != -1:
            print("==============")
            print("1 - Draw graph")
            print("2 - Breadth first search")
            print("3 - Add some edges")
            print("4 - bfs time")
            print("To exit enter any other number")
            key = int(input("Enter key: "))
            if key == 1:
                drawing()
            elif key == 2:
                bfs()
            elif key == 3:
                add_edge()
            elif key == 4:
                start_time = time.time()
                bfs_time()
                print("--- %s seconds ---" % (time.time() - start_time))
            else:
                key = -1
        print("Do you want to another quantity of vertex?")
        keyAgain = input("y/n ? ")
        if keyAgain == "y":
            flag = True
        else:
            flag = False
