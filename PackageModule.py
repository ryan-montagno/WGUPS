from contextlib import nullcontext


class Package:

    id = 0
    address = ""
    city = ""
    state = ""
    zipcode = ""
    deadline = ""
    weight = ""
    notes = ""
    status = ""


    def __init__(self, id, address, city, state, zipcode, deadline, weight, notes, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = "At hub."
        self.timeDelivered = None
        self.timeDeparted = None


    def __str__(self):
        return f'Address: {self.address} City: {self.city} State: {self.state} Zipcode: {self.zipcode} Deadline: {self.deadline} Weight: {self.weight} Notes: {self.notes} Status: {self.status}'

    def getID(self):
        return int(self.id)

    def updateStatus(self, userTime):

        if self.timeDelivered < userTime:
            self.status = "Delivered"
        elif self.timeDeparted < userTime:
            self.status = "En route"
        else:
            self.status = "At Hub"

