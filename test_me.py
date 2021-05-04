def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

def list_of_squares(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    return d
