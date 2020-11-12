sen="she is beautiful and she is a good dancer"
# print(sen.replace("is", "was", 1))
pos1=sen.find("is")
pos2=sen.find("is", pos1+1)
print(sen.find("is", pos2))