import heapq
import sys
import numpy as np
from typing import List, Dict, Set, Tuple
from IPython.display import Image
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = [15, 15]

def run(matrix, start, end):
    edges: Dict[Tuple[int, int], Set[Tuple[int, int]]] = {}
    risks = {}
    for r, row in enumerate(matrix):
        for c, weight in enumerate(row):
            risks[(r, c)] = weight
            if (r, c) not in edges:
                edges[(r, c)] = set()
            for ro, co in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = r + ro, c + co
                if nr < 0 or nc < 0 or nr >= len(matrix) or nc >= len(matrix[0]):
                    continue
                edges[(r, c)].add((nr, nc))

    current = start
    distances = {node: sys.maxsize for node in edges}
    
    distances[current] = 0
    goal = end
    pq = [(0, current)]
    while pq:

        dist, current = heapq.heappop(pq)
        for neighbor in edges[current]:
            ndist = dist + risks[neighbor]            
            if ndist < distances[neighbor]:
                distances[neighbor] = ndist
                heapq.heappush(pq, (ndist, neighbor))
        #if distances[goal] != sys.maxsize:
        
    path = return_path(matrix, start, end, distances)
    visualise(matrix, path, distances)
            
    return distances[goal]
    
    
    return distances[goal]

def visualise(maze, path, distances):
    start = path[0]
    end = path[-1]
    
    pathimage = np.zeros(np.shape(maze),dtype=float)
    values = np.linspace(0.1, 0.9, num=len(path))
    dist_mat = np.zeros(np.shape(maze))
    
    for i in range(np.shape(maze)[0]):
        for j in range(np.shape(maze)[1]):
            dist_mat[i,j] = distances[(i,j)]

    cm = plt.get_cmap('viridis')
    maze_c = cm(normalise_data(dist_mat))
    
    values = np.linspace(0.5, 0.9, num=len(path))
    for i, p in enumerate(path):
        maze_c[p] = [(1*values[i]),0,0,1]
    
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax1.imshow(maze)
    ax2.imshow(maze_c)


def return_path(grid, start, end, distances):
    path = []
    path.append(end)
    
    pos = end
    
    while True:
        dists = []
        neighs = neighbours(grid, pos[0], pos[1])
        for n in neighs:
            dists.append(distances[n])
        
        ind = np.argmin(dists)
        pos = neighs[ind]
        path.append(pos)
        if pos == start:
            return path[::-1]
        
    
def neighbours(grid, x, y):
    out = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(a, b) for a, b in out if 0 <= a < np.shape(grid)[0] and 0 <= b < np.shape(grid)[0]]


def normalise_data(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))