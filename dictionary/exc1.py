n=int(input("Enter a num"))
def cube(x):
    dic={}
    for i in range(1,x+1):
        cu=i*i*i
        dic[i]=cu

    return dic    
print(cube(n))        