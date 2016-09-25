def spiral_matrix(a):
    m = len(a)
    n = len(a[0])
    spiral = 0
    row_start = 0
    row_end = m-1
    col_start = 0
    col_end = n-1
    while row_start < row_end:
          row_start = row_start + spiral
          row_end = row_end - spiral
          col_start = col_start + spiral
          col_end = col_end - spiral
          for x in range(col_start, col_end):
               print a[row_start][x]
          for x in range(row_start+1, row_end):
               print a[x][col_end]
          for x in reversed(range(col_start, col_end)):
               print a[row_end][x]
          for x in reversed(range(row_start, row_end)):
               print a[x][col_start]
          spiral += 1
           

if __name__=='__main__':
    a = [[1,2,3], [6,5,4], [7,8,9]]
    spiral_matrix(a)
