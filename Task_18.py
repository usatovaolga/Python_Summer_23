
class Teacher:
    def __init__(self):
        self.work = 0
    #####
    def task(self):
        s=
    def  teach_sets(self, lesson, tasks, *pupil):
        for i in pupil:
            i.record(lesson,tasks)
    def check(self,lesson,status,*pupil):
        t={}
        tt={}
        for i in pupil:
            print(f"Проверка дз у ученика {i.name}")
            t=i.send(lesson)
            for k,v in t.items():
                t[k]=status
            i.write(lesson)
        tt[i.name]=t
        #return tt

class Pupil:
    #pupil_list = []
    def __init__(self,name):
        self.name =name
        #Pupil.pupil_list.append(self)
        self.notebook = {}
    def record(self,lesson, tasks):
        self.notebook[lesson]=tasks
    def solve(self,lesson,status):
        ans_tasks={}
        for k,v in self.notebook.items():
            if k==lesson:
                for x in range(1,v+1):
                    ans_tasks[x]=status
                self.notebook[k]=ans_tasks
        self.write(lesson)
        return self.notebook
    def send(self,lesson):
        return self.notebook[lesson]
    def write(self,lesson):
        for k,v in self.notebook.items():
            if k==lesson:
                print(f"{k} урок: ")
                if type(v)==dict:
                    for x,y in v.items():
                        print(f"Задача №{x} {y}")
                else: print(f"{v} задачи")


ZimnevM = Teacher()
olga = Pupil('Ольга')
q =int(input("Вы учитель(1) или ученик(2), напишите цифру: "))
if q==1:
    qq = int(input("Выберите действие 1-задать задание, 2-проверить задание, напишите цифру: "))
    match qq:
        case 1:
            ZimnevM.teach_sets(int(input()), int(input()), input())


        case 2:


ZimnevM.teach_sets(1, 3, olga) #учитель задает домашку, на 1 уроке 3 задания для таких-то учеников, ученик записывает в свою тетрадь

#print(olga.notebook) #смотрим что ученик записал в тетрадь
olga.solve(1, 'Решено') #ученик решает дз по заданному уроку
#olga.solve(2, 'Не решено')
ZimnevM.check(1,'Не решено',olga) #учитель проверяет дз по заданному уроку у конкретного ученика, в момент проверки учитель получает отправленное учеником дз
#print(ZimnevM.check(2,'Решено',olga))