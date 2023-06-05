dct= {1:'1', 2:2, 3:{4:22, 3:{3:111, 2:222, 1:{0:1111, 1:2222, 2:3333}}, 1:11}, 6:22}
r=[]
n = int(input("Введите значение ключа ->"))
def rec_s(dct,x):
    for k,v in dct.items():
        if type(v)==dict and k!=1:
            rec_s(v,x)
        elif type(v)==dict and k==1:
            r.append(v)
            rec_s(v, x)
        else:
            if k==x:r.append(v)
rec_s(dct,n)
print(r)