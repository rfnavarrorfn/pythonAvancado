from tkinter import ttk

from modulos import *
import sqlite3


class funcoes():
    def limpar_tela(self):
        self.entry_codigo.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_cpf.delete(0, END)
        self.entry_telefone.delete(0, END)
        self.entry_endereco.delete(0, END)
        self.entry_veiculo.delete(0, END)
        #self.combobox_servico.set(0, END)
        self.entry_data.delete(0, END)
        self.entry_situacao.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")

    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao banco de dados")

    def montar_tabela(self):
        self.conecta_bd()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
        cod INTEGER PRIMARY KEY,
        nome CHAR(40),
        cpf CHAR(20),
        telefone CHAR(20),
        endereco CHAR(40),
        veiculo CHAR(40),
        servico CHAR(40),
        data CHAR(20),
        situacao CHAR(20)        
        );
        """)
        self.conn.commit()
        self.desconecta_bd()

    def add_cliente(self):
        self.codigo = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        self.cpf = self.entry_cpf.get()
        self.telefone = self.entry_telefone.get()
        self.endereco = self.entry_endereco.get()
        self.veiculo = self.entry_veiculo.get()
        self.servico = self.combobox_servico.get()
        self.data = self.entry_data.get()
        self.situacao = self.entry_situacao.get()

        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO clientes ( nome, cpf, telefone, endereco, veiculo, servico,
        data, situacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (self.nome, self.cpf, self.telefone, self.endereco,
                                                             self.veiculo, self.servico, self.data, self.situacao))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpar_tela()

    def select_lista(self):
        self.lista1.delete(*self.lista1.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome, cpf, telefone, endereco, veiculo, servico, data, situacao
        FROM clientes ORDER BY nome ASC;""")
        for i in lista:
            self.lista1.insert("", END, value=i)
        self.desconecta_bd()

    def OnDoubleClick(self, event):
        self.limpar_tela()
        self.lista1.selection()
        for n in self.lista1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.lista1.item(n, 'values')
            self.entry_codigo.insert(END, col1)
            self.entry_nome.insert(END, col2)
            self.entry_cpf.insert(END, col3)
            self.entry_telefone.insert(END, col4)
            self.entry_endereco.insert(END, col5)
            self.entry_veiculo.insert(END, col6)
            self.combobox_servico.set(col7)
            self.entry_data.insert(END, col8)
            self.entry_situacao.insert(END, col9)

    def alterar_dados(self):
        self.codigo = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        self.cpf = self.entry_cpf.get()
        self.telefone = self.entry_telefone.get()
        self.endereco = self.entry_endereco.get()
        self.veiculo = self.entry_veiculo.get()
        self.combobox = self.combobox_servico.get()
        self.data = self.entry_data.get()
        self.situacao = self.entry_situacao.get()

        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome = ?, cpf = ?, telefone = ?, endereco = ?, veiculo = ?, servico = ?, data = ?,
        situacao = ? WHERE cod = ? """, (self.nome, self.cpf, self.telefone, self.endereco, self.veiculo, self.combobox,
                                          self.data, self.situacao, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpar_tela()

    def deletar_dados(self):
        self.codigo = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        self.cpf = self.entry_cpf.get()
        self.telefone = self.entry_telefone.get()
        self.endereco = self.entry_endereco.get()
        self.veiculo = self.entry_veiculo.get()
        self.servico = self.combobox_servico.get()
        self.data = self.entry_data.get()
        self.situacao = self.entry_situacao.get()

        self.conecta_bd()
        self.cursor.execute(""" DELETE FROM clientes WHERE cod = ? """, [self.codigo])
        self.conn.commit()
        self.desconecta_bd()
        self.limpar_tela()
        self.select_lista()

    def buscar_dados(self):
        self.conecta_bd()
        self.lista1.delete(*self.lista1.get_children())
        self.entry_nome.insert(END, '%')
        nome = self.entry_nome.get()
        self.cursor.execute(""" SELECT cod, nome, cpf, telefone, endereco, veiculo, servico, data, situacao FROM clientes 
         WHERE nome LIKE '%s' ORDER BY nome ASC""" % nome)
        busca_nome_cliente = self.cursor.fetchall()
        for i in busca_nome_cliente:
            self.lista1.insert("", END, values=i)
            self.limpar_tela()
            self.desconecta_bd()

