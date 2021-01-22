# user_info={'name':'Abhi','age':24}
# print(user_info)
user_info2={
    'name':'Abhi',
    'age':24,
    'Fav_movies':['inception','intersteller'],
    'Fav_songs':['understanding','hanging tree']
}
# insert data in a dictionary
user_info2['favv_place']='norway'
# checks key
# if 'name' in user_info2:
#     print('present')
# else:
#     print('not present')    
# to check data

# if 'Abhis' in user_info2.values():
#     print('data present')
# else:
#     print('data not present') 

# popped_item=user_info2.pop('favv_place')
poped_itm=user_info2.popitem()
print(poped_itm)
# print(user_info2)