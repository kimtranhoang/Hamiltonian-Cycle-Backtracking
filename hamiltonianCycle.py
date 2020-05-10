class Graph():
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]
                            for row in range(vertices)]
        self.V = vertices

    def value(self, v, pos, path):
        if self.graph[path[pos-1], [v]] == 0:
            return False

        for vertex in path:
            if vertex == v:
                return False

        return True
    def hamCycleUtil(self, path, pos):  
        if pos == self.V:  
            # Last vertex must be adjacent to the  
            # first vertex in path to make a cyle  
            if self.graph[ path[pos-1] ][ path[0] ] == 1:  
                return True
            else:  
                return False
  
        # Try different vertices as a next candidate  
        # in Hamiltonian Cycle.  
        for v in range(1,self.V):  
  
            if self.isSafe(v, pos, path) == True:  
  
                path[pos] = v  
  
                if self.hamCycleUtil(path, pos+1) == True:  
                    return True
  
                # Remove current vertex if it doesn't  
                # lead to a solution  
                path[pos] = -1
  
        return False
  
    def hamCycle(self):  
        path = [-1] * self.V  
  
        path[0] = 0
  
        if self.hamCycleUtil(path,1) == False:  
            print ("Solution does not exist\n") 
            return False
  
        self.printSolution(path)  
        return True
  
    def printSolution(self, path):  
        print ("Solution Exists: Following", 
                 "is one Hamiltonian Cycle") 
        for vertex in path:  
            print (vertex, end = " ") 
        print (path[0], "\n") 