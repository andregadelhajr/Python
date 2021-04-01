import random

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você se sabe',
            'Não faz isso Não!',
            'Acho que tá na hora certa!'
        ]

    def Iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))        
    
decida = DecidaPorMim()
decida.Iniciar()

