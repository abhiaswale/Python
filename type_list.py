l1=[1,2,'abhi',[1,2]]
def chck(list1):
    count=0
    for i in range(len(list1)):
        if type(list1)==type(list1[i]):
            count += 1
    return count    
print(chck(l1))
# print(type(l1[1])==type(l1[2]))
