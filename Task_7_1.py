x = 0
nn=[]
while True:
    x=int(input("Введите натурально число (окончание ввода 0) ->"))
    if x == 0: break
    nn.append(x)
def nok(lst):
    nk=1
    def nod(a, b):
        while a != b:
            if a < b:
                b = b - a
            else:
                a = a - b
        return a
    for i in lst:
        nk=nk*i/nod(nk,i)
        #print(i)
        #print(nk)
    return int(nk)
print(nok(nn))