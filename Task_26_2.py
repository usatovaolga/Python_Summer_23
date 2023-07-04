def dis(self):
    for k,v in self.__dict__.items():
        print( k+': '+v)

Pett = type('Pet',(),{'dis':dis})
m_Pet = Pett()
m_Pet.name = 'Tom'
m_Pet.dis()

