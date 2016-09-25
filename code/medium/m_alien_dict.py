
class Node():

    def __init__(self, val=None):
        self.val = val
        self.children = {}

    def add_child(self, child):
        if child not in self.children:
            self.children[child] = Node()

def alien_dict(words):
    graph = {}
    tree = Node()

    for word in words:
        node = tree
        for c in word:
            for x in node.children:
                if x not in graph:
                    graph[x] = []
                if x != c:
                    graph[x].append(c)
            if c not in node.children:
                node.add_child(c)
            node = node.children[c]
    return graph


if __name__=='__main__':
    words = ['wrt', 'wrf', 'er', 'ett', 'rftt']
    print alien_dict(words)
