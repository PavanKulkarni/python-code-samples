import random

class RandomKey():
    def __init__(self):
        self.hashmap = {}
        self.random_array = []

    def insert(self, key, value):
        self.random_array.append(key)
        self.hashmap[key] = (value, len(self.random_array)-1)

    def get(self, key):
        if key not in self.hashmap:
            return 'Key doesnt exits %s '% key
        return self.hashmap[key][0]

    def delete(self, key):
        random_index = self.hashmap[key][1]
        last_index = self.random_array[-1]
        self.random_array[random_index], self.random_array[-1] = self.random_array[-1], self.random_array[random_index]
        self.hashmap[last_index] = (self.hashmap[last_index][0], random_index)
        del self.hashmap[key]
        self.random_array.pop()

    def getRandomKey(self):
        random_key = self.random_array[random.randint(0, len(self.random_array)-1)]
        return self.get(random_key)

if __name__=='__main__':
    r = RandomKey()
    r.insert('a', 1)
    r.insert('b', 2)
    r.insert('c', 3)
    r.insert('d', 4)
    r.insert('e', 5)
    r.insert('f', 6)
    print r.get('a')
    print r.get('b')
    print 'Random Key is %s' %r.getRandomKey()
    r.delete('b')
    print r.get('b')
    print 'Random Key is %s' % r.getRandomKey()




