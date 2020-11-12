name,age = input("Enter Your Name & Age :").split(",")
age=int(age)
if name[0]=='a' or 'A' and age>10:
    print("You can watch the movie")
else:
    print("You cannot watch movie")    