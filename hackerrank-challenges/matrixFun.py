import sys
QueryBoard = [[0 for x in range(256)] for y in range(256)]
#print(QueryBoard)
def comLine(command, rowcol, x):
    if command == "SetCol":
        for i in QueryBoard:
            i[rowcol] = x
        return
    elif command == "SetRow":
        for j in QueryBoard[rowcol]:
            j = x
        return
    elif command == "QueryRow":
        rowSum = sum(QueryBoard[rowcol])
        print(rowSum)
        return
    elif command == "QueryCol":
        colSum = 0
        for i in QueryBoard:
            colSum += i[rowcol]
        print(colSum)
        return
inputLine = ['SetCol 32 20','SetRow 15 7', 'SetRow 16 31', 
'QueryRow 10', 'SetCol 2 14', 'QueryCol 32']

for line in inputLine:
    #print(line, end="")
    comList = line.split(' ')
    print(comList)
    if len(comList) == 2:
        comList.append(0)
    comLine(comList[0], int(comList[1]), int(comList[2]))
print(QueryBoard[15]) 
print(QueryBoard[16])

for i in range(len(QueryBoard[15])):
	QueryBoard[15][i] = 10;
print(QueryBoard[15])  

