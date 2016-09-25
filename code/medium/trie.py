class TrieNode():

    def __init__(self, val):
        self.val = val
        self.child_pointer = {}
        self.end_node = True
        
    def addChild(self, val):
        if val is None:
            return None
        if val in self.child_pointer:
            return True
        else:
            new_node = TrieNode(val)
            self.child_pointer[val] = new_node
        self.end_node = False


class Trie():

    def __init__(self):
        self.root = TrieNode(ord('-'))
    
    def _addChildString(self, string):
        node = self.root
        for char in string:
            ordinal = ord(char)
            if ordinal not in node.child_pointer:
                print "%s not in Trie for %s hence adding it now" % (char, string)
                node.addChild(ordinal)
            else:
                print "%s already exist in Trie for %s" %(char, string)
            node = node.child_pointer[ordinal]
        node.end_node = True
        
    def addString(self, string):
        self._addChildString(string[0:])

    def get_root(self):
        return self.root

    def printTrie(self, res = [], final_result = [], node=None):
        if node is None:
            node = self.root
        if node.end_node:
            res.append(chr(node.val))
            final_result.append([x for x in res[0:]])
            return
        res.append(chr(node.val))
        for i in node.child_pointer.keys():
            if node == self.root:
                 res = []
            self.printTrie(res, final_result, node.child_pointer[i])
        return final_result

if __name__=='__main__':
    trie = Trie()
    trie.addString('abc')
    trie.addString('abd')
    trie.addString('shruthi')
    trie.addString('shruthi123')
    print trie.printTrie()
