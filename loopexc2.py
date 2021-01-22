lis=['abc','pqr','xyz']
def rev(words):
    l1=[]
    for i in words:
        l1.append(i[::-1])
    return l1
print(rev(lis))        