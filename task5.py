n=int(input("enter the number"))
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
ans=fact(n)
print(ans)