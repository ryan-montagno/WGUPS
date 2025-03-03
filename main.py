
import csv
import datetime

from PackageModule import Package
from HashModule import PackageHash
from TruckModule import Truck


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

    addresses = list(csvFile3)

#Takes an address (string) and returns its ID (int). For use with getDistance
def getAddrID(address):

    #Checks each adress in the list and return index of match (address ID)
    for i in range(len(addresses)):
        if addresses[i][1] == address:
            return int(i)
        i = i+1
    return -1

#Takes two address ID's and gets the distance between the two from the distances list
def getDistance(a, b):

    #Uses logic to account for distances.csv only having half of the distances table
    if distances[a][b] == "":
        return float(distances[b][a])
    return float(distances[a][b])

def timeToDeliver(distance, speed):

    return ((distance / speed) * 60)

def deliver(truck):

    undeliveredPackages = []
    deliveredPackages = []
    deliveryTime= 0
    for item in truck.packages:
        undeliveredPackages.append(packageHash.search(item))

    currentAddr = truck.startingAddr
    currentPackage = None
    currentDistance = 20

    while len(undeliveredPackages) > 0:

        for package in undeliveredPackages:

            if getDistance(getAddrID(currentAddr), getAddrID(package.address)) < currentDistance:
                currentDistance = getDistance(getAddrID(currentAddr), getAddrID(package.address))
                currentAddr = package.address
                currentPackage = package


        undeliveredPackages.remove(currentPackage)
        deliveredPackages.append(currentPackage)
        truck.addMilesDriven(currentDistance)
        deliveryTime += timeToDeliver(currentDistance, truck.speedLimit)
        currentDistance = 20

    for package in deliveredPackages:
        print (package.id)

    print(truck.milesDriven)
    print(deliveryTime)




class Main:

    print("Welcome to WGUPS!")

    print("Loading Trucks...")
    truck1 = Truck(1, 18, 0, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 16, "4001 South 700 East",
                   datetime.timedelta(hours=8))

    truck2 = Truck(1, 18, 0, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 16, "4001 South 700 East",
                   datetime.timedelta(hours=9, minutes=5))

    truck3 = Truck(1, 18, 0, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 16, "4001 South 700 East",
                   datetime.timedelta(hours=10, minutes=20))

    print("Trucks departing hub...")
    print("Packages out for delivery...")
    print("What would you like to do?")

    usertime = input("Enter a time: ")

    (h, m) = usertime.split(":")

    time = datetime.timedelta(hours=int(h), minutes=int(m))

    print(time)




######TESTING#################################################################################
# packageHash.insert(45, Package(45, "8389 street", "philly", "pa", "928393", "2:30pm", 45, "This is a test package", "On time"))
# packageHash.remove(14)
# print(len(packageHash.hashTable))
# packageHash.resize()
# print(len(packageHash.hashTable))
# print(packageHash.search(14))
#
# for bucket in packageHash.hashTable:
#    for package in bucket:
#         print(package)
#
# for item in distances:
#    print(item)
#
# for address in addresses:
#    print(f"{getAddrID(address[1])} {address}")
#
# myTruck = Truck(1, 45, 0, [], 40, "123 street road", 800)
#
# print(myTruck)
# print(getDistance(2, 8))
#
# print(getAddrID("2300 Parkway Blvd"))
#
# print(truck1)
# print(truck2)
# print(truck3)
###################################################################################################















