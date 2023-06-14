def dec(func):
    def wrapper(*args,**kwargs):
        new_r=[]
        func(*args,**kwargs)
        for arg in args:
            if type(arg)==str:
                new_r.append(arg.upper())
        for k,v in kwargs.items():
            if type(v) == str:
                new_r.append(v.upper())
        return new_r
    return wrapper
@dec
def strr(*args,**kwargs):
    print(args,kwargs)
print(strr('qwer','gfs','rff',222,'rty',q='lll',w=123,e='1'))