import networkx as nx
import numpy as np
import matplotlib.pylab as plt
import random

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
    G = nx.Graph(mat)

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


def bias_alpha(mat, ori, current, visited, p , q):
	probability = []
	neighbor_ori = neighbor(mat, ori)
	neighbor_cur = neighbor(mat, current)
	for item in neighbor_cur:
		if item in visited:
			probability.append(1.0/p)
		elif item in neighbor_ori:
			probability.append(1.0)
		else:
			probability.append(1.0/q)
	return probability

def random_walk(mat, node, p, q, no_sample):
	ori_node = node
	first_step = None
	visited = [ori_node]
	walk = [node]
	probability = []
#1st step from origin	
	neigh = neighbor(mat, ori_node)
	first_step = random.choice(neigh)
	visited.append(first_step)
	walk.append(first_step)
#Other step	
	while len(visited) < no_sample:
		neigh = neighbor(mat, first_step)
		probability = bias_alpha(mat, ori_node, first_step, visited, p, q)
		max_index = probability.index(max(probability))
		ori_node = first_step
		first_step = neigh[max_index]
		if first_step not in visited:
			visited.append(first_step)
		walk.append(first_step)
	return walk





print(random_walk(adj_mat, 3, 5, 4, 6))
drawGraph(adj_mat)