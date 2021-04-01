import random

class DecidaPorMim:
    def __init__(R):
        R.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você se sabe',
            'Não faz isso Não!',
            'Acho que tá na hora certa!'
        ]

    def Iniciar(R):
        input('Faça sua pergunta: ')
        print(random.choice(R.respostas))
 
    
decida = DecidaPorMim()
decida.Iniciar()

