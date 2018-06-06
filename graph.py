import networkx as nx
import numpy as np
import matplotlib.pylab as plt

# adj_mat=np.array([[0,1,0,0,0,1],
#                   [1,0,1,1,1,0],
#                   [0,1,0,1,0,1],
#                   [0,1,1,0,0,1],
#                   [0,1,0,0,0,1],
#                   [1,0,1,1,1,0],])

adj_mat = np.array( [ [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
                      [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                      [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
                      [0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
                      [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                      [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                      [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                      [0, 1, 0, 0, 1, 0, 0, 1, 0, 0] ])

def drawGraph(mat):
    G = nx.Graph(adj_mat)

    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos, node_color="w")
    nx.draw_networkx_edges(G, pos, width=1)
    nx.draw_networkx_edge_labels(G, pos)
    nx.draw_networkx_labels(G, pos, font_size=16, font_color="black")

    plt.xticks([])
    plt.yticks([])
    plt.show()

def neighbor(mat, node):
    n = []
    for i in range(0, len(mat[node])):
        if mat[i, node] > 0 or mat[node, i] > 0:  # ma trận không đối xứng
            n.append(i)
    return n

def BFS(mat, node):
    if node > len(mat[0]):
        return None
    sample = [node]
    wait = [node]
    while len(wait) > 0:
        no = wait[0]
        for n in neighbor(mat, no):
            if n not in sample:
                sample.append(n)
                wait.append(n)
        wait.remove(no)
    return sample

def DFS(mat, node):
    if node > len(mat[0]):
        return None
    sample = []
    wait = [node]
    while len(wait) > 0:
        no = wait[0]
        if no not in sample:
            sample.append(no)
            child = neighbor(mat, no)
            for i in reversed(child):
                wait.insert(0, i)

        wait.remove(no)
    return sample

drawGraph(adj_mat)
print(DFS(adj_mat, 3))