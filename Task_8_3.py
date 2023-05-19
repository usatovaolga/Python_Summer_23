s=['abab','xx','aaaaa','qwerty']
b=['abab','opop']
print(sorted(s,key= lambda s:len(set(s)),reverse=True))
print(sorted(b,key= lambda b:len(set(b)),reverse=True))