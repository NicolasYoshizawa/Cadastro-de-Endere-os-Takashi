from tkinter import *
from tkinter import ttk
from functions import Functions


        

class Toplevel2(Functions):
    def __init__(self):
        self.window =  Toplevel()
        self.background_img = PhotoImage(file = f"./prices screen images/background.png")
        self.entry0_img = PhotoImage(file = f"./prices screen images/img_textBox0.png")
        self.entry1_img = PhotoImage(file = f"./prices screen images/img_textBox1.png")
        self.entry2_img = PhotoImage(file = f"./prices screen images/img_textBox2.png")
        self.entry3_img = PhotoImage(file = f"./prices screen images/img_textBox3.png")
        self.img0 = PhotoImage(file = f"./prices screen images/img0.png")
        self.img1 = PhotoImage(file = f"./prices screen images/img1.png")
        self.img2 = PhotoImage(file = f"./prices screen images/img2.png")
        self.pratos = ['Sashimi', 'Sashimi Tako', 'Niguiri Z', 'Niguiri Ebi/Tako', 'Gyozá']
        self.start()
        
    def start(self):
        self.windows_configuration()
        self.select_list_prices()
        self.window.mainloop()
    
    def windows_configuration(self):
        self.window.geometry("720x550")
        self.window.configure(bg = "#ffffff")
        self.window.iconbitmap('./icon/White-image.ico')
        
        canvas = Canvas(
            self.window,
            bg = "#ffffff",
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
            407.0, 405.0,
            image = self.entry0_img)
        
        # Frame
        self.frame1 = Frame(self.window)
        self.frame1.place(x = 157, y = 275, width = 500, height = 258)

        # Treeview
        self.treeview_prices(self.frame1, 200, 100)
        self.list_prices.place(x=0, y=0, width=500, height=258)
        self.list_prices.bind('<Double-1>', self.double_click_toplevel2)
        
        # ScrollBar
        self.scrollbar()
        self.list_prices.configure(yscroll=self.scrollbar.set)
        self.scrollbar.config(command=self.list_prices.yview)
        self.scrollbar.place(x=658, y=275, width=15, height=260)
        
        entry1_bg = canvas.create_image(
            380.0, 169.0,
            image = self.entry1_img)


        self.style_combobox = ttk.Style()
        self.style_combobox.configure('TCombobox', background= 'gray')
        
        self.entry_nome = Entry(
            master = self.window,
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0
        )
        

        self.entry_nome.place(
            x = 227.0, y = 155,
            width = 308.0,
            height = 28)
        
        self.entry_nome.bind('<Return>', self.read_toplevel2)

        entry2_bg = canvas.create_image(
            590.5, 169.0,
            image = self.entry2_img)

        self.entry_codigo = Entry(
            self.window,
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        self.entry_codigo.place(
            x = 568.0, y = 155,
            width = 50.0,
            height = 28)

        entry3_bg = canvas.create_image(
            317.0, 238.0,
            image = self.entry3_img)

        self.entry_preco = Entry(
            self.window,
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        self.entry_preco.place(
            x = 227.0, y = 224,
            width = 182.0,
            height = 28)
        
        self.entry_preco.bind('<Return>', self.update_toplevel2)

        botao_buscar = Button(
            self.window,
            activebackground='#464242',
            bg='#464242',
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.read_toplevel2(None),
            relief = "flat")

        botao_buscar.place(
            x = 209, y = 49,
            width = 104,
            height = 44)

        botao_editar = Button(
            self.window,
            activebackground='#464242',
            bg='#464242',
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.update_toplevel2(None),
            relief = "flat")

        botao_editar.place(
            x = 367, y = 49,
            width = 104,
            height = 44)

        botao_deletar = Button(
            self.window,
            activebackground='#464242',
            bg='#464242',
            image = self.img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.delete_toplevel2,
            relief = "flat")

        botao_deletar.place(
            x = 517, y = 49,
            width = 104,
            height = 44)

        self.window.resizable(False, False)
        self.window.focus_force()
        self.window.grab_set()
    

if __name__ == '__main__':
    Toplevel2()