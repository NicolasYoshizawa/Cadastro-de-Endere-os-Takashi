from tkinter import *
from Factory.functions import Functions


class Toplevel1(Functions):
    def __init__(self):
        self.window = Toplevel()
        self.background_img = PhotoImage(file = f"./address screen images/background.png")
        self.entry0_img = PhotoImage(file = f"./address screen images/img_textBox0.png")
        self.entry1_img = PhotoImage(file = f"./address screen images/img_textBox1.png")
        self.entry2_img = PhotoImage(file = f"./address screen images/img_textBox2.png")
        self.img0 = PhotoImage(file = f"./address screen images/img0.png")
        self.img1 = PhotoImage(file = f"./address screen images/img1.png")
        self.img2 = PhotoImage(file = f"./address screen images/img2.png")
        self.img3 = PhotoImage(file = f"./address screen images/img3.png")
        self.entry3_img = PhotoImage(file = f"./address screen images/img_textBox3.png")
        self.start()
    
    def start(self):
        self.windows_configuration()
        self.select_list_address()
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
        self.treeview_address(self.frame1, 200, 100)
        self.list_address.place(x=0, y=0, width=500, height=258)
        self.list_address.bind('<Double-1>', self.double_click_toplevel1)
        
        # ScrollBar
        self.scrollbar()
        self.list_address.configure(yscroll=self.scrollbar.set)
        self.scrollbar.config(command=self.list_address.yview)
        self.scrollbar.place(x=658, y=275, width=15, height=260)
        

        entry1_bg = canvas.create_image(
            317.0, 238.0,
            image = self.entry1_img)

        self.entry_taxa = Entry(
            master= self.window,
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        self.entry_taxa.place(
            x = 227.0, y = 224,
            width = 182.0,
            height = 28)

        self.entry_taxa.bind('<Return>', self.create_toplevel1)

        entry2_bg = canvas.create_image(
            380.0, 169.0,
            image = self.entry2_img)

        self.entry_nome = Entry(
            master= self.window,
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        self.entry_nome.place(
            x = 227.0, y = 155,
            width = 302.0,
            height = 28)
        
        self.entry_nome.bind('<Return>', self.read_toplevel1)
        
        entry3_bg = canvas.create_image(
            590.5, 169.0,
            image = self.entry3_img)

        self.entry_codigo = Entry(
            master= self.window,
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        self.entry_codigo.place(
            x = 566.0, y = 155,
            width = 44.0,
            height = 28)

        botao_buscar = Button(
            master= self.window,
            activebackground='#464242',
            bg='#464242',
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.read_toplevel1(None),
            relief = "flat")

        botao_buscar.place(
            x = 491, y = 218,
            width = 104,
            height = 44)

        botao_deletar = Button(
            master= self.window,
            activebackground='#464242',
            bg='#464242',
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.delete_toplevel1,
            relief = "flat")

        botao_deletar.place(
            x = 517, y = 49,
            width = 104,
            height = 44)

        botao_editar = Button(
            master= self.window,
            activebackground='#464242',
            bg='#464242',
            image = self.img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.update_toplevel1(None),
            relief = "flat")

        botao_editar.place(
            x = 367, y = 49,
            width = 104,
            height = 44)

        botao_adicionar = Button(
            master= self.window,
            activebackground='#464242',
            bg='#464242',
            image = self.img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.create_toplevel1(None),
            relief = "flat")

        botao_adicionar.place(
            x = 217, y = 49,
            width = 104,
            height = 44)

        self.window.resizable(False, False)
        self.window.focus_force()
        self.window.grab_set()  


if __name__ == '__main__':
    Toplevel1()