import string
import random
import csv

from PackageModule import Package
from HashModule import PackageHash

packageList = []
packageHash = PackageHash(40)

packageList.append(Package(5, "456 street road", "Ridley", "PA", "12345", "10:30", 100, "Deliver by 10:30", "On time"))
packageList.append(Package(41, "987 street road", "Ridley", "PA", "12346", "9:30", 10, "Deliver by 9:30", "On time"))
packageList.append(Package(12, "789 street road", "Ridley", "PA", "12346", "9:30", 10, "Deliver by 9:30", "On time"))
packageList.append(Package(45, "654 street road", "Ridley", "PA", "12346", "9:30", 10, "Deliver by 9:30", "On time"))
packageList.append(Package(1, "123 street road", "Ridley", "PA", "12346", "9:30", 10, "Deliver by 9:30", "On time"))


for i in range(len(packageList)):
    packageHash.insert(packageList[i].id, packageList[i])

with open(.)













