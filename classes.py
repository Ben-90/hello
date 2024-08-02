class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
    def passengr_list(self):
        return self.passengers

flight = Flight(3)

people = ['Jean', 'harris', 'paul', 'ben', 'arnaul']

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f'{person} added to the flight')
    else:
        print(f'{person} could not be added to the flight')

print(flight.passengr_list())

#####################################
#########################
###################
##############
########


def announce(f):
    def wrapper():
        print('Something is happening before the function is called.')
        f()
        print('The function is finishing the running.')
    return wrapper

@announce
def say_hello():
    print('Hello package for a review of python!')

say_hello()
#####################################

people1 = ["Harry", "Cho", "Ben", "Draco"]
people1.sort()

print(people1)

###################
people2 = [
    {"name": "Harry", "age": 20},
    {"name": "Cho", "age": 20},
    {"name": "Ben", "age": 20},
    {"name": "Draco", "age": 20}
]

def f(person):
    return person["name"]

#people2.sort(key=f)
people2.sort(key=lambda person: person["name"])

print(people2)

