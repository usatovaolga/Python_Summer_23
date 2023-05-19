
lst=[]
def rt(s):
    for i in s:#
        #if i=='А' or i=='Г':
        #    if s[s.index(i)+1]=='А' or s[s.index(i)+1]=='Г':
        #        lst.append(s[s.index(i)+1])
        #        lst.append(s[s.index(i)])
        if i == 'А' and s[s.index(i)+1]=='Г':
         #if s[s.index(i)+1]=='А' or s[s.index(i)+1]=='Г':
                lst.append(s[s.index(i)+1])
                lst.append(s[s.index(i)])
        else:
            lst.append(i)
    return ''.join(lst)
print(rt(input("Введите строку генетического кода")))