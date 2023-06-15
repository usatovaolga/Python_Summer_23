class F:
    def __init__(self,n):
        self.f=0
        self.s=1
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.f>self.n:
            raise StopIteration
        t = self.f + self.s
        self.f = t
        self.f, self.s = self.s, self.f
        return t
f = F(5)
for i in f:
    print(i)
