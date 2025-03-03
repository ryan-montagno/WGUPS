
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

    time =(distance / speed)

    hours = int(time)

    minutes = int((time * 60) % 60)

    return (datetime.timedelta(hours=hours, minutes=minutes))

def deliver(truck):

    #helper variables
    undeliveredPackages = []
    deliveredPackages = []

    #loads packages into a list for internal use
    for item in truck.packages:
        packageHash.search(item).timeDeparted = truck.startingTime
        undeliveredPackages.append(packageHash.search(item))


    #Sets starting values for delivery
    currentAddr = truck.startingAddr
    currentPackage = None
    currentDistance = 20

    #Run until all packages are delivered
    while len(undeliveredPackages) > 0:

        #Checks the distance form current address to each package
        for package in undeliveredPackages:
            #If the distance is smaller than the current distance, package is selected
            if getDistance(getAddrID(currentAddr), getAddrID(package.address)) < currentDistance:
                currentDistance = getDistance(getAddrID(currentAddr), getAddrID(package.address))
                currentPackage = package

        #Once shortest distance is found, variables are updated and package is removed form unDeliveredPackages
        currentAddr = currentPackage.address
        undeliveredPackages.remove(currentPackage)
        deliveredPackages.append(currentPackage)
        truck.addMilesDriven(currentDistance)
        truck.setCurrentTime(timeToDeliver(currentDistance, truck.speedLimit))
        currentPackage.timeDelivered = truck.currentTime
        currentDistance = 20


class Main:

    print("Welcome to WGUPS!")

    print("Loading Trucks...")
    truck1 = Truck(1, 18, 0, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 16, "4001 South 700 East",
                   datetime.timedelta(hours=8))

    truck2 = Truck(2, 18, 0, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 16, "4001 South 700 East",
                   datetime.timedelta(hours=10, minutes=20))

    truck3 = Truck(3, 18, 0, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 16, "4001 South 700 East",
                   datetime.timedelta(hours=9, minutes=5))

    print("Trucks departing hub...")
    print("Packages out for delivery...")
    print("\n\n")

    #Send trucks out for delivery. Truck2 has package 9 with wrong address.
    deliver(truck1)
    deliver(truck3)
    #Ensures Truck 2 does not leave until one other truck returns, but no earlier than 10:20 to account for package 9
    if min(truck1.currentTime, truck3.currentTime) > datetime.timedelta(hours=10, minutes=20):
        truck2.startingTime = min(truck1.currentTime, truck3.currentTime)

    deliver(truck2)
    print('Total miles driven by all trucks:')
    print(f'Truck 1: {truck1.milesDriven:.2f}')
    print(f'Truck 2: {truck2.milesDriven:.2f}')
    print(f'Truck 3: {truck3.milesDriven:.2f}')
    print(f'Total: {(truck1.milesDriven + truck2.milesDriven + truck3.milesDriven):.2f}')

    userTime = input("To begin, please enter a time(hh:mm): ")

    (h, m) = userTime.split(":")

    time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=0)

    print("\n\n")

    print("To see the status of a package, enter its ID.\n"
          "To see the status of all packages, enter \"All\"\n")

    userInput = input("What would you like to do? ")

    if(userInput == "All" or userInput == "all" or userInput == "ALL"):

        print("")
        print(f"Truck 1 at {time}:")
        for item in truck1.packages:
            printPackage = packageHash.search(item)
            printPackage.updateStatus(time)
            if printPackage.status == "Delivered":
                print(f'Package {printPackage.id} Delivered at {printPackage.timeDelivered}')
            else:
                print(f'Package {printPackage.id}: {printPackage.status}')

        print("")
        print(f"Truck 2 at {time}:")
        for item in truck2.packages:
            printPackage = packageHash.search(item)
            printPackage.updateStatus(time)
            if printPackage.status == "Delivered":
                print(f'Package {printPackage.id} Delivered at {printPackage.timeDelivered}')
            else:
                print(f'Package {printPackage.id}: {printPackage.status}')

        print("")
        print(f"Truck 3 at {time}:")
        for item in truck3.packages:
            printPackage = packageHash.search(item)
            printPackage.updateStatus(time)
            if printPackage.status == "Delivered":
                print(f'Package {printPackage.id} Delivered at {printPackage.timeDelivered}')
            else:
                print(f'Package {printPackage.id}: {printPackage.status}')

    else:
        try:
            userInputInt = int(userInput)
            userPackage = packageHash.search(userInputInt)

            print(packageHash.search(4).timeDelivered)
            userPackage.updateStatus(time)
            if userPackage.status == "Delivered":
                print(f'Package {userPackage.id} Delivered at {userPackage.timeDelivered}')
            else:
                print(f'Package {userPackage.id}: {userPackage.status}')

        except ValueError:
            print("No package found with that ID.")
            exit()


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















