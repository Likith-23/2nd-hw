def myfunction(n):
    if(n>0):
        return
    for i in range(0, n+1):
        print("codingal")
    myfunction(n/2)
    myfunction(n/3)
def myfunction1(n):
    if(n<=1):
        return
    print("Codingal")
    myfunction1(n-1)
print(myfunction(5))
print(myfunction1(4))