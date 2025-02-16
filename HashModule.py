from contextlib import nullcontext
from operator import truediv


#Hash hashTable class. Implements a has hashTable with chaining

class PackageHash:


    #Initializes a Has object
    def __init__ (self, capacity):
        #The hash table
        self.hashTable = []
        self.capacity = int(capacity)

        #Addss chains(lists) to the hash table. 'capacity' should be set to number of packagaes being delivered
        for i in range(capacity):
            self.hashTable.append([])

    def insert (self, key, value):
        bucket = self.hashTable[hash(key % self.capacity)]
        if value not in bucket:
            bucket.append(value)

    def search(self, key):
        bucket = self.hashTable[hash(key % self.capacity)]
        for item in bucket:
            if item.id == key:
                return item
        return False

    def remove(self, key):
        bucket = self.hashTable[hash(key % self.capacity)]
        for item in bucket:
            if item.id == key:
                bucket.remove(key)
                return True
        return False