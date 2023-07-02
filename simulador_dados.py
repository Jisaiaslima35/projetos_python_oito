import random
print('ola mundo, alterei novo modelo')


class SimuladoDados:

    def __init__(self):
        self.numero_menor = 1
        self.numero_maior = 6
        self.teste = ''
        self.mensagem = 'Rodar Mais uma Vez ? '

    def Iniciar(self):
        resposta = input(self.mensagem)
        numero = random.randint(self.numero_menor,self.numero_maior)

        if resposta == 's' or resposta == 'sim':
            print('O NUMERO FOI ', numero)

        else:
            print('ate mais thauuu')
            
simulador = SimuladoDados()
simulador.Iniciar()
