s = [[1,2,3],[2,334,24,6],[8,6]]
print(sorted(s,key= lambda s:len(''.join(map(str,s)))))
