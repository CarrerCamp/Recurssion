def firstIndex(arr, x,si):
    n=len(arr)
    if si==n:
        return -1
    if arr[si]==x:
        return si
    return firstIndex(arr,x,si+1)

from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x,0))
