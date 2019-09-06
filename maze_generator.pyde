
from board import *
import random as rd

def create_path(g):
    path = []
    
    stack = []
    
    current_cell = g.get_cell(0, 0)
    current_cell.visit()
    
    while g.get_dim()**2 - g.number_visited_cells() != 0:
        n = g.get_not_visited_neighbors(current_cell.get_i(), current_cell.get_j())
        if len(n) > 0:
            neighbour = rd.choice(n)
            stack.append(current_cell)
            
            path.append((current_cell, neighbour))
            
            current_cell = neighbour
            current_cell.visit()
        else:
            current_cell = stack.pop()
    g.unvisit_all_cells()
    return path

def create_tree(grid, path):
    # Crear matriz de adyacencia
    dim = grid.get_dim()
    dic = {}
    
    for a, b in path:
        if a not in dic:
            dic[a] = [b]
        else:
            dic[a].append(b)
        if b not in dic:
            dic[b] = [a]
        else:
            dic[b].append(a)
    return dic

def draw_maze():
    stroke(255)
    strokeWeight(20)
    for k, v in tree.items():
        for e in v:
            line(k.get_i()*k.get_dim() + k.get_dim()/2, k.get_j()*k.get_dim() + k.get_dim()/2,
                 e.get_i()*e.get_dim() + k.get_dim()/2, e.get_j()*e.get_dim() + k.get_dim()/2)

def setup():
    size(500, 500)
    
    global dim
    dim = 10
    
    global ie, je
    ie, je = dim-1, dim-1
    
    global g
    g = Grid(dim, width/dim)
    path = create_path(g)
    
    global tree
    tree = create_tree(g, path)
    
    global stack
    stack = [g.get_cell(0,0)]
    
    global parent
    parent = {}
    
    global current_cell
    current_cell = g.get_cell(0,0)


import time



def draw():
    
    background(0)
    draw_maze()
    
    stroke(255, 0, 0)
    strokeWeight(10)
    
    global current_cell
    if len(stack) > 0 and not (current_cell.get_i() == ie and current_cell.get_j() == je):
        current_cell = stack.pop(0)
        current_cell.visit()
        
        point(current_cell.get_i()*current_cell.get_dim() + current_cell.get_dim()/2, current_cell.get_j()*current_cell.get_dim() + current_cell.get_dim()/2)
        
        neighbors = tree[current_cell]
        for cell in neighbors:
            if not cell.was_visited():
                cell.visit()
                stack.append(cell)
                parent[cell] = current_cell
    else:
        if g.get_cell(ie, je) not in parent:
            print("No solution found!")
        else:
            path = []
            # Found path
            prev_cell = g.get_cell(ie,je)
            cell = parent[prev_cell]
            while cell is not g.get_cell(0,0):
                path.append(cell)
                prev_cell = cell
                cell = parent[prev_cell]
            path.append(g.get_cell(0, 0))
            path.insert(0, g.get_cell(ie,je))
            
            # Display path
            for i in range(len(path)-1):
                line(path[i].get_i()*current_cell.get_dim() + current_cell.get_dim()/2, 
                     path[i].get_j()*current_cell.get_dim() + current_cell.get_dim()/2, 
                     path[i+1].get_i()*current_cell.get_dim() + current_cell.get_dim()/2, 
                     path[i+1].get_j()*current_cell.get_dim() + current_cell.get_dim()/2)
            
            noLoop()
    time.sleep(0.05)
    
