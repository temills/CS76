# Proof of solvability of sensorless problem in polynomial time
To prove that a sensorless plan of the type implemented in this assignment always exists, I will first prove that it is
 possible to decrease the size of any belief state by at least 1 in polynomial time. A belief state is a set of locations
 in the nxn grid, representing the possible locations of the robot. After a move N, S, E, or W, the belief state may change.
 For each location l in the belief state, l maps to the location of a robot that started at l and attempted to make the specified
 move. Thus, if a robot moving from l would move into a wall or an obstacle, the robot cannot move, and so l maps to l. If
 a robot moving from l would move into a floor space, then l maps to this floor space. Thus, each location in the belief state maps
 to 1 new location in the new belief state, with some locations potentially mapping to the same new location. This means that after
 each move the number of locations in the belief state either decreases or stays the same.  
The size of the belief state decreases when two locations l1 and l2 map to the same new location. This occurs when, in the direction of the move,
there is l1, l2, and then an obstacle or a wall. l1 and l2 both then map to l2 after the move. Let's call such a mapping the desired mapping.
We can reach the desired mapping from any belief state in polynomial time as follows:  
First, take two possible locations l1 and l2 within the connected component containing the goal (if there is only one such location, then either the
 robot is at this location and we are done, or the goal is not reachable). Then, find the shortest path, p, between l1 and l2 using BFS.
 This can be done in O(n^2) time. Let this path contain e moves East, w moves West, s South, and n North. Then, move according to p.
l1 has now mapped to l1'=l2. l2 maps to some location l2' such that the path between l2' contains at most e moves East, w moves West, s moves South,
and n moves North, since a robot starting at l2 and taking each move in p would either do the move or remain in the same place (if stopped 
by an obstacle) for each move. Thus, the shortest path p' between l1' and l2' now contains the same moves as the path between l2 and l2'. 
By the logic above, p' is at most as long as p. Since p must move the locations at least one step N,S,E, or W (otherwise l1=l2), we can take p 
from l1 or l2 at most n times before running off the edge of the grid. So, the length of the path between l1 and l2 must decrease at least once
every n times a path is taken. So, we take a given path at most n times before taking a shorter path. Since there are n^2 locations, 
the original path can be at most n^2 moves long, and so we will have to take at most n^2 paths n times each before l1 reaches l2, giving us
 the desired mapping.
 With this desired mapping, the belief state decreases in size by at least 1.  

Since we start with at most n^2 possible locations in the belief state, this process will have to be repeated at most n^2 time before the number 
of possible locations has been reduced to 1. Thus, we can solve the problem in polynomial time over n, using a motion planner as described above.