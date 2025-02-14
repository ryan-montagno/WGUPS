
class Package:

    def __init__(self, id, address, deadline, city, zipcode, weight, status):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zipcode = zipcode
        self.weight = weight
        self.status = status

    def __str__(self):
        return f'ID: {self.id}\nAddress: {self.address}\nDeadline: {self.deadline}\nCity: {self.city}\nZipcode: {self.zipcode}\nWeight: {self.weight}\nStatus: {self.status}'


