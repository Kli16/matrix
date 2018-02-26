from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 255 ]
matrix = new_matrix()

print "---PRINT MATRIX---"
print_matrix(matrix)
print "---IDENTITY MATRIX---"
ident(matrix)
print_matrix(matrix)

print "---MATRIX MULTIPLICATION---"
A = [[6,3],
    [4, -3]]
B = [[6,5,7],
    [-1,-4,-3]]
matrix_mult(A,B)
'''
[33 18 33]
[27 32 37]
'''

matrix = new_matrix()

color = [ 205, 86, 57 ]

for x in range(60, 500):
    add_point(matrix, x, 100, 0)
    add_edge(matrix, x, 400, 0, 200, x, 0)

draw_lines( matrix, screen, color )
display(screen)
save_extension(screen, 'img.png')
