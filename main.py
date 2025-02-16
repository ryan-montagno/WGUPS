import string
import random

from PackageModule import Package
from HashModule import Hash

package = Package(5, "123 street road", "Ridley", "PA", "12345", "10:30", 100, "Deliver by 10:30", "On time")
hashTable = Hash(40)

list = []
randNum = 0

class testItem:

    def __init__(self, id, string):
        self.id = id
        self.string = string

for i in range(40):
    randNum = random.randint(1, 39)
    list.append(testItem(randNum, f'I am {randNum}'))
    print (list[i-1].id)

for i in range(40):
    hashTable.insert(list[i-1].id, list[i-1].string)

for i in range(40):
    chain = hashTable.table[i-1]
    for item in chain:
        print (f'{i} {item}')




