# Programa para cadastro de clientes feito em python sql e tkinter
# (Cadastro de Clientes 2.0.1)

# arquivo com as funções de back-end

# Funções do back-end

from modulos import *

class Funcs():
    def limpa_tela(self):
        self.entry_codigo.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_endereco.delete(0, END)
        self.entry_telefone.delete(0, END)
        self.entry_nomepet.delete(0, END)
        self.entry_racapet.delete(0, END)
        self.entry_tiposervico.delete(0, END)
        self.entry_valor.delete(0, END)
        self.entry_valor_total.delete(0, END)
        self.entry_situacao.delete(0, END)
        self.entry_observacao.delete("1.0", "end - 1 chars")
        self.entry_segunda.delete(0, END)
        self.entry_terca.delete(0, END)
        self.entry_quarta.delete(0, END)
        self.entry_quinta.delete(0, END)
        self.entry_sexta.delete(0, END)
        self.entry_sabado.delete(0, END)
        self.entry_domingo.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")

    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao banco de dados")

    def monta_tabelas(self):
        self.conecta_bd()
        ### Criando a tabela em SQL
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                endereco CHAR(40), 
                telefone INTEGER(20),
                nomepet CHAR(30),
                racapet CHAR(30), 
                tiposervico CHAR(30),
                valor INTEGER(10),
                valor_total INTEGER(10),
                situacao INTEGER(10),
                observacao CHAR(10),
                segunda CHAR(10),
                terca CHAR(10),
                quarta CHAR(10),
                quinta CHAR(10),
                sexta CHAR(10),
                sabado CHAR(10),
                domingo CHAR(10)
            );                
        """)
        self.conn.commit()
        self.desconecta_bd()

    def add_cliente(self):
        self.codigo = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        self.endereco = self.entry_endereco.get()
        self.telefone = self.entry_telefone.get()
        self.nomepet = self.entry_nomepet.get()
        self.racapet = self.entry_racapet.get()
        self.tiposervico = self.entry_tiposervico.get()
        self.valor = self.entry_valor.get()
        self.valor_total = self.entry_valor_total.get()
        self.situacao = self.entry_situacao.get()
        self.observacao = self.entry_observacao.get("1.0", "end - 1 chars")
        self.segunda = self.entry_segunda.get()
        self.terca = self.entry_terca.get()
        self.quarta = self.entry_quarta.get()
        self.quinta = self.entry_quinta.get()
        self.sexta = self.entry_sexta.get()
        self.sabado = self.entry_sabado.get()
        self.domingo = self.entry_domingo.get()

        messagebox.showinfo("SOS Cachorro - Informa!", "Cliente cadastrado com sucesso!")

        pygame.mixer.init()
        pygame.mixer.music.load("som_bt_novo.mp3")
        pygame.mixer.music.play()

        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, endereco, 
        telefone, nomepet, racapet, tiposervico, valor, valor_total, situacao, observacao, segunda, terca, quarta, 
        quinta, sexta, sabado, domingo)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (self.nome, self.endereco, self.telefone, self.nomepet,
        self.racapet, self.tiposervico, self.valor, self.valor_total, self.situacao, self.observacao, self.segunda,
        self.terca, self.quarta, self.quinta, self.sexta, self.sabado, self.domingo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def select_lista(self):
        self.lista1.delete(*self.lista1.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, endereco, telefone, nomepet, 
        racapet, tiposervico, valor, valor_total, situacao, observacao, segunda, terca, quarta, quinta, sexta, sabado, domingo FROM clientes 
        ORDER BY nome_cliente ASC;""")
        for i in lista:
            self.lista1.insert("", END, values=i)
        self.desconecta_bd()

    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.lista1.selection()
        for n in self.lista1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, \
            col13, col14, col15, col16, col17, col18 = self.lista1.item(n, 'values')
            self.entry_codigo.insert(END, col1)
            self.entry_nome.insert(END, col2)
            self.entry_endereco.insert(END, col3)
            self.entry_telefone.insert(END, col4)
            self.entry_nomepet.insert(END, col5)
            self.entry_racapet.insert(END, col6)
            self.entry_tiposervico.insert(END, col7)
            self.entry_valor.insert(END, col8)
            self.entry_valor_total.insert(END, col9)
            self.entry_situacao.insert(END, col10)
            self.entry_observacao.insert(END, col11)
            self.entry_segunda.insert(END, col12)
            self.entry_terca.insert(END, col13)
            self.entry_quarta.insert(END, col14)
            self.entry_quinta.insert(END, col15)
            self.entry_sexta.insert(END, col16)
            self.entry_sabado.insert(END, col17)
            self.entry_domingo.insert(END, col18)

    def deleta_cliente(self):
        if (messagebox.askyesnocancel("Atenção!", "Deseja mesmo excluir o registro?")):
            self.codigo = self.entry_codigo.get()
            self.nome = self.entry_nome.get()
            self.endereco = self.entry_endereco.get()
            self.telefone = self.entry_telefone.get()
            self.nomepet = self.entry_nomepet.get()
            self.racapet = self.entry_racapet.get()
            self.tiposervico = self.entry_tiposervico.get()
            self.valor = self.entry_valor.get()
            self.valor_total = self.entry_valor_total.get()
            self.situacao = self.entry_situacao.get()
            self.observacao = self.entry_observacao.get("1.0", "end - 1 chars")
            self.segunda = self.entry_segunda.get()
            self.terca = self.entry_terca.get()
            self.quarta = self.entry_quarta.get()
            self.quinta = self.entry_quinta.get()
            self.sexta = self.entry_sexta.get()
            self.sabado = self.entry_sabado.get()
            self.domingo = self.entry_domingo.get()

            self.conecta_bd()
            self.cursor.execute(""" DELETE FROM clientes WHERE cod = ? """, [self.codigo])
            self.conn.commit()
            self.desconecta_bd()
            self.limpa_tela()
            self.select_lista()

            messagebox.showinfo("SOS Cachorro informa!", "Registro excluído com sucesso!")

    def altera_cliente(self):
        if (messagebox.askyesnocancel("Atenção!", "Deseja mesmo alterar os dados desse cliente?")):
            self.codigo = self.entry_codigo.get()
            self.nome = self.entry_nome.get()
            self.endereco = self.entry_endereco.get()
            self.telefone = self.entry_telefone.get()
            self.nomepet = self.entry_nomepet.get()
            self.racapet = self.entry_racapet.get()
            self.tiposervico = self.entry_tiposervico.get()
            self.valor = self.entry_valor.get()
            self.valor_total = self.entry_valor_total.get()
            self.situacao = self.entry_situacao.get()
            self.observacao = self.entry_observacao.get("1.0", "end - 1 chars")
            self.segunda = self.entry_segunda.get()
            self.terca = self.entry_terca.get()
            self.quarta = self.entry_quarta.get()
            self.quinta = self.entry_quinta.get()
            self.sexta = self.entry_sexta.get()
            self.sabado = self.entry_sabado.get()
            self.domingo = self.entry_domingo.get()

            self.conecta_bd()
            self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, endereco = ?, 
            telefone = ?, nomepet = ?, racapet = ?, tiposervico = ?, valor = ?, valor_total = ?, situacao = ?, 
            observacao = ?, segunda = ?, terca = ?, quarta = ?, quinta = ?, sexta = ?, sabado = ?, domingo = ? 
            WHERE cod = ? """,
                                (self.nome, self.endereco, self.telefone, self.nomepet,
                                 self.racapet, self.tiposervico, self.valor, self.valor_total, self.situacao, self.observacao, self.segunda,
                                 self.terca, self.quarta, self.quinta, self.sexta, self.sabado, self.domingo,
                                 self.codigo))
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista()
            self.limpa_tela()

            messagebox.showinfo("SOS Cachorro informa!", "Dados alterados com sucesso!")

    def busca_cliente(self):
        self.conecta_bd()
        self.lista1.delete(*self.lista1.get_children())
        self.entry_nome.insert(END, '%')
        nome = self.entry_nome.get()
        self.cursor.execute("""
        SELECT cod, nome_cliente, endereco, telefone, nomepet, racapet, tiposervico, 
        valor, valor_total, situacao, observacao, segunda, terca, quarta, quinta, sexta, sabado, domingo FROM clientes
        WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC""" % nome)
        busca_nome_cliente = self.cursor.fetchall()
        for i in busca_nome_cliente:
            self.lista1.insert("", END, values=i)
            self.limpa_tela()
            self.desconecta_bd()

    def printSegunda(self):
        dataIni = self.calendario1.get_date()
        self.entry_segunda.insert(END, dataIni)

    def printTerca(self):
        dataIni = self.calendario1.get_date()
        self.entry_terca.insert(END, dataIni)

    def printQuarta(self):
        dataIni = self.calendario1.get_date()
        self.entry_quarta.insert(END, dataIni)

    def printQuinta(self):
        dataIni = self.calendario1.get_date()
        self.entry_quinta.insert(END, dataIni)

    def printsexta(self):
        dataIni = self.calendario1.get_date()
        self.entry_sexta.insert(END, dataIni)

    def printSabado(self):
        dataIni = self.calendario1.get_date()
        self.entry_sabado.insert(END, dataIni)

    def printDomingo(self):
        dataIni = self.calendario1.get_date()
        self.entry_domingo.insert(END, dataIni)

    def printSituacao(self):
        self.entry_situacao.insert(self.var1, self.var2)
