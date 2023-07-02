class AgendaTelefonica:
    def __init__(self):
        self.opcao = input('''
        ##########################
        projeto agenda python

        Menu:
        [1] cadastrar
        [2] lista contato
        ''')

    def Iniciar(self):
        inicio1 = self.opcao

agenda = AgendaTelefonica()
agenda.Iniciar()