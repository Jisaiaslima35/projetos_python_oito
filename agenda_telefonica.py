import random

class AgendaTelefonica:
    def __init__(self):
        self.opcao = ''
        self.id = random.randint(1, 10000)

    def Exibir_menu(self):
        print('###################################')
        print('projeto agenda python')
        print('Menu:')
        print('[1] Cadastrar')
        print('[2] Excluir')

    def Iniciar(self):
        while self.opcao not in ['1', '2']:
            self.Exibir_menu()
            self.opcao = input('Escolha uma opção acima: ')

        if self.opcao == '1':
            self.Cadastrar()
        else:
            self.Excluir()

    def Cadastrar(self):
        idContato = self.id
        nome = input('digite seu nome :')
        telefone = input('digite seu telefone :')
        email = input('digite seu email')
        # para criar e gravar no arquivo txt
        try:
            agenda = open("agenda.txt","a")
            dados = f'{idContato};{nome};{telefone},{email} \n'
            agenda.write(dados)
            agenda.close()
            print(f'contatos salvo com sucesso')
        except:
            print('houve um ERRO')
        

    def Excluir(self):
        print(f'Você selecionou a opção de excluir o contato com ID {self.id}.')

agenda = AgendaTelefonica()
agenda.Iniciar()

