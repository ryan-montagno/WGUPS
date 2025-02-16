from operator import truediv


#Hash table class. Implements a has table with chaining

class Hash:

    capacity = 1
    table =[]

    #Initializes a Has object
    def __init__ (self, capacity):
        #The hash table
        table = []
        capacity = int(capacity)

        #Addss chains(lists) to the hash table. 'capacity' should be set to number of packagaes being delivered
        for i in range(capacity):
            self.table.append([])

    def insert (self, key, value):
        bucket = hash(key) % self.capacity
        chain = self.table[bucket]
        if value not in chain:
            chain.append(value)

    def search(self, key):
        bucket = hash(key) % self.capacity
        chain = self.table[bucket]
        if key in chain:
            return chain.index(key)
        return -1

    def remove(self, key):
        bucket = hash(key) % self.capacity
        chain = self.table[bucket]
        if key in chain:
            chain.remove(key)
            return True
        return False