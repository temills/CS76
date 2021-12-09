#!/usr/bin/env python3

#Tracey Mills, 10/21/21


from MapColoringProblem import MapColoringProblem
from CircuitLayoutProblem import CircuitLayoutProblem
from BONUS_CircuitLayoutProblem import BONUS_CircuitLayoutProblem
from BacktrackingSolver import *

"""
map1 = {'WA':['NT','SA'],'NT':['WA','SA','Q'],'SA':['WA','NT','Q','NSW','V'],'Q':['NT','SA','NSW'],'NSW':['Q','SA','V'],'V':['SA','NSW'],'T':[]}
colors1 = ['red','green','blue']
mapProb1 = MapColoringProblem(map1, colors1)
result = backtracking_search(mapProb1.csp)
print(result)
mapProb1.print_result(result)
"""

"""
board1 = ['..........','..........','..........']
components1 = [['aaa','aaa'],['bbbbb','bbbbb'],['cc','cc','cc'],['eeeeeee']]
circuitProb1 = CircuitLayoutProblem(board1,components1)
result = backtracking_search(circuitProb1.csp)
circuitProb1.print_result(result)
"""

"""
board2 = ['..............','...............','...............','..............','...............','...............','..............','...............','...............','...............']
components2 = [['a','a'],['b','b'],['c'],['eeeeeee'],['f','f','f','f','f','f','f'],['gggggggggg','gggggggggg','gggggggggg','gggggggggg'],['hhhhhh','hhhhhh'],['ii','ii','ii','ii'],['jjjjjjj','jjjjjjj','jjjjjjj'],['hhhhhh','hhhhhh']]
circuitProb2 = CircuitLayoutProblem(board2,components2)
result = backtracking_search(circuitProb2.csp)
circuitProb2.print_result(result)
"""

#Bonus version
"""
board2 = ['..............','...............','...............','..............','...............','...............','..............','...............','...............','...............']
components2 = [['a','a'],['b','b'],['c'],['eeeeeee'],['f','f','f','f','f','f','f'],['gggggggggg','gggggggggg','gggggggggg','gggggggggg'],['hhhhhh','hhhhhh'],['ii','ii','ii','ii'],['jjjjjjj','jjjjjjj','jjjjjjj'],['hhhhhh','hhhhhh']]
circuitProb2 = BONUS_CircuitLayoutProblem(board2,components2)
result = backtracking_search(circuitProb2.csp)
circuitProb2.print_result(result)
"""

"""
board2 = ['..............','...............','...............','..............','...............','...............','..............','...............','...............','...............']
components2 = [['aaa','aaa'],['bbbbb','bbbbb'],['cc','cc','cc'],['eeeeeee'],['f','f','f','f','f','f','f'],['gggggggggg','gggggggggg','gggggggggg','gggggggggg'],['hhhhhh','hhhhhh'],['ii','ii','ii','ii'],['jjjjjjj','jjjjjjj','jjjjjjj']]
circuitProb2 = CircuitLayoutProblem(board2,components2)
result = backtracking_search(circuitProb2.csp)
circuitProb2.print_result(result)
"""

"""
board3 = ['...................', '...................', '...................', '...................', '...................', '...................', '...................', '...................', '...................', '...................']
components3 = [['aaa','aaa'],['bbbbb','bbbbb'],['cc','cc','cc'],['eeeeeee'],['f','f','f','f','f','f','f'],['gggggggggg','gggggggggg','gggggggggg','gggggggggg'],['hhhhhh','hhhhhh'],['ii','ii','ii','ii'],['jjjjjjjjjjjjjjjjjj','jjjjjjjjjjjjjjjjjj','jjjjjjjjjjjjjjjjjj'],['kkkk','kkkk','kkkk'],['l','l','l','l','l','l','l','l','l','l'],['mmmmm']]
circuitProb3 = CircuitLayoutProblem(board3,components3)
result = backtracking_search(circuitProb3.csp)
circuitProb3.print_result(result)
"""
