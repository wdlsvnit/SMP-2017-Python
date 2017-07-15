#! python3
#To print a list of list into organized way

tableData=[['apples', 'oranges', 'cherries', 'banana'],
           ['Alice', 'Bob', 'Carol', 'David'],
           ['dogs', 'cats', 'moose', 'goose']]


def printTable(data):
    maxlen=[0,0,0]
    for i in range(len(data)):
        for j in range(len(data[i])):
            if len(data[i][j]) > maxlen[i] :
                   maxlen[i]=len(data[i][j])

    for i in range(len(data[0])):
        for j in range(len(data)):
            print(data[j][i].rjust(maxlen[j]),end=" ")
        print("")

    
            
printTable(tableData)   
