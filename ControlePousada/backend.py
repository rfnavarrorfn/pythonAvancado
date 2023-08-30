import time
from tkinter import END

from modulos import *

class Funcs():
    def limpa_tela(self):
        self.entry_codigo.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_cpf.delete(0, END)
        self.entry_telefone.delete(0, END)
        self.entry_celular.delete(0, END)
        self.entry_endereco.delete(0, END)
        self.entry_complemento.delete(0, END)
        self.entry_cep.delete(0, END)
        self.entry_quarto.delete(0, END)
        self.entry_data_entrada.delete(0, END)
        self.entry_hora_entrada.delete(0, END)
        self.entry_data_saida.delete(0, END)
        self.entry_hora_saida.delete(0, END)


    def conecta_bd(self):
        self.conn = sqlite3.connect("hospedes.db")
        self.cursor = self.conn.cursor(); print("Conectando ao bando de dados")

    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao banco de dados")

    def monta_tabelas(self):
        self.conecta_bd()
        # Cria a tabela se não existir
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS hospedes (
            codigo INTEGER PRIMARY KEY,
            nome TEXT,
            cpf TEXT,
            telefone TEXT,
            celular TEXT,
            endereco TEXT,
            complemento TEXT,
            cep TEXT,
            quarto TEXT,
            data_entrada TEXT,
            hora_entrada TEXT,
            data_saida TEXT,
            hora_saida TEXT
        )''')
        self.conn.commit()
        self.desconecta_bd()

    def add_cliente(self):
        self.codigo = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        if not self.nome:
            messagebox.showerror("Atenção","O nome do hóspede é obrigatório para continuar!")
            return
        self.cpf = self.entry_cpf.get()
        if not self.cpf:
            messagebox.showerror("Atenção","O CPF do hóspede é obrigatório para continuar!")
            return
        self.telefone = self.entry_telefone.get()
        self.celular = self.entry_celular.get()
        if not self.celular:
            messagebox.showerror("Atenção","O celular do hóspede é obrigatório para continuar!")
            return
        self.endereco = self.entry_endereco.get()
        self.complemento = self.entry_complemento.get()
        self.cep = self.entry_cep.get()
        self.quarto = self.entry_quarto.get()
        self.data_entrada = self.entry_data_entrada.get()
        self.hora_entrada = self.entry_hora_entrada.get()
        self.data_saida = self.entry_data_saida.get()
        self.hora_saida = self.entry_hora_saida.get()

        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO hospedes (nome, cpf, telefone, celular,
        endereco, complemento, cep, quarto, data_entrada, hora_entrada, data_saida, hora_saida)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""", (self.nome, self.cpf, self.telefone,
                                              self.celular, self.endereco, self.complemento,
                                              self.cep, self.quarto, self.data_entrada, self.hora_entrada,
                                              self.data_saida, self.hora_saida))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def select_lista(self):

        self.lista1.delete(*self.lista1.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT codigo, nome, cpf, telefone, celular, endereco,
         complemento, cep, quarto, data_entrada, hora_entrada, data_saida, hora_saida FROM hospedes 
        ORDER BY nome ASC;""")
        for i in lista:
            self.lista1.insert("", END, values=i)
        self.desconecta_bd()

    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.lista1.selection()
        for n in self.lista1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13 = self.lista1.item(n, 'values')
            self.entry_codigo.insert(END, col1)
            self.entry_nome.insert(END, col2)
            self.entry_cpf.insert(END, col3)
            self.entry_telefone.insert(END, col4)
            self.entry_celular.insert(END, col5)
            self.entry_endereco.insert(END, col6)
            self.entry_complemento.insert(END, col7)
            self.entry_cep.insert(END, col8)
            self.entry_quarto.insert(END, col9)
            self.entry_data_entrada.insert(END, col10)
            self.entry_hora_entrada.insert(END, col11)
            self.entry_data_saida.insert(END, col12)
            self.entry_hora_saida.insert(END, col13)

    def deleta_hospede(self):
        self.codigo = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        self.cpf = self.entry_cpf.get()
        self.telefone = self.entry_telefone.get()
        self.celular = self.entry_celular.get()
        self.endereco = self.entry_endereco.get()
        self.complemento = self.entry_complemento.get()
        self.cep = self.entry_cep.get()
        self.quarto = self.entry_quarto.get()
        self.data_entrada = self.entry_data_entrada.get()
        self.hora_entrada = self.entry_hora_entrada.get()
        self.data_saida = self.entry_data_saida.get()
        self.hora_saida = self.entry_hora_saida.get()

        self.conecta_bd()
        self.cursor.execute(""" DELETE FROM hospedes WHERE codigo = ? """, [self.codigo])
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()

    def alterar_dados(self):
        if messagebox.askyesnocancel("Atenção", "Deseja mesmo alterar os dados desse hóspede?"):
            self.codigo = self.entry_codigo.get()
            self.nome = self.entry_nome.get()
            self.cpf = self.entry_cpf.get()
            self.telefone = self.entry_telefone.get()
            self.celular = self.entry_celular.get()
            self.endereco = self.entry_endereco.get()
            self.complemento = self.entry_complemento.get()
            self.cep = self.entry_cep.get()
            self.quarto = self.entry_quarto.get()
            self.data_entrada = self.entry_data_entrada.get()
            self.hora_entrada = self.entry_hora_entrada.get()
            self.data_saida = self.entry_data_saida.get()
            self.hora_saida = self.entry_hora_saida.get()

            self.conecta_bd()
            self.cursor.execute(""" UPDATE hospedes SET nome = ?, cpf = ?, telefone = ?, celular = ?, endereco = ?,
             complemento = ?, cep = ?, quarto = ?, data_entrada = ?, hora_entrada = ?, data_saida = ?, hora_saida = ? 
             WHERE codigo = ?  """, (self.nome, self.cpf, self.telefone, self.celular, self.endereco, self.complemento,
                                   self.cep, self.quarto, self.data_entrada, self.hora_entrada, self.data_saida,
                                   self.hora_saida, self.codigo))
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista()
            self.limpa_tela()

            messagebox.showinfo("Sistema informa:", "Dados alterados com sucesso!")

    def buscar_registro(self):
        self.conecta_bd()
        self.lista1.delete(*self.lista1.get_children())
        self.entry_nome.insert(END, '%')
        nome = self.entry_nome.get()
        self.cursor.execute("""
        SELECT codigo, nome, cpf, telefone, celular, endereco, complemento, cep, quarto, data_entrada, hora_entrada,
        data_saida, hora_saida FROM hospedes WHERE nome LIKE '%s' ORDER BY nome ASC """ % nome)
        busca_nome_cliente = self.cursor.fetchall()
        for i in busca_nome_cliente:
            self.lista1.insert("", END, values=i)
            self.limpa_tela()
            self.desconecta_bd()

    def abrir_google(self):
        webbrowser.open("https://www.google.com.br")













