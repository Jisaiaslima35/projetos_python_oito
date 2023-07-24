from tkinter.ttk import *
from tkinter import*
from tkinter import messagebox

# cores
co0 = '#f0f3f5' #preto
co1 = '#f0f3f5' #cinza
co2 = '#feffff' #branca
co3 = '#38576b' #valor
co4 = '#f0f3f5' #letra
co5 = '#ef5350' #vermelho
co6 = '#93cd95' #

janela = Tk ()
janela.title ('')
janela.geometry('500x450')
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use('clam')

frame_cima = Frame(janela,width=500, height=50, bg=co3, relief='flat')
frame_cima.grid(row=0, column=0,pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela,width=500, height=150, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0,pady=1, padx=0, sticky=NSEW)

frame_tabela = Frame(janela,width=500, height=248, bg=co2, relief='flat')
frame_tabela.grid(row=2, column=0, columnspan=2,pady=1, padx=10, sticky=NW)

#configurando a frame cima titulo
l_nome = Label(frame_cima, text='Agenda Telefonica', anchor=NE, font=('times 20 bold'), bg=co3, fg=co1)
l_nome.place(x=7, y=5)

# campo nome
l_nome = Label(frame_baixo, text='Nome: *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co5 )
l_nome.place(x=10, y=20)
# caixa de entrada de texto
e_nome = Entry(frame_baixo, width=27,justify='left', font=('', 10), highlightthickness=1)
e_nome.place(x=80, y=20)

#campo sexo
# config frame baixo
l_sexo = Label(frame_baixo, text='Sexo: *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co5 )
l_sexo.place(x=10, y=50)
# caixa de entrada de texto
s_sexo = Combobox(frame_baixo, width=27)
s_sexo['value'] = ('', 'F', 'M')
s_sexo.place(x=80, y=50)

#campo telefone
l_telefone = Label(frame_baixo, text='Telefone: *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co5 )
l_telefone.place(x=10, y=80)
# caixa de entrada de texto
e_telefone = Entry(frame_baixo, width=27,justify='left', font=('', 10), highlightthickness=1)
e_telefone.place(x=80, y=80)

#campo email
l_email = Label(frame_baixo, text='Email: *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co5 )
l_email.place(x=10, y=110)
# caixa de entrada de texto
e_email = Entry(frame_baixo, width=27,justify='left', font=('', 10), highlightthickness=1)
e_email.place(x=80, y=110)

#campo procurar
b_procurar = Button(frame_baixo, text='Procurar: *', font=('Ivy 8 bold'), bg=co1, fg=co5, relief=RAISED, overrelief=RIDGE )
b_procurar.place(x=290, y=20)
# caixa de entrada de texto
e_procurar = Entry(frame_baixo, width=16,justify='left', font=('', 10), highlightthickness=1)
e_procurar.place(x=363, y=21)

# boato ver dados
e_ver_dados = Button(frame_baixo,  text='Ver Dados: *', font=('Ivy 8 bold'), bg=co1, fg=co5, relief=RAISED, overrelief=RIDGE )
e_ver_dados.place(x=290, y=50)

e_ver_dados = Button(frame_baixo,  text='Ver Dados: *', font=('Ivy 8 bold'), bg=co1, fg=co5, relief=RAISED, overrelief=RIDGE )
e_ver_dados.place(x=400, y=50)

e_ver_dados = Button(frame_baixo,  text='Atualizar: *', justify='center', font=('Ivy 8 bold'), bg=co1, fg=co5, relief=RAISED, overrelief=RIDGE )
e_ver_dados.place(x=400, y=80)

e_ver_dados = Button(frame_baixo,  text='Deletar: *', font=('Ivy 8 bold'), bg=co1, fg=co5, relief=RAISED, overrelief=RIDGE )
e_ver_dados.place(x=400, y=110)






janela.mainloop()
