# flight.py  a new flight of given capacity
# limit the number of passengers
class Flight():
    def __init__(self,capacity): 
        self.capacity = capacity
        self.passengers =[]
    # Method to add a passenger to the list
    def add_passenger(self,name):
        if not self.open_seats():   
          return False
        self.passengers.append(name) 
        return True
   
    # Method to return number of open seats
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
    # create a list of people who may be passengers upto max 3
flight = Flight(3)
# add a list of people
people = ["Gwydion","Heledd","Llyr","Griff"]
# Atfor person in people:
for person in people:
    if flight.add_passenger(person):
     print (f"Added {person} successfully to flight")
else:
     print (f"Person {person} was not added, flight is full")  

