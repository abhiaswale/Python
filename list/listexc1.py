l1=['true','false',1,2,2.2]
def fun(x):
    sort=[]
    for i in x:
        if type(i)==int or type(i)==float:
            sort.append(i)
    return sort        
print(fun(l1))

