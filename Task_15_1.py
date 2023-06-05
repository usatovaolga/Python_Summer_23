dct= {1:1, 2:2, 3:{2:22, 3:{1:111, 2:222, 3:{0:1111, 1:2222, 2:3333}}, 1:11,}, 6:22}
r=[]
n = int(input("Введите значение ключа ->"))
def rec_s(dct,x):
    for k,v in dct.items():
        if type(v)==dict:
            rec_s(v,x)
        else:
            if k==x:r.append(v)
rec_s(dct,n)
print(r)