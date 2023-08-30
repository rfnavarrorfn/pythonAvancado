import tkinter

from modulos import *
from backend import *


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()


class frontEnd(funcoes):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_tela()
        self.widgets_frame1()
        self.lista_frame1()
        self.montar_tabela()
        self.select_lista()
        self.root.mainloop()

    def tela(self):
        self.root.title("Lava Rápido - Wash-Car")
        self.root.geometry("1920x1080")# Configuração tela monitor atual 1920x1080

    def frames_tela(self):
        self.frame1 = customtkinter.CTkFrame(self.root, fg_color="lightgrey")
        self.frame1.place(relx=0.01, rely=0.01, relheight=0.98, relwidth=0.98)

    def widgets_frame1(self):
        # Labels, entrys e combobox
        font = customtkinter.CTkFont(size=20)
        self.label_formulario = customtkinter.CTkLabel(self.frame1, text="Formulário de cadastro de clientes", font=font)
        self.label_formulario.place(relx=0.35, rely=0.01)

        self.label_codigo = customtkinter.CTkLabel(self.frame1, text="Código")
        self.label_codigo.place(relx=0.01, rely=0.04)

        self.entry_codigo = customtkinter.CTkEntry(self.frame1)
        self.entry_codigo.place(relx=0.01, rely=0.07)

        self.label_nome = customtkinter.CTkLabel(self.frame1, text="Nome")
        self.label_nome.place(relx=0.18, rely=0.04)

        self.entry_nome = customtkinter.CTkEntry(self.frame1)
        self.entry_nome.place(relx=0.18, rely=0.07, relwidth=0.80)

        self.label_cpf = customtkinter.CTkLabel(self.frame1, text="CPF:")
        self.label_cpf.place(relx=0.01, rely=0.10)

        self.entry_cpf = customtkinter.CTkEntry(self.frame1)
        self.entry_cpf.place(relx=0.01, rely=0.13)

        self.label_telefone = customtkinter.CTkLabel(self.frame1, text="Telefone / WhatsApp")
        self.label_telefone.place(relx=0.18, rely=0.10)

        self.entry_telefone = customtkinter.CTkEntry(self.frame1)
        self.entry_telefone.place(relx=0.18, rely=0.13)

        self.label_endereco = customtkinter.CTkLabel(self.frame1, text="Endereço")
        self.label_endereco.place(relx=0.35, rely=0.10)

        self.entry_endereco = customtkinter.CTkEntry(self.frame1)
        self.entry_endereco.place(relx=0.35, rely=0.13, relwidth=0.63)

        self.label_veiculo = customtkinter.CTkLabel(self.frame1, text="Veículo")
        self.label_veiculo.place(relx=0.01, rely=0.16)

        self.entry_veiculo = customtkinter.CTkEntry(self.frame1)
        self.entry_veiculo.place(relx=0.01, rely=0.19, relwidth=0.32)

        self.label_servico = customtkinter.CTkLabel(self.frame1, text=" ***** Selecione abaixo o tipo de serviço *****     /     ***** Valor em R$ *****")
        self.label_servico.place(relx=0.35, rely=0.16)

        #self.combobox_servico = ttk.StringVar(value="")

        self.combobox_servico = ctk.CTkComboBox(master=self.frame1,
                                                          values=["",
                                                                  "Ducha com pretinho   R$ 15,00",
                                                                  "Lavagem simples - Carro pequeno  R$ 35,00",
                                                                  "Lavagem com cera - Carro pequeno R$ 40,00",
                                                                  "Lavagem simples - Carro grande   R$ 45,00",
                                                                  "Lavagem com cera - Carro grande  R$ 50,00",
                                                                  "Higienização R$ 200,00",
                                                                  "Lavagem Motor    R$ 150,00",
                                                                  ])
        self.combobox_servico.place(relx=0.35, rely=0.19, relwidth=0.63)

        self.label_data = customtkinter.CTkLabel(self.frame1, text="Data do serviço")
        self.label_data.place(relx=0.01, rely=0.22)

        self.entry_data = customtkinter.CTkEntry(self.frame1)
        self.entry_data.place(relx=0.01, rely=0.25)

        self.label_situacao = customtkinter.CTkLabel(self.frame1, text="Situação")
        self.label_situacao.place(relx=0.09, rely=0.22)

        self.entry_situacao = customtkinter.CTkEntry(self.frame1)
        self.entry_situacao.place(relx=0.09, rely=0.25)

        # Botões
        self.botao_cadastrar = customtkinter.CTkButton(self.frame1, text="Cadastrar", command=self.add_cliente)
        self.botao_cadastrar.place(relx=0.17, rely=0.25)

        self.botao_alterar = customtkinter.CTkButton(self.frame1, text="Alterar", command=self.alterar_dados)
        self.botao_alterar.place(relx=0.25, rely=0.25)

        self.botao_buscar = customtkinter.CTkButton(self.frame1, text="Buscar", command=self.buscar_dados)
        self.botao_buscar.place(relx=0.17, rely=0.29)

        self.botao_excluir = customtkinter.CTkButton(self.frame1, text="Excluir", command=self.deletar_dados)
        self.botao_excluir.place(relx=0.25, rely=0.29)

    # Criar um campo e-mail marketing em que ao clicar no botão enviar e-mail o programa envia um e-mail marketing automático

    def lista_frame1(self):
        style = ttk.Style()
        style.theme_use("clam")
        font = customtkinter.CTkFont(size=20)

        self.lista1 = ttk.Treeview(self.frame1, height=25, columns=("col1", "col2", "col3", "col4", "col5",
                                                                   "col6", "col7", "col8", "col9"))
        self.lista1.heading("#0", text="")
        self.lista1.heading("#1", text="Código")
        self.lista1.heading("#2", text="Nome")
        self.lista1.heading("#3", text="CPF")
        self.lista1.heading("#4", text="Telefone / WhatsApp")
        self.lista1.heading("#5", text="Endereço")
        self.lista1.heading("#6", text="Veículo")
        self.lista1.heading("#7", text="Tipo de serviço / Valor R$")
        self.lista1.heading("#8", text="Data do serviço")
        self.lista1.heading("#9", text="Situação")


        self.lista1.column("#0", width=20)
        self.lista1.column("#1", width=80)
        self.lista1.column("#2", width=300)
        self.lista1.column("#3", width=120)
        self.lista1.column("#4", width=200)
        self.lista1.column("#5", width=300)
        self.lista1.column("#6", width=180)
        self.lista1.column("#7", width=220)
        self.lista1.column("#8", width=160)
        self.lista1.column("#9", width=180)


        self.lista1.place(relx=0.01, rely=0.40)

        self.scroolLista = Scrollbar(self.frame1, orient="vertical")
        self.lista1.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.95, rely=0.40, relwidth=0.04, relheight=0.54)

        self.lista1.bind("<Double-1>", self.OnDoubleClick)


frontEnd()
