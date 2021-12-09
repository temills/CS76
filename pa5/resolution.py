# Tracey Mills 10/30/21

# Resolution
def resolution(clauses, vars):
    new_clauses = []
    #iterate thru clauses
    for c1 in clauses:
        #for each var in clause
        for v in c1:
            #check all other clauses for -v
            for c2 in clauses:
                if -v in c2:
                    #take out v and put c1 and c2 together (resolution)
                    new_clause = []
                    for var in c1:
                        if (var != v) and (var not in new_clause):
                            new_clause.append(var)
                    for var in c2:
                        if (var != -v) and (var not in new_clause):
                            new_clause.append(var)
                    new_clauses.append(new_clause)
    #add new clauses to original clauses and return
    for clause in new_clauses:
        if clause not in clauses:
            clauses.append(clause)
    return clauses