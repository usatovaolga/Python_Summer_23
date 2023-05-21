dg=['у','е','ы','а','о','э','я','и','ю','ё']
s=input("Введите слово - ")
k3 = {}
n = int(input("Введите кол-во слов:"))
for i in range(0,n):
  k3[input("Введите слово и нажмите Enter - ")] = []
x=[]
k2=[]
rez=[]
for i,v in enumerate(list(s)):
    if v in dg:
        x.append(i)
for k,v in k3.items():
    for i,v in enumerate(list(k)):
        if v in dg:
            k2.append(i)
    k3[k]=k2
    k2=[]
for m,l in k3.items():
    if l==x:
        rez.append(m)
print(', '.join(rez))
