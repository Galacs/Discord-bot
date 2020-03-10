mat = [
[1,0,0,1,0],
[1,0,1,0,0],
[0,0,1,0,1],
[1,0,1,0,1],
[1,0,1,1,0],
]

checked = []
c = 0

def riverSizes(matrix):
    a, b = 0, 0
    d = []
    checked, rivers = [], []
    for i in matrix:
        checked.append([])
        for g in i:
            if checked[a][b] != True:
                if matrix[a][b] == 1:
                    checkSides(a, b)
            else:
                checked[c].append(True)
            b += 1
        a += 1

def checkSides(a,b):
    try:
        checked[c].append(True)
        if matrix[a-1][b] ==1:
            checkSides(a-1, b)

        if matrix[a][b+1] ==1:
            checkSides(a, b+1)

        if matrix[a+1][b] == 1:
            checkSides(a+1, b)

        if matrix[a][b-1] == 1:
            checkSides(a, b-1)
    except:
        pass
    return 0

riverSizes(mat)