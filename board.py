

def cmp(i, j, dim):
    return 0 <= i < dim and 0 <= j < dim


class Cell:
    
    def __init__(self, i, j, dim):
        self.__i = i
        self.__j = j
        self.__dim = dim
        
        self.__visited = False
    
    def visit(self):
        self.__visited = True
    
    def unvisit(self):
        self.__visited = False
    
    def was_visited(self):
        return self.__visited
    
    def get_i(self):
        return self.__i
    
    def get_j(self):
        return self.__j
    
    def get_dim(self):
        return self.__dim
    
    def __str__(self):
        return str((self.__i, self.__j))


class Grid:
    
    def __init__(self, dim, cell_dim):
        self.__dim = dim
        self.__grid = [[Cell(i, j, cell_dim) for j in range(self.__dim)] for i in range(self.__dim)]
    
    def get_dim(self):
        return self.__dim
    
    def get_cell(self, i, j):
        return self.__grid[i][j]
    
    def unvisit_all_cells(self):
        for v in self.__grid:
            for cell in v:
                cell.unvisit()
    
    def get_neighbors(self, i, j):
        neighbors = []
        if cmp(i-1, j, self.__dim):
            neighbors.append(self.get_cell(i-1, j))
        if cmp(i+1, j, self.__dim):
            neighbors.append(self.get_cell(i+1, j))
        if cmp(i, j-1, self.__dim):
            neighbors.append(self.get_cell(i, j-1))
        if cmp(i, j+1, self.__dim):
            neighbors.append(self.get_cell(i, j+1))
        return neighbors
    
    def get_not_visited_neighbors(self, i, j):
        neighbors = self.get_neighbors(i, j)
        res = []
        for cell in neighbors:
            if not cell.was_visited():
                res.append(cell)
        return res
    
    def number_visited_cells(self):
        n = 0
        for v in self.__grid:
            for cell in v:
                if cell.was_visited():
                    n += 1
        return n


class Tree:
    
    def __init__(self, info):
        self.__info = info
        self.__links = []
    
    def add_child(self, child):
        assert isinstance(child, Tree), "Error: child is not a Tree"
        self.__links.append(child)
    
    def children(self):
        return self.__links
    
    def __str__(self):
        return str(self.__info)
    
