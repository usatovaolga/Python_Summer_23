s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
class CP:
    def __init__(self):
        self.n=0
        self.ss=[]
        for i in s:
            self.ss.append(i)
    def __iter__(self):
        return self
    def __next__(self):
        # if self.n>10:
        #     raise StopIteration
        try:
            self.ss[self.n]
        except IndexError:
            self.n=0
        w = self.ss[self.n]
        self.n+=1
        return self.n,w
f = CP()
for i in f:
    print(*list(i),sep=', ',end=', ')