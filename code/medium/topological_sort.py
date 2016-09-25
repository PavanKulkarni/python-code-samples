

def topo_sort(graph, start):
    global_stack = []
    visited = set()
    stack = [start]
    while len(stack):
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print "Visited %s" % vertex
            if not graph[vertex]:
               # No more children hence add
               global_stack.append(vertex)
            stack.extend(graph[vertex] - set(vertex))
        else:
            global_stack.append(vertex)
        
    return visited, global_stack




if __name__=='__main__':
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}
    print graph
    print topo_sort(graph, 'C')
