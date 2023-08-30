# Programa para cadastro de clientes feito em python sql e tkinter
# (Cadastro de Clientes 2.0.1)

# arquivo principal com as funções de front-end
import click

from modulos import *
from funcionalidades import *

root = Tk()

# Funções do front-end
class Aplicações(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgetsdoframe1()
        self.lista_frame2()
        self.monta_tabelas()
        self.select_lista()
        self.menu()
        root.mainloop()

    def tela(self):
        self.root.title("SOS Cachorro - Cadastro de clientes - Versão 2.0.1 - Desenvolvido por Raphael Navarro")
        self.root.configure(background="lightgray")
        self.root.geometry("1920x1080")

    def frames_da_tela(self):
        self.frame1 = Frame(self.root, bg="lightgray", highlightbackground="white", highlightthickness=5)
        self.frame1.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.48)

        self.frame2 = Frame(self.root, bg="gray", highlightbackground="white", highlightthickness=5)
        self.frame2.place(relx=0.01, rely=0.51, relwidth=0.98, relheight=0.48)

    def widgetsdoframe1(self):
        ### Imagem do frame1
        self.imagem = ImageTk.PhotoImage(Image.open("cadastro.png"))
        label_imagem = Label(self.frame1, image=self.imagem)
        label_imagem.place(relx=0.02, rely=0.6, relwidth=0.17, relheight=0.3)

        ### Criação dos botões

        self.botao_novo = Button(self.frame1, text="Novo", command=self.add_cliente)
        self.botao_novo.place(relx=0.16, rely=0.025, relwidth=0.14, relheight=0.12)

        self.botao_limpar = Button(self.frame1, text="Limpar", command=self.limpa_tela)
        self.botao_limpar.place(relx=0.31, rely=0.025, relwidth=0.14, relheight=0.12)

        self.botao_buscar = Button(self.frame1, text="Buscar", command=self.busca_cliente)
        self.botao_buscar.place(relx=0.46, rely=0.025, relwidth=0.14, relheight=0.12)

        self.botao_alterar = Button(self.frame1, text="Alterar", command=self.altera_cliente)
        self.botao_alterar.place(relx=0.61, rely=0.025, relwidth=0.14, relheight=0.12)

        self.botao_apagar = Button(self.frame1, text="Apagar", command=self.deleta_cliente)
        self.botao_apagar.place(relx=0.76, rely=0.025, relwidth=0.14, relheight=0.12)

        self.botao_sair = Button(self.frame1, text="Sair", command=exit)
        self.botao_sair.place(relx=0.91, rely=0.025, relwidth=0.08, relheight=0.96)

        ### Criação das labels e entrys
        self.label_codigo = Label(self.frame1, text="Código", bg="lightgray")
        self.label_codigo.place(relx=0.01)

        self.entry_codigo = Entry(self.frame1)
        self.entry_codigo.place(relx=0.01, rely=0.06)

        self.label_nome = Label(self.frame1, text="Nome", bg="lightgray")
        self.label_nome.place(relx=0.01, rely=0.15, relwidth=0.08)

        self.entry_nome = Entry(self.frame1)
        self.entry_nome.place(relx=0.01, rely=0.21, relwidth=0.89)

        self.label_endereco = Label(self.frame1, text="Endereço", bg="lightgray")
        self.label_endereco.place(relx=0.01, rely=0.27, relwidth=0.08)

        self.entry_endereco = Entry(self.frame1)
        self.entry_endereco.place(relx=0.01, rely=0.33, relwidth=0.45)

        self.label_telefone = Label(self.frame1, text="Telefone", bg="lightgray")
        self.label_telefone.place(relx=0.47, rely=0.27, relwidth=0.08)

        self.entry_telefone = Entry(self.frame1)
        self.entry_telefone.place(relx=0.47, rely=0.33, relwidth=0.43)

        self.labelPet = Label(self.frame1, text="Dados do Pet", bg="lightgray")
        self.labelPet.place(relx=0.01, rely=0.4)

        self.label_nomepet = Label(self.frame1, text="Nome", bg="lightgray")
        self.label_nomepet.place(relx=0.01, rely=0.45, relwidth=0.08)

        self.entry_nomepet = Entry(self.frame1)
        self.entry_nomepet.place(relx=0.01, rely=0.5, relwidth=0.45)

        self.label_racapet = Label(self.frame1, text="Raça", bg="lightgray")
        self.label_racapet.place(relx=0.47, rely=0.45, relwidth=0.08)

        self.entry_racapet = Entry(self.frame1)
        self.entry_racapet.place(relx=0.49, rely=0.5, relwidth=0.3)

        self.label_tiposervico = Label(self.frame1, text="Tipo de serviço", bg="lightgray")
        self.label_tiposervico.place(relx=0.2, rely=0.55, relwidth=0.08)

        self.entry_tiposervico = Entry(self.frame1)
        self.entry_tiposervico.place(relx=0.2, rely=0.60, relwidth=0.3)

        self.label_valor = Label(self.frame1, text="Valor diário", bg="lightgray")
        self.label_valor.place(relx=0.2, rely=0.645)

        self.entry_valor = Entry(self.frame1)
        self.entry_valor.place(relx=0.2, rely=0.69)

        self.label_valor_total = Label(self.frame1, text="Valor mensal", bg="lightgray")
        self.label_valor_total.place(relx=0.2, rely=0.75)

        self.entry_valor_total = Entry(self.frame1)
        self.entry_valor_total.place(relx=0.2, rely=0.80)

        self.label_situacao = Label(self.frame1, text="Situação / Data Pagto", bg="lightgray")
        self.label_situacao.place(relx=0.34, rely=0.645)

        self.entry_situacao = Entry(self.frame1)
        self.entry_situacao.place(relx=0.34, rely=0.69)

        self.label_observacao = Label(self.frame1, text="Observação / Anotações")
        self.label_observacao.place(relx=0.34, rely=0.75)

        self.entry_observacao = Text(self.frame1, width=40, height=5)
        self.entry_observacao.place(relx=0.34, rely=0.80)

        # Dias da semana
        self.bt_segunda = Button(self.frame1, text="Segunda", command=self.printSegunda)
        self.bt_segunda.place(relx=0.52, rely=0.55)

        self.entry_segunda = Entry(self.frame1, width=10)
        self.entry_segunda.place(relx=0.58, rely=0.55)

        self.bt_terca = Button(self.frame1, text="Terça", command=self.printTerca).place(relx=0.52, rely=0.61)

        self.entry_terca = Entry(self.frame1, width=10)
        self.entry_terca.place(relx=0.58, rely=0.61)

        self.bt_quarta = Button(self.frame1, text="Quarta", command=self.printQuarta).place(relx=0.52, rely=0.67)

        self.entry_quarta = Entry(self.frame1, width=10)
        self.entry_quarta.place(relx=0.58, rely=0.67)

        self.bt_quinta = Button(self.frame1, text="Quinta", command=self.printQuinta).place(relx=0.52, rely=0.73)

        self.entry_quinta = Entry(self.frame1, width=10)
        self.entry_quinta.place(relx=0.58, rely=0.73)

        self.bt_sexta = Button(self.frame1, text="Sexta", command=self.printsexta).place(relx=0.52, rely=0.79)

        self.entry_sexta = Entry(self.frame1, width=10)
        self.entry_sexta.place(relx=0.58, rely=0.79)

        self.bt_sabado = Button(self.frame1, text="Sábado", command=self.printSabado).place(relx=0.52, rely=0.852)

        self.entry_sabado = Entry(self.frame1, width=10)
        self.entry_sabado.place(relx=0.58, rely=0.852)

        self.bt_domingo = Button(self.frame1, text="Domingo", command=self.printDomingo).place(relx=0.52, rely=0.915)

        self.entry_domingo = Entry(self.frame1, width=10)
        self.entry_domingo.place(relx=0.58, rely=0.915)

        ### Calendário fixo
        self.calendario1 = Calendar(self.frame1, fg="gray75", bg="blue", font=("Times", "9", "bold"),
                                    locale="pt_br")
        self.calendario1.place(relx=0.66, rely=0.56)

    def lista_frame2(self):
        self.lista1 = ttk.Treeview(self.frame2, height=3,
                                   columns=("col1", "col2", "col3", "col4", "col5", "col6",
                                            "col7", "col8", "col9", "col10", "col11", "col12",
                                            "col13", "col14", "col15", "col16", "col17", "col18"))
        self.lista1.heading("#0", text="")
        self.lista1.heading("#1", text="Código")
        self.lista1.heading("#2", text="Nome")
        self.lista1.heading("#3", text="Endereço")
        self.lista1.heading("#4", text="Telefone")
        self.lista1.heading("#5", text="Nome Pet")
        self.lista1.heading("#6", text="Raça")
        self.lista1.heading("#7", text="Serviço")
        self.lista1.heading("#8", text="Valor diário")
        self.lista1.heading("#9",text="Valor mensal")
        self.lista1.heading("#10", text="Situação / Data Pagto")
        self.lista1.heading("#11", text="Observação / Anotações")
        self.lista1.heading("#12", text="Segunda")
        self.lista1.heading("#13", text="Terça")
        self.lista1.heading("#14", text="Quarta")
        self.lista1.heading("#15", text="Quinta")
        self.lista1.heading("#16", text="Sexta")
        self.lista1.heading("#17", text="Sábado")
        self.lista1.heading("#18", text="Domingo")

        self.lista1.column("#0", width=1)
        self.lista1.column("#1", width=50)
        self.lista1.column("#2", width=200)
        self.lista1.column("#3", width=200)
        self.lista1.column("#4", width=50)
        self.lista1.column("#5", width=200)
        self.lista1.column("#6", width=200)
        self.lista1.column("#7", width=200)
        self.lista1.column("#8", width=200)
        self.lista1.column("#9", width=200)
        self.lista1.column("#10", width=200)
        self.lista1.column("#11", width=200)
        self.lista1.column("#12", width=200)
        self.lista1.column("#13", width=200)
        self.lista1.column("#14", width=200)
        self.lista1.column("#15", width=200)
        self.lista1.column("#16", width=200)
        self.lista1.column("#17", width=200)
        self.lista1.column("#18", width=200)

        self.lista1.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame2, orient='vertical')
        self.lista1.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

        self.lista1.bind("<Double-1>", self.OnDoubleClick)

    def menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def quit(): self.root.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Mapa", menu=filemenu2)

        filemenu.add_command(label="Sair", command=quit)

        def map():

            label1 = LabelFrame()
            label1.pack(pady=20)

            mapwidget = tkintermapview.TkinterMapView(label1, width=1500, height=800)
            mapwidget.set_position(-23.533773, -46.625290)  # Latitude e longitude
            mapwidget.set_zoom(15)
            botaosair = Button(label1, text="Sair", command=label1.destroy)
            botaosair.place(relx=0.9, rely=0.01)

            mapwidget.pack()

        filemenu2.add_command(label="Mapa", command=map)


Aplicações()
