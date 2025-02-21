
import csv

from PackageModule import Package
from HashModule import PackageHash

#Create the hashtable to hold packages. Takes the number of packages as param
packageHash = PackageHash(40)

#Reads in packages csv file and loads packages into hash table
with open("./assets/packages.csv", mode="r") as file:

    csvFile = csv.reader(file)

    #Inserts each package into the hash table
    for lines in csvFile:
        packageHash.insert(int(lines[0]), Package(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], int(lines[6]), lines[7], lines[8]))

#Reads in distance csv file places distances in a list
with open("./assets/distances.csv", mode="r") as file2:

    csvFile2 = csv.reader(file2)

    distances = list(csvFile2)

#Reads in addresses file and places them in a list
with open("assets/addresses.csv", mode="r") as file3:

    csvFile3 = csv.reader(file3)

    adresses = list(csvFile3)

#packageHash.insert(45, Package(45, "8389 street", "philly", "pa", "928393", "2:30pm", 45, "This is a test package", "On time"))
# packageHash.remove(14)
# print(len(packageHash.hashTable))
# packageHash.resize()
# print(len(packageHash.hashTable))
# print(packageHash.search(14))

# for bucket in packageHash.hashTable:
#    for package in bucket:
#         print(package)
#
# for item in distances:
#     print(item)
#
# for addrress in adresses:
#     print(addrress)















