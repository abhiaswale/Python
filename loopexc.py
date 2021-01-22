numbers=[1,2,3,4,5,6]
def rev(l1):
    temp=0
    rev_list=[]
    for i in range(len(l1)):
        temp=l1.pop()
        rev_list.append(temp)
    return rev_list   
print(rev(numbers))        

