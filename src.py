import math, pandas, pprint

class Equipment:
    def __init__(self, id, type, probFail, fixTime, inventory):
        self.id = id
        self.type = type
        self.probFail = probFail
        self.fixTime = [int(fixTime[0]), int(fixTime[1])]
        self.inventory = inventory

    def toStr(self):
        print('ID: ' + str(self.id))
        print('Type: ' + str(self.type))
        print('probFail: ' + str(self.probFail))
        print('fixTime: ' + str(self.fixTime))
        print('inventory: ' + str(self.inventory))
        print()

class Worker:
    def __init__(self, name, equipmentTypes, shifts):
        self.name = name
        self.equipmentTypes = equipmentTypes
        self.shifts = shifts

    def toStr(self):
        print('Name: ' + str(self.name))
        print('equipmentTypes: ' + str(self.equipmentTypes))
        print('shifts: ' + str(self.shifts))
        print()

class Facility:
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords
        #self.inventory = inventory

    def toStr(self):
        print('Name: ' + str(self.name))
        print('coords: ' + str(self.coords))
        #print('inventory: ' + str(self.inventory))
        print()

class Order:
    def __init__(self, id, facility, equipment, priority, fixTime, submissionTime):
        self.id = id
        self.facility = facility
        self.equipment = equipment
        self.priority = priority
        self.fixTime = fixTime
        self.submissionTime = submissionTime

    def toStr(self):
        print('ID: ' + str(self.id))
        print('facility: ' + str(self.facility))
        print('equipment: ' + str(self.equipment))
        print('priority: ' + str(self.priority))
        print('fixTime: ' + str(self.fixTime))
        print('submissionTime: ' + str(self.submissionTime))
        print()

equipment_list = list()
workers = list()
facilities = list()
examples = list()

def input_data(filename):
    xls = pandas.ExcelFile(filename)

    equipment = pandas.read_excel(xls, 'Equipment Details')
    worker = pandas.read_excel(xls, 'Worker Details')
    facility = pandas.read_excel(xls, 'Facility Details')
    test(pandas.read_excel(xls, 'Work Order Examples'))

    global equipment_list
    global workers
    global facilities

    for index, row in equipment.iterrows():
        inventory = [row['Fac' + str(i)] for i in range(1, 6)]
        item = Equipment(index, row['Equipment'], row['Probability of Failure'], row['Hours to Fix (range)'].split('-'), inventory)
        equipment_list.append(item)

    for index, row in worker.iterrows():
        item = Worker(row['Name'], row['Equipment Certification(s)'].split(', '), row['Shifts'])
        workers.append(item)

    for index, row in facility.iterrows():
        item = Facility(row['Facility'], (row['Latitude'], row['Longitude']))
        facilities.append(item)

def calculateDistance(facA, facB):
    return math.fabs(math.sqrt(math.pow(facA.coords[0] - facB.coords[0], 2) + math.pow(facA.coords[1] - facB.coords[1], 2)))

def rankFacilities(facilities):
    distances = list()
    for i in range(len(facilities)):
        fromI = list()
        for j in range(len(facilities)):
            if not i == j:
                distance = calculateDistance(facilities[i], facilities[j])
                fromI.append((distance, facilities[j].name))
                #print('Distance from ' + facilities[i].name + ' to ' + facilities[j].name + ': ' + str(distance))
        fromI.sort()
        distances.append(fromI)
    return distances

def test(examples):
    index = 0
    for index, row in examples.iterrows():
        # make an equipment item
        item = Order(index, row['Facility'], row['Equipment Type'], row['Priority(1-5)'], row['Time to Complete'], row['Submission Timestamp'])
        equipment_list.append(item)
        index += 1

def main():
    filename = 'data.xlsx'
    input_data(filename)

    global facilities
    global workers
    global equipment_list
    distances = rankFacilities(facilities)

    for worker in workers:
        worker.toStr()

main()
