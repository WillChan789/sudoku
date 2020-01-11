board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def printboard(b):
    for i in range(len(b)):
        if i != 0 and i % 3 == 0:
            print("= = = = = = = = = = = = =")

        for j in range(len(b[i])):
            if j != 0 and j % 3 == 0:
                print(" | ", end = "")

            if j < 8:
                print(str(b[i][j]) + " ", end = "")
            else:
                print(b[i][j])

def findempty(b):
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j] == 0:
                return (i, j)
    return None

printboard(board)
