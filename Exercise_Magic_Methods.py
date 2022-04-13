import csv

class Astronaut:
    def __init__(self,name,flight,status):
        self.name = name
        self.Flight = flight
        self.status = status

    def __gt__(self,other):
        return self.flight > other.flight
    
    def __eq__(self,other):
        return self.flight == other.flight
    
    def __ge__(self,other):
        return self.flight >= other.flight

    def __str__(self):
        return f'{self.name}, {self.status}'


#Part 3
f=open("astronauts.csv",'r')      
astronautDictionary = csv.DictReader(f)
dictList = list(astronautDictionary)
f.close() 

peopleList =[]
for i in range(0,len(dictList)):
    peopleList.append(Astronaut(dictList[i]["Name"], dictList[i]["Space Flight (hr)"], dictList[i]["Status"]))

print(vars(peopleList[0]))


import random

a1 = random.choice(peopleList)
a2 = random.choice(peopleList)
print(a1)
print(a1>a2)
print(a1=a2)
print(a1>=a2)



for i in range(0,len(peopleList)):
    print(peopleList[i])