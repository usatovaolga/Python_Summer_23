s1,s2=input('str 1->'),input('str 2->')
print(sum(1 for i in range(len(s1)) if s1[i] != s2[i]))
