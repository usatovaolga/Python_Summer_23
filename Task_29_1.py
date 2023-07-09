s=[1,1,1,1,-1,1,1]
print(min(set(s), key=lambda x: s.count(x)))