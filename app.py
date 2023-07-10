import mysql.connector

# Criando a conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='bdyoutube'
)

cursor = conexao.cursor()

def adicionar_registro():
    nome_produto = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do produto: "))

    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
    cursor.execute(comando)
    conexao.commit()
    print("Registro inserido com sucesso!")

def pesquisar_registros():
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print("Registros encontrados:")
    for registro in resultado:
        print(registro)

def atualizar_registro():
    nome_produto = input("Digite o nome do produto que deseja atualizar: ")
    novo_valor = float(input("Digite o novo valor do produto: "))

    comando = f'UPDATE vendas SET valor = {novo_valor} WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conexao.commit()
    print("Registro atualizado com sucesso!")

def excluir_registro():
    nome_produto = input("Digite o nome do produto que deseja excluir: ")

    comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conexao.commit()
    print("Registro excluído com sucesso!")

# Menu de opções
while True:
    print("Opções disponíveis:")
    print("1. Adicionar registro")
    print("2. Pesquisar registros")
    print("3. Atualizar registro")
    print("4. Excluir registro")
    print("0. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        adicionar_registro()
    elif opcao == "2":
        pesquisar_registros()
    elif opcao == "3":
        atualizar_registro()
    elif opcao == "4":
        excluir_registro()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")

cursor.close()
conexao.close()




'''
# criando conexao com bd
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database= 'bdyoutube',
)

cursor = conexao.cursor()
# CREATE inicio
#comando INSERT
nome_produto = "chocolate"
valor = 15
comando = f' INSERT INTO vendas (nome_produto,valor) VALUES ("{nome_produto}" , {valor})'
cursor.execute(comando)
conexao.commit() #edita o banco de dados atualizar o o bd
resultado = cursor.fetchall() #ler o banco de dados
# CREATE fim

# READ
# UPDATE
# DELETE



cursor.close()
conexao.close()
'''