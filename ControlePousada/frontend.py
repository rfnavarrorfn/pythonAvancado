import sys
import tkinter.font

import customtkinter

from modulos import *
from backend import *

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()


class Aplicacoes(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame()
        self.monta_tabelas()
        self.select_lista()
        self.root.mainloop()

    def tela(self):
        self.root.title("Pousada & SPA Recanto do Sossego")
        self.root.geometry("1920x1080")   # 1920x1080 configuração do meu monitor atual
        self.root.resizable(True, True)

    def frames_da_tela(self):
        self.frame1 = customtkinter.CTkFrame(self.root)
        self.frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def widgets_frame1(self):
        self.label_formulario = customtkinter.CTkLabel(self.frame1, text="(Formulário de Cadastro)")
        self.label_formulario.place(relx=0.10, rely=0.01)

        self.label_codigo = customtkinter.CTkLabel(self.frame1, text="Código")
        self.label_codigo.place(relx=0.01, rely=0.01)

        self.entry_codigo = customtkinter.CTkEntry(self.frame1)
        self.entry_codigo.place(relx=0.05, rely=0.01, relwidth=0.02)

        self.label_nome = customtkinter.CTkLabel(self.frame1, text="Nome do hóspede")
        self.label_nome.place(relx=0.01, rely=0.05)

        self.entry_nome = customtkinter.CTkEntry(self.frame1)
        self.entry_nome.place(relx=0.01, rely=0.08, relwidth=0.30)

        self.label_cpf = customtkinter.CTkLabel(self.frame1, text="CPF")
        self.label_cpf.place(relx=0.32, rely=0.05)

        self.entry_cpf = customtkinter.CTkEntry(self.frame1)
        self.entry_cpf.place(relx=0.32, rely=0.08, relwidth=0.20)

        self.label_telefone = customtkinter.CTkLabel(self.frame1, text="Telefone")
        self.label_telefone.place(relx=0.54, rely=0.05)

        self.entry_telefone = customtkinter.CTkEntry(self.frame1)
        self.entry_telefone.place(relx=0.54, rely=0.08)

        self.label_celular = customtkinter.CTkLabel(self.frame1, text="Celular")
        self.label_celular.place(relx=0.76, rely=0.05)

        self.entry_celular = customtkinter.CTkEntry(self.frame1)
        self.entry_celular.place(relx=0.76, rely=0.08, relwidth=0.23)

        self.label_endereco = customtkinter.CTkLabel(self.frame1, text="Endereço")
        self.label_endereco.place(relx=0.01, rely=0.12)

        self.entry_endereco = customtkinter.CTkEntry(self.frame1)
        self.entry_endereco.place(relx=0.01, rely=0.15, relwidth=0.51)

        self.label_complemento = customtkinter.CTkLabel(self.frame1, text="Complemento")
        self.label_complemento.place(relx=0.54, rely=0.12)

        self.entry_complemento = customtkinter.CTkEntry(self.frame1)
        self.entry_complemento.place(relx=0.54, rely=0.15)

        self.label_cep = customtkinter.CTkLabel(self.frame1, text="Cep")
        self.label_cep.place(relx=0.76, rely=0.12)

        self.entry_cep = customtkinter.CTkEntry(self.frame1)
        self.entry_cep.place(relx=0.76, rely=0.15, relwidth=0.23)

        self.label_quarto = customtkinter.CTkLabel(self.frame1, text="Número do quarto")
        self.label_quarto.place(relx=0.01, rely=0.19)

        self.entry_quarto = customtkinter.CTkEntry(self.frame1)
        self.entry_quarto.place(relx=0.01, rely=0.22)

        self.label_data_entrada = customtkinter.CTkLabel(self.frame1, text="Data de entrada")
        self.label_data_entrada.place(relx=0.32, rely=0.19)

        self.entry_data_entrada = customtkinter.CTkEntry(self.frame1)
        self.entry_data_entrada.place(relx=0.32, rely=0.22, relwidth=0.20)

        self.label_hora_entrada = customtkinter.CTkLabel(self.frame1, text="Hora de entrada")
        self.label_hora_entrada.place(relx=0.54, rely=0.19)

        self.entry_hora_entrada = customtkinter.CTkEntry(self.frame1)
        self.entry_hora_entrada.place(relx=0.54, rely=0.22, relwidth=0.20)

        self.label_data_saida = customtkinter.CTkLabel(self.frame1, text="Data de saída")
        self.label_data_saida.place(relx=0.32, rely=0.25)

        self.entry_data_saida = customtkinter.CTkEntry(self.frame1)
        self.entry_data_saida.place(relx=0.32, rely=0.28, relwidth=0.20)

        self.label_hora_saida = customtkinter.CTkLabel(self.frame1, text="Hora de saída")
        self.label_hora_saida.place(relx=0.54, rely=0.25)

        self.entry_hora_saida = customtkinter.CTkEntry(self.frame1)
        self.entry_hora_saida.place(relx=0.54, rely=0.28, relwidth=0.20)

        self.botao_cadastro = customtkinter.CTkButton(self.frame1, text="Cadastrar", command=self.add_cliente, fg_color="grey")
        self.botao_cadastro.place(relx=0.01, rely=0.95)

        self.botao_buscar = customtkinter.CTkButton(self.frame1, text="Buscar hóspede", command=self.buscar_registro)
        self.botao_buscar.place(relx=0.12, rely=0.95)

        self.botao_excluir_cadastro = customtkinter.CTkButton(self.frame1, text="Excluir cadastro", command=self.deleta_hospede)
        self.botao_excluir_cadastro.place(relx=0.20, rely=0.95)

        self.botao_limpar = customtkinter.CTkButton(self.frame1, text="Limpar formulário", command=self.limpa_tela)
        self.botao_limpar.place(relx=0.32, rely=0.95)

        self.botao_sair = customtkinter.CTkButton(self.frame1, text="Sair", command=sys.exit)
        self.botao_sair.place(relx=0.90, rely=0.95)

        self.botao_alterar = customtkinter.CTkButton(self.frame1, text="Alterar", command=self.alterar_dados)
        self.botao_alterar.place(relx=0.40, rely=0.95)

        self.botao_google = customtkinter.CTkButton(self.frame1, text="Google", command=self.abrir_google)
        self.botao_google.place(relx=0.49, rely=0.95)

    def lista_frame(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="lightgrey")
        self.lista1 = ttk.Treeview(self.frame1, height=3,
                                  columns=("col1", "col2", "col3", "col4", "col5",
                                           "col6", "col7", "col8", "col9", "col10", "col11", "col12", "col13"))
        self.lista1.heading("#0", text="")
        self.lista1.heading("#1", text="Código")
        self.lista1.heading("#2", text="Nome do hóspede")
        self.lista1.heading("#3", text="CPF")
        self.lista1.heading("#4", text="Telefone")
        self.lista1.heading("#5", text="Celular")
        self.lista1.heading("#6", text="Endereço")
        self.lista1.heading("#7", text="Complemento")
        self.lista1.heading("#8", text="Cep")
        self.lista1.heading("#9", text="Nº quarto")
        self.lista1.heading("#10", text="Data entrada")
        self.lista1.heading("#11", text="Hora entrada")
        self.lista1.heading("#12", text="Data saída")
        self.lista1.heading("#13", text="Hora saída")

        self.lista1.column("#0", width=20)
        self.lista1.column("#1", width=30)
        self.lista1.column("#2", width=20)
        self.lista1.column("#3", width=20)
        self.lista1.column("#4", width=20)
        self.lista1.column("#5", width=20)
        self.lista1.column("#6", width=20)
        self.lista1.column("#7", width=20)
        self.lista1.column("#8", width=20)
        self.lista1.column("#9", width=20)
        self.lista1.column("#10", width=20)
        self.lista1.column("#11", width=20)
        self.lista1.column("#12", width=20)
        self.lista1.column("#13", width=20)

        self.lista1.place(relx=0.01, rely=0.45, relwidth=0.98, relheight=0.48)

        self.lista1.bind("<Double-1>", self.OnDoubleClick)


Aplicacoes()
