import math


def print_matrix( matrix ):
    ctr = 0
    while (ctr < len(matrix)):
        print matrix[ctr]
        ctr += 1;

def ident( matrix ):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if row == col:
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    temp = new_matrix(len(m2[0]), len(m2))
    #print_matrix(temp)
    for r in range(len(m1)):
        for col in range(len(temp[0])):
            for r2 in range(len(temp)):
                temp[r][col] += m1[r][r2] * m2[r2][col]
    #print_matrix(temp)
    for i in range(len(m2)):
        for j in range(len(m2[0])):
            m2[i][j] = temp[i][j]
    print_matrix(m2)

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
