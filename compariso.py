l1=[1,2,3,4,5,6]
l2=[1,2,5,6,7,8]
def cmp(i1,i2):
    output=[]
    i=0
    j=0
    for i in i1:
        for j in i2:
            if i == j:
                output.append(i)
    return output   
print(cmp(l1,l2))