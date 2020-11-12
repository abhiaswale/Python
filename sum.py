num=input('enter a number with multiple digits:')
leng1=len(num)
# print(leng1)
total=0
i=0   
while i<leng1:
    total=total+int(num[i])
    i=i+1

print(f"sum of the numbers is :{total}")