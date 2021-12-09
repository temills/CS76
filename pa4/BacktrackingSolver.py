#Tracey Mills, 10/21/21

from math import inf
import queue

mrv = False
degree = False
lcv = False
ac3 = False

#backtracking search through variable assignments, until complete assignment is found
def backtracking_search(csp):
    return recursive_backtracking_search([-1]*csp.numVars, csp)

def recursive_backtracking_search(assignment, csp):
    print("here")
    #return assignment if complete
    if -1 not in assignment:
        return assignment
    #find unassigned variable
    var = select_unassigned_var(assignment, csp)
    #try out all values
    for val in get_vals(var, assignment, csp):
        assignment[var] = val
        #make sure assignment is consistent
        if csp.check(assignment):
            prev_domain = csp.domain
            csp.domain[var] = [val]
            print(sum([len(l) for l in csp.domain]))
            if(ac3):
                AC3(assignment, csp)    #update domains
            #print(sum([len(l) for l in csp.domain]))
            #recurse
            res = recursive_backtracking_search(assignment, csp)
            #if solved, return assignment
            if res == 'failure':
                print('failed!')
            if res != 'failure':
                return res
            csp.domain = prev_domain
        #otherwise unassign val to var
        assignment[var] = -1
    #if no val worked for this var, return failure
    return 'failure'

def select_unassigned_var(assignment, csp):
    if(degree):
        #degree heuristic
        return select_unassigned_var_degree(assignment, csp)
    elif(mrv):
        #mrv heuristic
        return select_unassigned_var_mrv(assignment, csp)
    else:
        #naive
        for var in range(len(assignment)):
            if assignment[var]==-1:
                return var

#choose var with least remaining legal values
def select_unassigned_var_mrv(assignment, csp):
    counts = [float(inf)]*len(assignment)
    for var in range(len(assignment)):
        if assignment[var]==-1:
            #count num legal values for unassigned var
            count=0
            for val in csp.domain[var]:
                assignment[var] = val
                if csp.check(assignment):
                    count = count+1
            counts[var] = count
            assignment[var] = -1
    #return var with min num legal values
    return counts.index(min(counts))

#choose var with least remaining legal values,
#and greatest involvement in constraints on other vars
def select_unassigned_var_degree(assignment, csp):
    counts = [float(inf)]*len(assignment)
    for var in range(len(assignment)):
        if assignment[var]==-1:
            #count num legal values for unassigned var
            count=0
            for val in csp.domain[var]:
                assignment[var] = val
                if csp.check(assignment):
                    count = count+1
            counts[var] = count
            assignment[var] = -1
    #find vars with min num legal values
    minVars = [i for i in range(len(counts)) if counts[i] == min(counts)]
    #no need for degree heuristic
    if len(minVars)==1:
        return minVars[0]
    #get degree for each var as sum of possible values for each (var, unassigned var) pair
    counts = [float(inf)]*len(assignment)
    for var in minVars:
        count = 0
        for var2 in range(len(assignment)):
            if assignment[var2] == -1 and var != var2:
                count = count + len(csp.constraints[tuple(sorted([var,var2]))])
        counts[var] = count
    #return var with min count, which is most constraining on unassigned vars
    return counts.index(min(counts))

#get possible values for given var
def get_vals(var, assignment, csp):
    if(lcv):
        return get_lcv(var, assignment, csp)
    else:
        return csp.domain[var]

#gets value assignment for given variable that constrains other variables the least
#value such that sum of legal vals for other unassigned vars is maximized
def get_lcv(var, assignment, csp):
    #try out each possible value
    num_legal_vals = {}
    for val in csp.domain[var]:
        num_legal_vals[val] = 0
        assignment[var] = val
        #given assignment, get num legal values for each unassigned var
        for otherVar in range(len(assignment)):
            if assignment[otherVar]==-1:
                #count num legal values for unassigned var
                count=0
                for v in csp.domain[otherVar]:
                    assignment[otherVar] = v
                    if csp.check(assignment):
                        count = count+1
                num_legal_vals[val] = num_legal_vals[val] + count
                assignment[otherVar] = -1
    assignment[var] = -1
    #return val that allows for most legal value assignments of other vars
    return(sorted(num_legal_vals.keys(), key=lambda k: num_legal_vals[k], reverse=True))

#Arc consistency heuristic, updates variable domains
def AC3(assignment, csp):
    #create queue with arcs between each var
    q = queue.Queue()
    for v1 in range(len(assignment)):
        for v2 in range(len(assignment)):
            if v1 != v2:
                q.put((v1,v2))
    #go thru arcs and check for consistency
    while(not q.empty()):
        arc = q.get()
        if remove_inconsistent(arc, assignment, csp):
            for v in range(len(assignment)):
                #not same var, or var we just checked consistency with
                if v != arc[0] and v != arc[1]:
                    q.put((v, arc[0]))

#helper for AC3, given arc, removes inconsistent values from domain of first var
def remove_inconsistent(arc, assignment, csp):
    removed = False
    new_domain = []
    #check each value for first var
    for val1 in csp.domain[arc[0]]:
        ok = False
        #go thru possible vals for second var
        for val2 in csp.domain[arc[1]]:
            if arc[0]<arc[1]:
                tup = (val1,val2)
            else:
                tup=(val2,val1)
            if tup in csp.constraints[tuple(sorted([arc[0],arc[1]]))]:
                ok = True
        if ok:
            #keep val1 in domain of arc[0]
            new_domain.append(val1)
    if len(new_domain) < len(csp.domain[arc[0]]):
        removed = True
    csp.domain[arc[0]] = new_domain
    return removed
