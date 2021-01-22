d1={}
name=input("Enter Your name :")
age=int(input("Enter your age :"))
fav_movies=input("Enter your fav movies :").split(",")
fav_place=input("Enter your fav places :").split(",")
d1['name']=name
d1['age']=age
d1['Fav_movies']=fav_movies
d1['Fav_place']=fav_place
for i,j in d1.items():
    print(f"{i} is {j}")
