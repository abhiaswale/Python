numb=input("Enter a multiple digit number:")
leng=len(numb)
total=0
for i in range(0,leng):
    total = total + int(numb[i])
print(f"Total is:{total}")    
