m = int(input('Enter value of m'))
n = int(input('Enter value of n'))
arr = [[(i*j) for i in range(n)] for j in range(m)]
print(arr)