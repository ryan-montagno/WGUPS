
class Truck:

    def __init__(self, id, speedLimit, milesDriven, packages, maxPackages, startingAddr, startingTime):

        self.id = id
        self.speedLimit = speedLimit
        self. mileDriven = milesDriven
        self. packages = packages
        self.maxPackages = maxPackages
        self.startingAddr = startingAddr
        self.startingTime = startingTime

    def __str__(self):

        return f"Truck {self.id} has {len(self.packages)} packages on board."
