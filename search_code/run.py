# Search methods

import search
import utils

ab = search.GPSProblem('A', 'B', search.romania)

#print "Busqueda en anchura"
#print search.breadth_first_graph_search(ab).path()

#print "Busqueda en profundidad"
#print search.depth_first_graph_search(ab).path()
#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()

#print search.astar_search(ab).path()

print "Ramificacion por coste"
print search.RMporCoste(ab).path()

print "Ramificacion por coste y euristica"
print search.RMporCosteHeuristica(ab).path()



# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
