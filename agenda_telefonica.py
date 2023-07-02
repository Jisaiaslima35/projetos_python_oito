class AgendaTelefonica:
    def __init__(self):
        self.opcao = ''

    def Exibir_menu(self):
        print('###################################')
        print('projeto agenda python')
        print('Menu :')
        print('''
        [1] Cadastrar
        [2] Excluir
        ''')
    def Iniciar(self):
        while self.opcao not in ['1','2']:
            self.Exibir_menu()
            self.opcao = input('Escolha uma opçao Acima :')
        
        if self.opcao == '1':
            self.Cadastrar()
        else:
            self.Excluir()
    def Cadastrar(self):
          print('vc escolheu a opçao de cadastro')

    def Excluir(self):
        print('vc vai exckuir')

