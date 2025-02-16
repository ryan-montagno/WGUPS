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
        bucket = hash(key % self.capacity)
        bucketlist = self.hashTable[bucket]
        if value not in bucketlist:
            bucketlist.append(value)

    def search(self, key):
        bucket = hash(key % self.capacity)
        bucketlist = self.hashTable[bucket]
        if key in bucketlist:
            return bucketlist.index(key)
        return -1

    def remove(self, key):
        bucket = hash(key % self.capacity)
        bucketlist = self.hashTable[bucket]
        if key in bucketlist:
            bucketlist.remove(key)
            return True
        return False