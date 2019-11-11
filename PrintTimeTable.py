from texttable import Texttable

def concat_list(list):
    result = ''
    for element in list:
        result += str(element) + ' /'
    return result[0:-1]

def PrintTT(model,numberOfDays,numberOfTimeSlots, slotDict):
    numberOfSlots = numberOfDays * numberOfTimeSlots
    row = [None] * (numberOfSlots)

    for i in range(numberOfSlots):
        row[i] = set([])

    for paper in slotDict:
        for slot in range(numberOfSlots):
            if model.evaluate(slotDict[paper][slot]):
                row[slot].add(paper.split('/')[0])

    row = [list(x) for x in row]

    for i in range(numberOfSlots):
        row[i] = concat_list(row[i])

    table = Texttable()
    slotString = ["D"+str(i+1)+"S"+str(j+1) for i in range(numberOfDays) for j in range(numberOfTimeSlots)]
    tableRows = [["Slots", "Courses"]]

    for i in range(numberOfSlots):
        tableRows.append([slotString[i],row[i]])

    table.add_rows(tableRows)
    print(table.draw())
