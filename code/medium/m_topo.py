

def topo(graph_unsorted):
    graph_sorted = []

    # Convert the unsorted graph into a hash table. This gives us
    # constant-time lookup for checking if edges are unresolved, and
    # for removing nodes from the unsorted graph.
    graph_unsorted = dict(graph_unsorted)

    # Run until the unsorted graph is empty.
    while graph_unsorted:

        # Go through each of the node/edges pairs in the unsorted
        # graph. If a set of edges doesn't contain any nodes that
        # haven't been resolved, that is, that are still in the
        # unsorted graph, remove the pair from the unsorted graph,
        # and append it to the sorted graph. Note here that by using
        # using the items() method for iterating, a copy of the
        # unsorted graph is used, allowing us to modify the unsorted
        # graph as we move through it. We also keep a flag for
        # checking that that graph is acyclic, which is true if any
        # nodes are resolved during each pass through the graph. If
        # not, we need to bail out as the graph therefore can't be
        # sorted.
        acyclic = False
        import pdb;pdb.set_trace()
        for node, edges in graph_unsorted.items():
            for edge in edges:
                if edge in graph_unsorted:
                    break
            else:
                acyclic = True
                del graph_unsorted[node]
                graph_sorted.append((node, edges))

        if not acyclic:
            # Uh oh, we've passed through all the unsorted nodes and
            # weren't able to resolve any of them, which means there
            # are nodes with cyclic edges that will never be resolved,
            # so we bail out with an error.
            raise RuntimeError("A cyclic dependency occurred")

    return graph_sorted



if __name__=='__main__':
    graph = [(2, []),
                  (5, [11]),
                  (11, [2, 9, 10]),
                  (7, [11, 8]),
                  (9, []),
                  (10, []),
                  (8, [9]),
                  (3, [10, 8])]
 
    print topo(graph)
