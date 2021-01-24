l=['abc','tuv','xyz']
def fen(list1):
    rev=[i[::-1] for i in list1]
    # for i in list1:
    #     rev.append(i[::-1])
    return rev
print(fen(l))

even_nos=[i for i in range(1,20) if i%2==0]
print(even_nos)
