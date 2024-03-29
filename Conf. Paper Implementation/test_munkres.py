from munkres import Munkres, print_matrix, make_cost_matrix
import sys
matrix = [[5, 9, 1],
          [10, 3, 2],
          [8, 7, 4]]
cost_matrix = make_cost_matrix(matrix, lambda cost: sys.maxint - cost)
m = Munkres()
indexes = m.compute(cost_matrix)
print_matrix(matrix, msg='Lowest cost through this matrix:')
total = 0
for row, column in indexes:
    value = matrix[row][column]
    total += value
    print '(%d, %d) -> %d' % (row, column, value)
print 'total profit=%d' % total