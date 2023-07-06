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
        print('[2] Listar Conatos')
        print('[3] Excluir')
        print('[4] Buscar Pelo Nome')
        

    def Iniciar(self):
        while self.opcao not in ['1', '2', '3' ,'4','5']:
            self.Exibir_menu()
            self.opcao = input('Escolha uma opção acima: ')

        if self.opcao == '1':
            self.Cadastrar()
        elif self.opcao == '2':
            self.Lista_contatos()
        elif self.opcao == '3':
            self.Excluir()
        elif self.opcao == '4':
            self.Buscar_nome()
        elif self.opcao == '5':
            self.Sair()

    def Cadastrar(self):
        idContato = self.id
        nome = input('Digite seu nome: ')
        telefone = input('Digite seu telefone: ')
        email = input('Digite seu email: ')
        # para criar e gravar no arquivo txt
        try:
            agenda = open("agenda.txt", "a")
            dados = f'{idContato};{nome};{telefone},{email} \n'
            agenda.write(dados)
            agenda.close()
            print('Contato salvo com sucesso')
        except:
            print('Houve um erro')

    def Lista_contatos(self):
        agenda = open("agenda.txt", "r")
        for contato in agenda:
            print(contato)
        agenda.close()

    def Limpar(self):
        self.opcao = ''
        self.id = random.randint(1, 10000)

    def Buscar_nome(self):
        agenda = open("agenda.txt", "r")
        for contato in agenda:
            print(contato)
        agenda.close()


    def Excluir(self):
        print(f'Você selecionou a opção de excluir o contato com ID {self.id}.')

    def Sair(self):
        print("Até mais")
        exit()


agenda = AgendaTelefonica()
agenda.Iniciar()

while True:
    pergunta = input('Deseja continuar? [s] Sim | [n] Não ')
    if pergunta.lower() == 's':
        agenda.Limpar()
        agenda.Iniciar()
    elif pergunta.lower() == 'n':
        break
    else:
        print("Escolha uma das opções abaixo")
