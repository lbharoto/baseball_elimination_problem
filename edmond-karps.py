import decimal
import sys

def EdmondsKarp(capacity, neighbors, start, end):
  flow = 0
  length = len(capacity)
  flows = [[0 for i in range(length)] for j in range(length)]
  while True:
    max, parent = BreadthFirstSearch(capacity, neighbors, flows, start, end)
    if max == 0:
      break
    flow = flow + max
    v = end
    while v != start:
      u = parent[v]
      flows[u][v] = flows[u][v] + max
      flows[v][u] = flows[v][u] - max
      v = u
  return (flow, flows)

def BreadthFirstSearch(capacity, neighbors, flows, start, end):
  length = len(capacity)
  parents = [-1 for i in range(length)] 
  parents[start] = -2 
  M = [0 for i in range(length)] 
  M[start] = decimal.Decimal('Infinity') 

  queue = []
  queue.append(start)
  while queue:
    u = queue.pop(0)
    for v in neighbors[u]:
    
      if capacity[u][v] - flows[u][v] > 0 and parents[v] == -1:
        parents[v] = u
       
        M[v] = min(M[u], capacity[u][v] - flows[u][v]) 
        if v != end:
          queue.append(v)
        else:
          return M[end], parents
  return 0, parents

def ParseGraph(file):
  file_object = open(file, "r")
  capacity = []
  neighbors = {} 
  for line in file_object.readlines():
    capacity.append([int(i) for i in line.split(',')])
  for vertex in range(len(capacity)):
    neighbors[vertex] = []
  for vertex, flows in enumerate(capacity):
    for neighbor, flow in enumerate(flows):
      if flow > 0:
        neighbors[vertex].append(neighbor)
        neighbors[neighbor].append(vertex)
  return capacity, neighbors

if __name__ == "__main__":
  file_name = sys.argv[1] 
  capacity, neighbors = ParseGraph(file_name)
  
  #question1:
  flow, flows = EdmondsKarp(capacity, neighbors, 0, 13)
  
  #question2:
  #flow, flows = EdmondsKarp(capacity, neighbors, 0, 13)
  
  #question3:
  #flow, flows = EdmondsKarp(capacity, neighbors, 0, 18)
  print('Max flow: %s' % flow)
  