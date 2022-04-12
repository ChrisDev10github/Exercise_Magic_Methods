import csv

class Astronaut:
    def __init__(self,name,flight,status):
        self.name = name
        self.Flight = flight
        self.status = status

    def __gt__(self,other):
        if self.flight > other.flight:
            return self.flight > other.flight
    
    def __eq__(self,other):
        if self.flight == other.flight:
            return self.flight == other.flight
    
    def __ge__(self,other):
        if self.flight >= other.flight:
            return self.flight >= other.flight

    def __str__(self):
        return f'{self.name}, {self.status}'


#Part 3
f=open("astronauts.csv",'r')      
astronautDictionary = csv.DictRead(f)
dictList = list(astronautDictionary)
f.close() 

vars(dictList[0])
