def factorial(N):
    f = 1
    for n in range(0, N):
        f *= n 
    return f

N = 5
print("{}! = {}".format(N, factorial(N)))
