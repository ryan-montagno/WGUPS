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


    def __str__(self):
        return f'ID: {self.id}\nAddress: {self.address}\nCity: {self.city}\nState: {self.state}\nZipcode: {self.zipcode}\nDeadline: {self.deadline}\nWeight: {self.weight}\nNotes: {self.notes}\nStatus: {self.status}'

    def getID(self):
        return int(self.id)


