numbers=[1,2,3,4,5,6,7,8,9,10]
def even_odd(l1):
    even=[]
    odd=[]
    for i in l1:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i) 
    output=[odd,even] 
    return output    
print(even_odd(numbers))    