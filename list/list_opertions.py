f1=["x","b","a","y"]
f2=[1,2,3]
f1.insert(1,"m")
f1.append("x")
f1.extend(f2)
f1.append(f2)
f1.pop(1)
f1.remove("a")
del f1[1]
print(f1.count("a"))
# f1.sort()
# print(sorted(f1))
c1=f1.copy()
f2.clear()
print(f2)