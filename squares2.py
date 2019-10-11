squares=[]
for x in range(10):
    squares.append(x**2)
print(squares)

squares=[x**2 for x in range(10)]
print(squares)

matrix=[(z,y) for z in [1,2,3] for y in [3,2,1] if z!=y]
print(matrix)
