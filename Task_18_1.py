class Teacher:
    def __init__(self,name):
        self.name = name
        self.task = '' #список задач
    def make_task(self):
        task = input('Ведите задачу:')
        self.task = task
        for pup in Pupil.ppls:
            pup.task = task
            pup.status = False
            pup.teacher = self
    def check_task(self):
        print('\nПроверка')
        for pup in Pupil.ppls:
            print(f"{pup.name} {pup.status} {pup.solution}")
            if pup.status=='?' or pup.status ==False or pup.status=='':
                dec=input("Правильно?")
                if dec=='Да':
                    pup.status==True
                else:
                    pup.status = False
    def get_res(self):
        print("\nРезультаты:")
        for pup in Pupil.ppls:
            print(pup.name,pup.status)
class Pupil:
    ppls=[]
    def __init__(self,name):
        self.name = name
        self.task= ''#список кортежей (task,solution,status)
        self.solution =''
        self.status=''
        self.teacher=''
        Pupil.ppls.append((self))
    def make_solution(self):
        print(f"\Ввод решения {self.name} {self.task}")
        if self.status =='' or self.status==False:
            solution = input("Введите решение")
            self.solution = solution
            self.status ='?'

t=Teacher('ttt')
a=Pupil('aaa')
b=Pupil('bbb')
c=Pupil('ccc')
t.make_task()
a.make_solution()
b.make_solution()
c.make_solution()
t.check_task()
t.get_res()