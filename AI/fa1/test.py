f = lambda x, j: [j] + f(x/j,j) if x%j==0 else f(x,j+1) if j<x else []
print(*f(int(input()), 2), sep='x')
