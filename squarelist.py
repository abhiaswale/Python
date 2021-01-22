# numbers=[1,2,3,4]
no=int(input('Enter a number:'))
numbers= list(range(1,no))
def neg(l):
    square_nos = []
    for i in l:       
        square_nos.append(i*i)
    return square_nos  

print(neg(numbers))

