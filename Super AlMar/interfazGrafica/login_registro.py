from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import  StringVar,Frame
from conexion import *
import time
from app_administrador import administrador
class registro(Frame):
    def __init__(self):
        
        self.ventana=Tk()
        self.ventana.title("")
        self.ventana.minsize(height=750,width=1300)
        self.ventana.geometry('1000x50+180+80')
        self.ventana.call('wm','iconphoto',self.ventana._w,PhotoImage(file='Super AlMar\interfazGrafica\carrito-de-supermercado (1).png'))

        super().__init__()
        
    # variables boolean son señales para los botones
        self.menu=True
        self.color=True
    #es para los entry para obtener los textos productos
        
        self.nombre_cuenta= StringVar()
        self.apellido=StringVar()
        self.nombre1=StringVar()
        self.nombre2=StringVar()
        self.dni=StringVar()
        self.fecha_nacimiento=StringVar()
        self.domicilio=StringVar()
        self.email=StringVar()
        self.telefono= StringVar()
        self.contrasenia=StringVar()
        self.id_tipo_usuario=StringVar()
        
        self.buscar=StringVar()
        self.buscar_actualiza=StringVar()
    # base_datos objeto de la clase registro_producto
        self.base_datos=Conexion()
    #creamos los Frame
        self.frame_inicio=Frame(self.master,bg="DarkOliveGreen2",width=55,height=45)
        self.frame_inicio.grid_propagate(0)
        self.frame_inicio.grid(column=0,row=0,sticky="nsew") 
        #sticky es para que modifique en todo los sentido norte sur este oeste
        #frame_menu para el menu plegable
        self.frame_menu=Frame(self.master,bg="DarkOliveGreen2",width=50)
        self.frame_menu.grid_propagate(0)
        self.frame_menu.grid(column=0,row=1,sticky="nsew")
        #frame_top es para el titulo
        self.frame_top=Frame(self.master,bg="DarkOliveGreen2",height=50)
        self.frame_top.grid(column=1,row=0,sticky="nsew")
        #frame_principal almacenamos todo la pagina del contenido en si
        self.frame_principal=Frame(self.master,bg="DarkOliveGreen2")
        self.frame_principal.grid(column=1,row=1,sticky="nsew")
        self.master.columnconfigure(1,weight=1)
        self.master.rowconfigure(1,weight=1)
        self.frame_principal.columnconfigure(0,weight=1)
        self.frame_principal.rowconfigure(0,weight=1)
    
        self.widgets()
        self.ventana.mainloop()
        
        
    def pantalla_inicial(self):
        self.paginas.select([self.frame_uno])
        
    def pantalla_datos(self):
        self.paginas.select([self.frame_dos])
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.columnconfigure(1, weight=1)
        self.frame_dos.rowconfigure(2, weight=1)
        
    def pantalla_escribir(self):
        self.paginas.select([self.frame_tres])
        self.frame_tres.columnconfigure(0, weight=1)
        self.frame_tres.columnconfigure(1, weight=1)
        
    def menu_lateral(self):
        if self.menu is True:
            for i in range(50,170,10):				
                self.frame_menu.config(width= i)
                self.frame_inicio.config(width= i)
                self.frame_menu.update()
                clik_inicio = self.bt_cerrar.grid_forget()
                if clik_inicio is None:		
                    self.bt_inicio.grid(column=0, row=0, padx =10, pady=10)
                    self.bt_inicio.grid_propagate(0)
                    self.bt_inicio.config(width=i)
                    self.pantalla_inicial()
                    self.menu = False
        else:
            for i in range(170,50,-10):
                self.frame_menu.config(width= i)
                self.frame_inicio.config(width= i)
                self.frame_menu.update()
                clik_inicio = self.bt_inicio.grid_forget()
                if clik_inicio is   None:
                    self.frame_menu.grid_propagate(0)		
                    self.bt_cerrar.grid(column=0, row=0, padx=20, pady=200)
                    self.bt_cerrar.grid_propagate(0)
                    self.bt_cerrar.config(width=i)
                    self.pantalla_inicial()
            self.menu = True 
    
    def widgets(self):
        
        self.imagen_inicio = PhotoImage(file ='Super AlMar\interfazGrafica\clave (2).png')
        self.imagen_menu = PhotoImage(file ='Super AlMar\interfazGrafica\clave (2).png')
        self.imagen_datos = PhotoImage(file ='Super AlMar\interfazGrafica\iniciar-sesion.png')
        self.imagen_registrar = PhotoImage(file ='Super AlMar\interfazGrafica\derechos-de-autor (2).png')
        
        self.logo = PhotoImage(file ='Super AlMar\interfazGrafica\Bolsa-de-la-compra (2).png')
        self.imagen_uno = PhotoImage(file ='Super AlMar\interfazGrafica\Registro.png')
        self.imagen_dos= PhotoImage(file ='Super AlMar\interfazGrafica\iniciar-sesion (2).png')
        self.bt_inicio = Button(self.frame_inicio, image= self.imagen_inicio, bg='DarkOliveGreen2',activebackground='DarkOliveGreen2', bd=0, command = self.menu_lateral)
        self.bt_inicio.grid(column=0, row=0, padx=10, pady=10)
        self.bt_cerrar = Button(self.frame_inicio, image= self.imagen_menu, bg='DarkOliveGreen2',activebackground='DarkOliveGreen2', bd=0, command = self.menu_lateral)
        self.bt_cerrar.grid(column=0, row=0, padx=10, pady=10)	
		#BOTONES Y ETIQUETAS DEL MENU LATERAL 
        Button(self.frame_menu, image= self.imagen_datos, bg='DarkOliveGreen2', activebackground='DarkOliveGreen2', bd=0, command = self.pantalla_datos).grid(column=0, row=1, pady=20,padx=1)
        Button(self.frame_menu, image= self.imagen_registrar, bg='DarkOliveGreen2',activebackground='DarkOliveGreen2', bd=0, command =self.pantalla_escribir ).grid(column=0, row=2, pady=20,padx=1)
        
        Label(self.frame_menu, text='Iniciar sesion', bg= 'DarkOliveGreen2', fg= 'black', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=1, pady=20, padx=2)
        Label(self.frame_menu, text='Registrarse', bg= 'DarkOliveGreen2', fg= 'black', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=2, pady=20, padx=2)
        
        	#############################  CREAR  PAGINAS  ##############################
        estilo_paginas = ttk.Style()
        estilo_paginas.configure("TNotebook", background='DarkOliveGreen2', foreground='black', padding=0, borderwidth=0)
        estilo_paginas.theme_use('default')
        estilo_paginas.configure("TNotebook", background='DarkOliveGreen2', borderwidth=0)
        estilo_paginas.configure("TNotebook.Tab", background="DarkOliveGreen2", borderwidth=0)
        estilo_paginas.map("TNotebook", background=[("selected", 'DarkOliveGreen2')])
        estilo_paginas.map("TNotebook.Tab", background=[("selected", 'DarkOliveGreen2')], foreground=[("selected", 'DarkOliveGreen2')])

		#CREACCION DE LAS PAGINAS 
        self.paginas = ttk.Notebook(self.frame_principal , style= 'TNotebook') #, style = 'TNotebook'
        self.paginas.grid(column=0,row=0, sticky='nsew')
        self.frame_uno = Frame(self.paginas, bg='white')
        self.frame_dos = Frame(self.paginas, bg='DarkSeaGreen1')
        self.frame_tres = Frame(self.paginas, bg='pale turquoise')
        
        self.paginas.add(self.frame_uno)
        self.paginas.add(self.frame_dos)
        self.paginas.add(self.frame_tres)
        
		##############################         PAGINAS       #############################################

		######################## FRAME TITULO #################
        self.titulo = Label(self.frame_top,text= 'SUPER ALMAR', bg='DarkOliveGreen2', fg= 'black', font= ('Imprint MT Shadow', 28, 'bold'))
        self.titulo.pack(expand=1)
		######################## VENTANA PRINCIPAL #################
        Label(self.frame_uno, text= 'Bienvenido a nuestra tienda oline', bg='white', fg= 'forest green', font= ('Freehand521 BT', 30, 'bold')).pack(expand=1)
        Label(self.frame_uno ,image= self.logo, bg='white').pack(expand=1)

		######################## INICIO SESION #################
        Label(self.frame_dos, text= 'Inicio de Sesion', bg='DarkSeaGreen1', fg= 'green4', font= ('Comic Sans MS', 15, 'bold')).grid(column =0, row=0)
        Label(self.frame_dos, text = 'Nombre_usuario',fg='navy', bg ='DarkOliveGreen2', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=5, padx=5)
        Label(self.frame_dos, text = 'Contraseña',fg='navy', bg ='DarkOliveGreen2', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=5)
        Entry(self.frame_dos, textvariable=self.nombre_cuenta , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=1)
        Entry(self.frame_dos, textvariable=self.contrasenia, font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=2)
        
        Button(self.frame_dos,command= self.verificar, text='Ingresar', font=('Arial',18,'bold'), bg='DarkOliveGreen2').grid(column=1,row=3, pady=5, padx=4)
        Label(self.frame_dos, image= self.imagen_dos, bg= 'DarkSeaGreen1').grid(column= 3, rowspan= 7, row = 0, padx= 50)
        self.aviso_guardado = Label(self.frame_dos, bg= 'white', font=('Comic Sans MS', 15), fg='black')
        self.aviso_guardado.grid(columnspan= 2 , column =2, row = 4, padx= 5)
        
        
		######################## AGREGAR NUEVO USUARIO #################
        Label(self.frame_tres, text = 'Agrege sus datos',fg='purple', bg ='pale turquoise', font=('Comic Sans MS', 15, 'bold')).grid(columnspan=1, column=0,row=0, pady=2)
        Label(self.frame_tres, text = 'Nombre_usuario',fg='navy', bg ='pale turquoise', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15, padx=5)
        Label(self.frame_tres, text = 'Contraseña',fg='navy', bg ='pale turquoise', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
        Label(self.frame_tres, text = 'Apellido',fg='navy', bg ='pale turquoise', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
        Label(self.frame_tres, text = 'Primer Nombre', fg='navy',bg ='pale turquoise', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
        Label(self.frame_tres, text = 'Segundo Nombre',fg='navy', bg ='pale turquoise', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)  ##E65561
        Label(self.frame_tres, text = 'DNI',fg='navy', bg ='pale turquoise', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=15) 
        Label(self.frame_tres, text = 'Fecha de nacimiento',fg='navy', bg ='pale turquoise', font=('Rockwell',13,'bold')).grid(column=0,row=7, pady=15) 
        Label(self.frame_tres, text = 'Domicilio',fg='navy', bg ='pale turquoise', font=('Rockwell',13,'bold')).grid(column=0,row=8, pady=15) 
        Label(self.frame_tres, text = 'Email',fg='navy', bg ='pale turquoise', font=('Rockwell',13,'bold')).grid(column=0,row=9, pady=15) 
        Label(self.frame_tres, text = 'Telefono',fg='navy', bg ='pale turquoise', font=('Rockwell',13,'bold')).grid(column=0,row=10, pady=15) 
        Label(self.frame_tres, text = 'numero_administrador',fg='navy', bg ='pale turquoise', font=('Rockwell',13,'bold')).grid(column=0,row=11, pady=15) 
        
        Entry(self.frame_tres, textvariable=self.nombre_cuenta , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=1)
        Entry(self.frame_tres, textvariable=self.contrasenia, font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=2)
        Entry(self.frame_tres, textvariable=self.apellido , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=3)
        Entry(self.frame_tres, textvariable=self.nombre1, font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=4)
        Entry(self.frame_tres, textvariable=self.nombre2 , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=5)
        Entry(self.frame_tres, textvariable=self.dni, font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=6)
        Entry(self.frame_tres, textvariable=self.fecha_nacimiento , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=7)
        Entry(self.frame_tres, textvariable=self.domicilio, font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=8)
        Entry(self.frame_tres, textvariable=self.email , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=9)
        Entry(self.frame_tres, textvariable=self.telefono , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=10)
        Entry(self.frame_tres, textvariable=self.id_tipo_usuario , font=('Comic Sans MS', 12),highlightbackground = "DarkOrchid1", highlightcolor= "green2", highlightthickness=5).grid(column=1,row=11)
        
        Button(self.frame_tres,command= self.agregar_datos, text='REGISTRARSE', font=('Arial',18,'bold'), bg='purple2').grid(column=3,row=8, pady=10, padx=4)
        Label(self.frame_tres, image= self.imagen_uno, bg= 'pale turquoise').grid(column= 3, rowspan= 7, row = 0, padx= 50)
        self.aviso_guardado = Label(self.frame_tres, bg= 'white', font=('Comic Sans MS', 15), fg='black')
        self.aviso_guardado.grid(columnspan= 2 , column =0, row = 6, padx= 5)
        
            
    def agregar_datos(self):
        nombre_cuenta=self.nombre_cuenta.get()
        apellido=self.apellido.get()
        nombre1=self.nombre1.get()
        nombre2=self.nombre2.get()
        dni=self.dni.get()
        fecha=self.fecha_nacimiento.get()
        domicilio=self.domicilio.get()
        email=self.email.get()
        telefono=self.telefono.get()
        contrasenia=self.contrasenia.get()
        tipo_usuario=self.id_tipo_usuario.get()
        
        datos = (nombre_cuenta,apellido,nombre1,nombre2,dni,fecha,domicilio,email,telefono,contrasenia,tipo_usuario)
        if  nombre_cuenta and apellido and nombre1 and dni and fecha and domicilio and email and telefono and contrasenia !='':
            self.base_datos.insertar_usuario(datos)
            self.aviso_guardado['text'] = 'Datos Guardados'
            self.limpiar_datos()
            self.aviso_guardado.update()						
            time.sleep(1) 
            self.aviso_guardado['text'] = ''						
        else:
            self.aviso_guardado['text'] = 'Ingrese todos los datos'
            self.aviso_guardado.update()
            time.sleep(1) 
            self.aviso_guardado['text'] = ''
                			
        
    def limpiar_datos(self):
        self.nombre_cuenta.set("")
        self.apellido.set("")
        self.nombre1.set("")
        self.nombre2.set("")
        self.dni.set("")
        self.fecha_nacimiento.set("")
        self.domicilio.set("")
        self.email.set("")
        self.telefono.set("")
        self.contrasenia.set("")
        self.id_tipo_usuario.set("")
        
        
    def buscar_usuario(self):
        nombre_usuario = str(self.nombre_cuenta.get())
        nombre_buscado = self.base_datos.buscar_usuario(nombre_usuario)
        if nombre_buscado == []:
            self.nombre_cuenta['text'] = 'No existe'
            self.nombre_cuenta.update()						
            time.sleep(1) 
            self.nombre_cuenta['text'] =''
        return nombre_buscado
            
    def buscar_contrasenia(self):
        nombre_contra = str(self.contrasenia.get())
        nombre_buscado = self.base_datos.buscar_contrasenia(nombre_contra)
        if nombre_buscado == []:
            self.contrasenia['text'] = 'No existe'
            self.contrasenia.update()						
            time.sleep(1) 
            self.contrasenia['text'] =''
        return nombre_buscado
    def verificar(self):
        user= self.buscar_usuario
        contra=self.buscar_contrasenia
        if user==[] and contra==[]:
            self.contrasenia['text'] = 'Usuario y contraseña no existen'
            self.contrasenia.update()
            self.nombre_cuenta.update()	
            time.sleep(1) 
            self.contrasenia['text'] =''
            self.contrasenia['text'] =''
            self.limpiar_datos
        elif user!=[] and contra!=[]:
            if user[11]==2 and contra==2:
                administrador()
        else:
            self.contrasenia['text'] = 'Usuario o contraseña no existen'
            self.contrasenia.update()
            self.nombre_cuenta.update()	
            self.limpiar_datos
            time.sleep(1) 
            self.contrasenia['text'] =''
            self.contrasenia['text'] =''