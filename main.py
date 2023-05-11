from tkinter import *
from tkinter.font import Font
from functions import Functions
from toplevel1 import Toplevel1
from toplevel2 import Toplevel2

    

class Application(Functions):
    def __init__(self):
        self.window = Tk()
        self.background_img = PhotoImage(file = f"./main screen images/background.png")
        self.entry0_img = PhotoImage(file = f"./main screen images/img_textBox0.png")
        self.entry1_img = PhotoImage(file = f"./main screen images/img_textBox1.png")
        self.entry2_img = PhotoImage(file = f"./main screen images/img_textBox2.png")
        self.img0 = PhotoImage(file = f"./main screen images/img0.png")
        self.img1 = PhotoImage(file = f"./main screen images/img1.png")
        self.img2 = PhotoImage(file = f"./main screen images/img2.png")
        self.img3 = PhotoImage(file = f"./main screen images/img3.png")
        self.fonte = Font(family="Inter",size=11,weight="bold")
        self.start()
        
    def start(self):
        self.windows_configuration()
        self.create_database_address()
        self.create_database_prices()
        self.select_list_address()
        self.window.mainloop()

    def windows_configuration(self):
        self.window.geometry("720x550")
        self.window.configure(bg = "#464242")
        self.window.title('')
        self.window.iconbitmap('./icon/White-image.ico')

        canvas = Canvas(
            self.window,
            bg = "#464242",
            height = 550,
            width = 720,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background = canvas.create_image(
            360.0, 275.0,
            image=self.background_img)

        entry0_bg = canvas.create_image(
            495.0, 48.5,
            image = self.entry0_img)

        self.entry_unidades = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0,)

        self.entry_unidades.place(
            x = 420.0, y = 38,
            width = 150.0,
            height = 23)
        
        self.entry_unidades.bind('<Return>', self.calculate)

        entry1_bg = canvas.create_image(
            496.0, 298.5,
            image = self.entry1_img)

        self.entry_endereco = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        self.entry_endereco.place(
            x = 421.0, y = 288,
            width = 150.0,
            height = 23)
        
        self.entry_endereco.bind('<Return>', self.read_main)

        # Frame 
        self.frame1 = Frame(self.window)
        self.frame1.place(x = 293, y = 373, width = 405, height = 160)
        
        # Treeview
        self.treeview_address(self.frame1, 200, 125)
        self.list_address.place(x=0, y=0, width=405, height=160)
        
        # ScrollBar
        self.scrollbar()
        self.list_address.configure(yscroll=self.scrollbar.set)
        self.scrollbar.config(command=self.list_address.yview)
        self.scrollbar.place(x=698, y=373, width=15, height=160)    
        
        # Label Sashimi
        self.label_sashimi = Label(master=self.window, 
                              text='0 un de Sashimi fica R$0.00', 
                              font=self.fonte, 
                              background= "#464242", 
                              foreground='#ffffff', 
                              )
        self.label_sashimi.place(x=395, y=75)

        # Label Sashimi Tako
        self.label_sashimi_tako = Label(master=self.window, 
                                   text='0 un de Sashimi Tako fica R$0.00', 
                                   font=self.fonte, 
                                   background= "#464242", 
                                   foreground='#ffffff', 
                                   )
        self.label_sashimi_tako.place(x=395, y=100)
        
        # Label Niguiri Z
        self.label_niguiri = Label(master=self.window, 
                              text='0 un de Niguiri Z fica R$0.00', 
                              font=self.fonte, 
                              background= "#464242", 
                              foreground='#ffffff', 
                              )
        self.label_niguiri.place(x=395, y=125)
        
        # Label Niguiri Tako
        self.label_niguiri_tako = Label(master=self.window, 
                                   text='0 un de Niguiri Tako/Ebi fica R$0.00', 
                                   font=self.fonte, 
                                   background= "#464242", 
                                   foreground='#ffffff', 
                                   )
        self.label_niguiri_tako.place(x=395, y=150)
        
        # Label Gyoza
        self.label_gyoza = Label(master=self.window, 
                           text='0 un de Gyozá fica R$0.00', 
                           font=self.fonte, 
                           background= "#464242", 
                           foreground='#ffffff', 
                           )
        self.label_gyoza.place(x=395, y=175)

        # Botao Calcular
        botao_calcular = Button(
            activebackground='#464242',
            bg='#464242',
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.calculate(None),
            relief = "flat")

        botao_calcular.place(
            x = 452, y = 205,
            width = 88,
            height = 38)

        # Botao Buscar
        botao_buscar = Button(
            activebackground='#D9D9D9',
            bg='#D9D9D9',
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.read_main(None), 
            relief = "flat")

        botao_buscar.place(
            x = 452, y = 321,
            width = 88,
            height = 38)

        # Botao Alterar Precos
        botao_alterar_precos = Button(
            activebackground='#FFFFFF',
            bg='#FFFFFF',
            image = self.img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = Toplevel2,
            relief = "flat")

        botao_alterar_precos.place(
            x = 81, y = 321,
            width = 111,
            height = 42)

        # Botao Adicionar Endereco
        botao_adicionar_endereco = Button(
            activebackground='#FFFFFF',
            bg='#FFFFFF',
            image = self.img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = Toplevel1,
            relief = "flat")

        botao_adicionar_endereco.place(
            x = 71, y = 379,
            width = 131,
            height = 49)

        self.window.resizable(False, False)
        
        
Application()