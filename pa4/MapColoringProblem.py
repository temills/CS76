# Map coloring CSP problem
#Tracey Mills, 10/21/21

from ConstraintSatisfactionProblem import ConstraintSatisfactionProblem

class MapColoringProblem():

    def __init__(self, map, colors):
        #keep track of order of locations and colors to decode assignment
        self.locations = tuple(map.keys())
        self.colors = tuple(colors)
        #each loc in map can be any color
        domain = [list(range(len(colors)))] * len(self.locations)
        #adjacent locs must be different colors
        constraints = {}
        colorPairs = []
        difColorPairs = []
        for c1 in range(len(self.colors)):
            for c2 in range(len(self.colors)):
                colorPairs.append((c1,c2))
                if c1 != c2:
                    difColorPairs.append((c1,c2))
        for l1 in range(len(self.locations)):
            loc1 = self.locations[l1]
            for l2 in range(len(self.locations)):
                if l1 != l2:
                    loc2 = self.locations[l2]
                    if loc2 in map[loc1]:
                        constraints[tuple(sorted([l1, l2]))] = difColorPairs
                    else:
                        constraints[tuple(sorted([l1, l2]))] = colorPairs
        self.csp = ConstraintSatisfactionProblem(domain, constraints)

    def __str__(self):
        string =  "map-coloring: "
        return string

    def print_result(self, assignment):
        if assignment == 'failure':
            print('Failure')
        else:
            print("Location colors:")
            for i in range(len(assignment)):
                loc = self.locations[i]
                color = self.colors[assignment[i]]
                print(loc + ": " + color)
