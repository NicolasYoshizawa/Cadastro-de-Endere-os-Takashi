from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3


class Functions:
    
    def clear_display_main(self):
        self.entry_unidades.delete(0, END)
        self.entry_endereco.delete(0, END)
        
    def clear_label_main(self):
        self.label_sashimi['text'] = '0 un de Sashimi fica R$0.00'
        self.label_sashimi_tako['text'] = '0 un de Sashimi Tako fica R$0.00'
        self.label_niguiri['text'] = '0 un de Niguiri Z fica R$0.00'
        self.label_niguiri_tako['text'] = '0 un de Niguiri Tako/Ebi fica R$0.00'
        self.label_gyoza['text'] = '0 un de Gyozá fica R$0.00'
        
    def clear_display_toplevel1(self):
        self.entry_nome.delete(0, END)
        self.entry_taxa.delete(0, END)
        self.entry_codigo.delete(0, END)
        
    def clear_display_toplevel2(self):
        self.entry_nome.delete(0, END)
        self.entry_preco.delete(0, END)
        self.entry_codigo.delete(0, END)
    
    def variaves_main(self):
        self.unidades = self.entry_unidades.get()
        self.endereco = self.entry_endereco.get()
        
        
    def variaveis_toplevel1(self):
        self.nome_endereco = self.entry_nome.get().title().strip()
        self.taxa_entrega = self.entry_taxa.get()
        self.codigo = self.entry_codigo.get()
        
    def variaveis_toplevel2(self):
        self.nome_prato = self.entry_nome.get().title().strip()
        self.preco_prato = self.entry_preco.get()
        self.codigo = self.entry_codigo.get()
    
    def treeview_address(self, frame, width_column1, width_column2):
        self.style = ttk.Style()
        self.style.theme_use('default')
        
        self.list_address = ttk.Treeview(frame, height=3, columns=('col1', 'col2', 'col3'))
        self.list_address.heading('#0', text='')
        self.list_address.heading('#1', text='Codigo')
        self.list_address.heading('#2', text='Endereço')
        self.list_address.heading('#3', text='Taxa de Entrega')
        
        self.list_address.column('#0', width=1)
        self.list_address.column('#1', width=50)
        self.list_address.column('#2', width=width_column1)
        self.list_address.column('#3', width=width_column2)
        
    def treeview_prices(self, frame, width_column1, width_column2):
        self.style = ttk.Style()
        self.style.theme_use('default')
        
        self.list_prices = ttk.Treeview(frame, height=3, columns=('col1', 'col2', 'col3'))
        self.list_prices.heading('#0', text='')
        self.list_prices.heading('#1', text='Codigo')
        self.list_prices.heading('#2', text='Prato')
        self.list_prices.heading('#3', text='Preço por Unidade')
        
        self.list_prices.column('#0', width=1)
        self.list_prices.column('#1', width=50)
        self.list_prices.column('#2', width=width_column1)
        self.list_prices.column('#3', width=width_column2)
        
        
    
    def scrollbar(self):
        self.scrollbar = Scrollbar(self.window, orient='vertical')
        
    def connect_database(self, database):
        self.connect = sqlite3.connect('./databases/' + database)
        self.cursor = self.connect.cursor()
        print('Connecting to database')    
        
    def disconnect_database(self):
        self.cursor.close()
        self.connect.close()
        print('Disconnecting from database')
        
    def create_database_address(self):
        self.connect_database('endereco.db')
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS endereco (
                cod INTEGER PRIMARY KEY,
                address CHAR(40) NOT NULL,
                delivery_fee FLOAT(20)
            );
        """)
        self.connect.commit()
        print('Database created')
        self.disconnect_database()

    def create_database_prices(self):
        self.connect_database('preco.db')
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS preco (
                cod INTEGER PRIMARY KEY,
                item CHAR(40) NOT NULL,
                item_price FLOAT(20)
            );
        """)
        self.connect.commit()
        print('Database created')
        self.disconnect_database()
        
        pratos = {
                'Sashimi': 0.0, 
                'Sashimi Tako': 0.0,
                'Niguiri Z': 0.0, 
                'Niguiri Ebi/Tako': 0.0, 
                'Gyozá': 0.0
                }
        self.connect_database('preco.db')
        self.cursor.execute(f""" SELECT * FROM preco""")
        query = self.cursor.fetchall()
        self.disconnect_database()
        if query == []:
            self.connect_database('preco.db')
            for i in pratos:
                self.cursor.execute(""" INSERT INTO preco (item, item_price)
                                    VALUES (?, ?)""", (i, pratos[i]))
                self.connect.commit()
            self.disconnect_database()

            
    def select_list_address(self):
        self.list_address.delete(*self.list_address.get_children())
        self.connect_database('endereco.db')
        list = self.cursor.execute(""" SELECT cod, address, delivery_fee FROM endereco
                                   ORDER BY address ASC; """)
        for i in list:
            x = i[0]
            y = i[1]
            z = f'R${i[2]:.2f}'
            i = (x, y, z)
            self.list_address.insert('', END, values=i)
        self.disconnect_database()
            
    def select_list_prices(self):
        self.list_prices.delete(*self.list_prices.get_children())
        self.connect_database('preco.db')
        list = self.cursor.execute(""" SELECT cod, item, item_price FROM preco
                                   ORDER BY cod ASC; """)
        for i in list:
            x = i[0]
            y = i[1]
            z = f'R${i[2]:.2f}'
            i = (x, y, z)
            self.list_prices.insert('', END, values=i)    
        self.disconnect_database()
    
    def double_click_toplevel1(self, event):
        self.x = 1
        self.clear_display_toplevel1()
        self.list_address.selection()
        for n in self.list_address.selection():
            col1, col2, col3 = self.list_address.item(n, 'values')
            col3 = col3.replace('R$', '')
            self.entry_codigo.insert(END, col1)
            self.entry_nome.insert(END, col2)
            self.entry_taxa.insert(END, col3)
            
    def double_click_toplevel2(self, event):
        self.clear_display_toplevel2()
        self.list_prices.selection()
        for n in self.list_prices.selection():
            col1, col2, col3 = self.list_prices.item(n, 'values')
            col3 = col3.replace('R$', '')
            self.entry_codigo.insert(END, col1)
            self.entry_nome.insert(END, col2)
            self.entry_preco.insert(END, col3)
        
    """ ----------------- CRUD Main ---------------- """
    def read_main(self, event):
        self.connect_database('endereco.db')
        self.list_address.delete(*self.list_address.get_children())
        self.entry_endereco.insert(END, '%')
        self.entry_endereco.insert(0,'%')
        nome = self.entry_endereco.get()
        search_name = self.cursor.execute(
            """ SELECT cod, address, delivery_fee FROM endereco
            WHERE address LIKE '%s' ORDER BY address ASC""" % nome)
        for i in search_name:
            x = i[0]
            y = i[1]
            z = f'R${i[2]:.2f}'
            i = (x, y, z)
            self.list_address.insert('', END, values=i)
        self.clear_display_main()
        self.disconnect_database()   
        
    def calculate(self, event):
        try:
            self.variaves_main()
            self.unidades = float(self.unidades)
            self.connect_database('preco.db')
            quant = int(self.unidades)
            self.cursor.execute(""" SELECT item_price FROM preco ORDER BY cod ASC""")
            values = self.cursor.fetchall()
            sashimi = values[0][0] * quant
            sashimi_tako = values[1][0] * quant
            niguiri_z = values[2][0] * quant
            niguiri_tako_ebi = values[3][0] * quant
            gyoza = values[4][0] * quant
            self.label_sashimi['text'] = '{} un de Sashimi fica R${:.2f}'.format(quant, sashimi)
            self.label_sashimi_tako['text'] = '{} un de Sashimi Tako fica R${:.2f}'.format(quant, sashimi_tako)
            self.label_niguiri['text'] = '{} un de Niguiri Z fica R${:.2f}'.format(quant, niguiri_z)
            self.label_niguiri_tako['text'] = '{} un de Niguiri Tako/Ebi fica R${:.2f}'.format(quant, niguiri_tako_ebi)
            self.label_gyoza['text'] = '{} un de Gyozá fica R${:.2f}'.format(quant, gyoza)
            self.disconnect_database()
            self.clear_display_main()
        except:
            msg = """Digite um valor válido!
Obs: Casas decimais serão ignoradas"""
            messagebox.showinfo('Calculo de Preço - Aviso!!', msg)
            self.clear_display_main()
            self.clear_label_main()
    """ -------------- CRUD Toplevel1 -------------- """
    def create_toplevel1(self, event):
        try:
            self.variaveis_toplevel1()
            self.connect_database('endereco.db')
            self.cursor.execute(f""" SELECT * FROM endereco WHERE address = '{self.nome_endereco}'""")
            query = self.cursor.fetchall()
            self.disconnect_database()
            if query == []:
                if self.nome_endereco == '' or self.taxa_entrega == '':
                    msg = 'Preencha todos os campos para cadastrar um novo endereço!'
                    messagebox.showinfo('Cadastro de Endereço - Aviso!!', msg)
                else:
                    self.taxa_entrega = float(self.taxa_entrega)
                    self.connect_database('endereco.db')
                    self.cursor.execute(""" INSERT INTO endereco (address, delivery_fee)
                                        VALUES (?, ?)""", (self.nome_endereco, self.taxa_entrega))
                    self.connect.commit()
                    self.disconnect_database()
                    self.select_list_address()
                    self.clear_display_toplevel1()
            else:
                msg = 'Endereço já existente!'
                messagebox.showinfo('Cadastro de Endereço - Aviso!!', msg)
        except:
            msg = """Digite um valor válido!
Obs: Casas decimais devem ser representadas com ponto"""
            messagebox.showinfo('Cadastro de Endereço - Aviso!!', msg)
            self.clear_display_toplevel1()
            
    def read_toplevel1(self, event):
        self.connect_database('endereco.db')
        self.list_address.delete(*self.list_address.get_children())
        self.entry_nome.insert(END, '%')
        self.entry_nome.insert(0,'%')
        nome = self.entry_nome.get()
        search_name = self.cursor.execute(
            """ SELECT cod, address, delivery_fee FROM endereco
            WHERE address LIKE '%s' ORDER BY address ASC""" % nome)
        for i in search_name:
                x = i[0]
                y = i[1]
                z = f'R${i[2]:.2f}'
                i = (x, y, z)
                self.list_address.insert('', END, values=i)
        self.clear_display_toplevel1()
        self.disconnect_database()
    
    def update_toplevel1(self, event):
        try:
            self.variaveis_toplevel1()
            if self.nome_endereco == '' or self.taxa_entrega == '':
                msg = 'Selecione um endereço para editar!'
                messagebox.showinfo('Cadastro de Endereço - Aviso!!', msg)
            else:
                self.taxa_entrega = float(self.taxa_entrega)
                self.connect_database('endereco.db')
                self.cursor.execute(f""" SELECT * FROM endereco WHERE cod = '{self.codigo}'""")
                query = self.cursor.fetchall()
                self.disconnect_database()
                if query == []:
                    msg = 'Selecione um endereço existente para editá-lo'
                    messagebox.showinfo('Cadastro de Endereço - Aviso!!', msg)
                    self.clear_display_toplevel1()
                else:
                    self.connect_database('endereco.db')
                    self.connect_database('endereco.db')
                    self.cursor.execute(""" UPDATE endereco SET address = ?, delivery_fee = ?
                                        Where cod = ?""", (self.nome_endereco, self.taxa_entrega, self.codigo))
                    self.connect.commit()
                    self.disconnect_database()
                    self.select_list_address()
                    self.clear_display_toplevel1()
        except:
            msg = """Digite um valor válido!
Obs: Casas decimais devem ser representadas com ponto"""
            messagebox.showinfo('Cadastro de Endereço - Aviso!!', msg)
            self.clear_display_toplevel1()
        
    def delete_toplevel1(self):
        self.variaveis_toplevel1()
        if self.nome_endereco == '' or self.taxa_entrega == '':
            msg = 'Selecione um endereço para excluir!'
            messagebox.showinfo('Cadastro de Endereço - Aviso!!', msg)
        else:
            self.connect_database('endereco.db')
            self.cursor.execute("""DELETE FROM endereco WHERE cod = ? """, [self.codigo])
            self.connect.commit()
            self.disconnect_database()
            self.clear_display_toplevel1()
            self.select_list_address()
            
    """ -------------- CRUD Toplevel2 -------------- """
    def read_toplevel2(self, event):
        self.connect_database('preco.db')
        self.list_prices.delete(*self.list_prices.get_children())
        
        self.entry_nome.insert(END, '%')
        nome = self.entry_nome.get()
        search_name = self.cursor.execute(
            """ SELECT cod, item, item_price FROM preco
            WHERE item LIKE '%s' ORDER BY cod ASC""" % nome)
        for i in search_name:
                x = i[0]
                y = i[1]
                z = f'R${i[2]:.2f}'
                i = (x, y, z)
                self.list_prices.insert('', END, values=i)
        self.clear_display_toplevel2()
        self.disconnect_database()
        
    def update_toplevel2(self, event):
        try:
            self.variaveis_toplevel2()
            if self.nome_prato == '' or self.preco_prato == '':
                msg = 'Selecione um prato para editar!'
                messagebox.showinfo('Cadastro de Preço - Aviso!!', msg)
            else:
                self.connect_database('preco.db')
                self.cursor.execute(f""" SELECT * FROM preco WHERE cod = '{self.codigo}'""")
                query = self.cursor.fetchall()
                self.disconnect_database()
                if query == []:
                    msg = 'Selecione um prato válido para editar!'
                    messagebox.showinfo('Cadastro de Preço - Aviso!!', msg)
                else:
                    self.preco_prato = float(self.preco_prato)
                    if self.nome_prato == '' or self.preco_prato == '':
                        msg = 'Selecione um prato para editar!'
                        messagebox.showinfo('Cadastro de Preço - Aviso!!', msg)
                    else:
                        self.connect_database('preco.db')

                        self.cursor.execute(""" UPDATE preco SET item_price = ?
                                            Where cod = ?""", (self.preco_prato, self.codigo))
                        self.connect.commit()
                        self.disconnect_database()
                        self.select_list_prices()
                        self.clear_display_toplevel2()
        except:
            msg = """Digite um valor válido!
Obs: Casas decimais devem ser representadas com ponto"""
            messagebox.showinfo('Cadastro de Preço - Aviso!!', msg)
            self.clear_display_toplevel2()
            
    def delete_toplevel2(self):
        self.variaveis_toplevel2()
        if self.nome_prato == '' or self.preco_prato == '':
            msg = 'Selecione um prato para deletar!'
            messagebox.showinfo('Cadastro de Preço - Aviso!!', msg)
        else:
            self.connect_database('preco.db')

            self.cursor.execute(""" UPDATE preco SET item_price = ?
                                Where cod = ?""", (0, self.codigo))
            self.connect.commit()
            self.disconnect_database()
            self.select_list_prices()
            self.clear_display_toplevel2()
            
            