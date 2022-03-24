matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(matrix[0][1]) #2


#Iterating over matrix lists with nested loops
for row in matrix:
  for cell in row:
    print(cell)