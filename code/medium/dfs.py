

def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print "Visited %s" % vertex
            stack.extend(graph[vertex] - visited)
    return visited

def topo(graph, start, visited, stack):
     if start not in visited:
          visited.add(start)
     for i in graph[start]:
          if i not in visited:
              topo(graph, i, visited, stack)
     stack.append(start)
     return stack, visited
             


if __name__=='__main__':
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}
    print dfs(graph, 'C')
    topo_graph = {'A': set(['C']),
                  'B': set(['C', 'E']),
                  'C': set(['D']),
                  'D': set(['F']),
                  'E': set(['F']),
                  'F': set(['G']),
                  'G': set([])}
    visited = set()
    stack = []
    ret_stack,visited = topo(topo_graph, 'E', visited, stack)
    remaining_items = list(set(graph.keys()) - set(ret_stack))
    while (remaining_items):
        ret_stack, visited = topo(topo_graph, remaining_items[0], visited, stack)
        remaining_items = list(set(graph.keys()) - set(ret_stack))
    print ret_stack
        
