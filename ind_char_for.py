nm=input("Enter a name:")
temp=""
for i in range(0,len(nm)):
    if nm[i] not in temp:

        temp += nm[i]
        print(f"{nm[i]}={nm.count(nm[i])}")