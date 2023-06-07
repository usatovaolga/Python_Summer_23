def sample_dec(func):
    def wrapper():
        res = func()
        new_res=res.title()
        return new_res
    return wrapper  # возвращаем новую функцию
@sample_dec
def say():
    return input("Введите строку ->")#'Hello how are you'
print(say())