#Class for solving circuit layout csp
#Tracey Mills, 10/21/21

from ConstraintSatisfactionProblem import ConstraintSatisfactionProblem

class CircuitLayoutProblem():

    def __init__(self, board, components):
        self.board = board
        self.nRows = len(board)
        self.nCols = len(board[0])
        self.components = tuple(components)
        self.locations = list(range(self.nRows*self.nCols)) #location = y*nCols + x
        self.locationDict = {}
        #x,y location to indexed location mapping
        for y in range(self.nCols):
            for x in range(self.nRows):
                self.locationDict[(x,y)] = y*self.nCols + x
        #domain of each component is all possible x,y locations of bottom left corner
        domain = []
        for comp in self.components:
            h = len(comp)
            w = len(comp[0])
            yVals = list(range(self.nRows-h+1))
            xVals = list(range(self.nCols-w+1))
            compLocs = []
            for y in yVals:
                for x in xVals:
                    #compLocs.append((x,y))
                    compLocs.append(y*self.nCols + x)
            domain.append(compLocs)
        #constraints between components require no overlap
        constraints = {}
        #choose first component
        for i in range(len(self.components)):
            comp1 = self.components[i]
            for j in range(len(self.components)):
                #ignore if same component
                if i == j:
                    continue
                comp2 = self.components[j]
                #get possible location pairs for this component pair
                #for all locs in each domain, which do not overlap?
                noOverlap = []
                #try out each location for first component
                for loc1 in domain[i]:
                    y1 = int(loc1/self.nCols)
                    x1 = loc1 - (y1*self.nCols)
                    xMin1 = x1
                    xMax1 = x1 + len(comp1[0]) - 1
                    yMin1 = y1
                    yMax1 = y1 + len(comp1) - 1
                    #try out each location for second component
                    for loc2 in domain[j]:
                        y2 = int(loc2/self.nCols)
                        x2 = loc2 - (y2*self.nCols)
                        xMin2 = x2
                        xMax2 = x2 + len(comp2[0]) - 1
                        yMin2 = y2
                        yMax2 = y2 + len(comp2) - 1
                        #if no overlap, add location pair to constraint
                        if (xMax2 < xMin1 or xMin2 > xMax1 or yMax2 < yMin1 or yMin2 > yMax1):
                            #correctly order locations since stored in dictionary with ordered tuple as key
                            if i<j:
                                noOverlap.append((loc1, loc2))
                            else:
                                noOverlap.append((loc2, loc1))                   
                constraints[tuple(sorted([i,j]))] = noOverlap
        print(constraints)
        self.csp = ConstraintSatisfactionProblem(domain, constraints)

    def __str__(self):
        string =  "circuit layout: "
        return string

    def print_result(self, assignment):
        if assignment == 'failure':
            print('Failure')
        else:
            board=[]
            for i in range(self.nRows):
                board.append(['.']*self.nCols)
            print("Circuit:")
            for i in range(len(assignment)):
                loc = assignment[i]
                y = int(loc/self.nCols)
                x = loc - (y*self.nCols)
                comp = self.components[i]
                compChar = comp[0][0]
                #left to right starting with x
                for c in range(x, x+len(comp[0])):
                    #bottom to top starting with y
                    for r in range(self.nRows-y-len(comp), self.nRows-y):
                        board[r][c] = compChar
            s = ""
            for row in board:
                print(s.join(row))