user={
    'name':'Abhi',
    'age':24,
    'Fav_movies':['inception','intersteller'],
    'Fav_songs':['understanding','hanging tree']
}

# add data
user['fav_album']=['blueprint','divinity']
print(user)
 #delete data
#1)Pop method
# popped_item1=user.pop('fav_album')
# print(popped_item1)

#2)Popped item method
popped=user.popitem()
print(popped)
print(user)