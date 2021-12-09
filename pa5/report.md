# CS76, Fall 2021, Assignment 5, Tracey Mills
## Description
I used the provided code to store and display the puzzles, as well as the provided solve_sudoku.py file to set the random seed, run the SAT algorithms, and output the result. I wrote a SAT.py file to imoplement the SAT algorithms. In this file there is a SAT class which stores variables in their original and translated forms, clauses, the threshold value, max iterations, and the solution (which starts off as None) as instance variables. An instance of the class is created by passing in a .cnf file, which is read line by line, interpreted as one clause per line and variables separated by spaces. Variables are translated to integer values by putting them in a sorted list and then taking their indexes in this list (starting with index 1). A negated variable is indicated by a negative integer number, so not(1) = -1.  
Gsat and Walksat are implemented as desscribed in the instructions.  

## Evaluation
Both algorithms work as expected.  
Gsat solves one_cell in 6 iterations, all_cells in ~400 iterations, and rows in ~700 iterations, but runs for several minutes and iterates more than 2000 times before finding a solution for the other problems.  
As exepected due to its considering fewer variables for flipping, Walksat solves the problems more quickly. Walksat solves one_cell in 6 iterations, all_cells in ~400 iterations, and rows in ~900 iterations, rows_and_cols in ~9000 iterations, rules in ~10000 iterations, puzzle1 in ~60000 iterations, and puzzle2 in ~150000 iterations. It solves the first 5 in under a minute, and the last 2 puzzles in a couple minutes.

## BONUS
I also briefly implemented a resolution option in the init function by taking the initial clauses and performing resolution on each pair of clauses possible (in which one clause contains variable v, the other contains -v). I then added these resultant clauses to the list of clauses. This greatly increased the number of clauses (in res_test.cnf, resolution increased num clauses from 343 to 2943). Resolution is not likely to be helpful for the algorithm, since the new clause, by construction, do not add any additional information to the knowledge base (each was already entailed). However the process does better emulate the way many people might solve puzzles. For example, the initial res_test puzzle contains one 3x3 square containing all digits 1-9, and in which the top middle square is a 3. For example, through resolution with clauses -123 -124 and 123, the clause -124 could be added (the top middle square cannot be a 4). Then, by applying resolution again with clause 114 124 134 214 224 234 314 324 334, we can get the clause 114 134 214 224 234 314 324 334 (some square other than the top middle square must be a 4).


