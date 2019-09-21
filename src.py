import pandas

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

xls = pandas.ExcelFile('data.xlsx')

equipment = pandas.read_excel(xls, 'Equipment Details')
worker = pandas.read_excel(xls, 'Worker Details')
facility = pandas.read_excel(xls, 'Facility Details')
examples = pandas.read_excel(xls, 'Work Order Examples')
sheets = [equipment, worker, facility, examples]

equipment_list = list()
workers = list()
facilities = list()

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
    item.toStr()
