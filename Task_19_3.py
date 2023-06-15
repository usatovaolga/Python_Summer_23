class Person:
    def __init__(self,f,n,l):
        self.f=f
        self.n=n
        self.l=l
    def rev(self):
        print(self.l[::-1]+self.n[::-1]+self.f[::-1])
p = Person('Иванов','Михаил', 'Федорович')
p.rev()