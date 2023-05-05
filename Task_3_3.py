s = input("Введите предложение ->   ") #hi how are you
lst=[]
lst=s.split()
mlen=0
mlst=[]
for i in lst:
    if len(i)>mlen: mlen=len(i)
for i in lst:
    if len(i)==mlen: mlst.append(i)
print(f"Самое длинное первое слово - {mlst[0]}")
print("Все самые длинные слова - ", ', '.join(mlst))
