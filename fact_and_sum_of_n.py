def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
    

def fact1(n):
    if n==0:
        return 1
    smallOutput=fact(n-1)
    return n*smalloutput

def sum_n(n):
    if n==0:
        return 0
    smallOutput=sum_n(n-1)
    output=smallOutput+n
    return output

n=int(input())
print(fact(n))
print(sum_n(n))
