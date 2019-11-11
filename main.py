from z3 import *
import sys
sys.path.append('./Utils')

#reading data from input.json file
from Input import getData
from PrintTimeTable import PrintTT
data = getData()

courseDict = {}
roomDict = {}
dayDict = {}
slotDict = {}
sizeDict = {}

numberOfDays = int(data['numberOfDays'])
numberOfTimeSlots = int(data['numberOfTimeSlots'])
numberOfSlots = numberOfDays*numberOfTimeSlots

if len(data['roomsAvailableOnDay']) != numberOfDays:
    print("Invalid input check roomsAvailableOnDay and numberOfDays")
    sys.exit(0)

for course in data['courses']:
    courseDict[str(course[0])] = {"batches": [str(batch) for batch in course[1]], "size": [int(batchSize) for batchSize in course[2]]}
    if len(courseDict[str(course[0])]["batches"]) != len(courseDict[str(course[0])]["size"]):
        print("Invalid input check number of batches and batch sizes for course: "+str(course[0]))
        sys.exit(0)

for course in courseDict:
    for batch,size in zip(courseDict[course]["batches"],courseDict[course]["size"]):
        sizeDict[str(course)+'/'+str(batch)] = size

for room in data['roomsCapacity']:
    roomDict[str(room)] = {"size": int(data['roomsCapacity'][room])}

day = 0
for rooms in data['roomsAvailableOnDay']:
    dayDict[day] = {"size": sum([int(roomDict[room]["size"]) for room in rooms])}
    day += 1
print(dayDict)

for course in courseDict:
    for batch in courseDict[course]["batches"]:
        slotDict[course+'/'+batch] = [Bool(course+'/'+batch+'/'+str(j)+'/'+str(i)) for i in range(numberOfDays) for j in range(numberOfTimeSlots)]

solver = Solver()

#At most one exam for each course and each batch taking that course in the whole time table
for paper in slotDict:
    for i in range(numberOfSlots):
        for j in range(numberOfSlots):
            if i != j:
                solver.add(Implies(slotDict[paper][i], Not(slotDict[paper][j])))

#there should be atleast one exam for each course and each batch taking that course for all days
for paper in slotDict:
    solver.add(Or([slots for slots in slotDict[paper]]))

#For all batches taking a particular course the exam should be on the same day
for paper in slotDict:
    for i in range(numberOfSlots):
        for remaining in slotDict:
            if remaining.split('/')[0] == paper.split('/')[0] and paper != remaining:
                solver.add(Implies(slotDict[paper][i],slotDict[remaining][i]))

#There can only be one exam of a batch in one day
for paper in slotDict:
    for i in range(numberOfSlots):
        for remaining in slotDict:
            if remaining.split('/')[1] == paper.split('/')[1] and paper != remaining:
                y = int(i/numberOfTimeSlots)
                y = y*numberOfTimeSlots
                for j in range(y,y+numberOfTimeSlots):
                    solver.add(Implies(slotDict[paper][i],Not(slotDict[remaining][j])))

# The total number of students taking exam in a particular time slot must be less than the total capacity of rooms availablr that day.
for i in range(numberOfDays):
    x = i*numberOfTimeSlots
    for j in range(x,x+numberOfTimeSlots):
        solver.add(Sum([If(slotDict[paper][j],sizeDict[str(paper)],0) for paper in slotDict]) <= dayDict[i]["size"])

if solver.check() == sat:
    PrintTT(solver.model(), numberOfDays, numberOfTimeSlots, slotDict)
else:
    print("No possible Time Table for given Input!!")
