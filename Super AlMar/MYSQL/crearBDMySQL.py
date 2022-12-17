
import mysql.connector
from mysql.connector import Error
#para mostrar mensajes
from tkinter import messagebox

def crearDB(nombre):
    try:
        miConexion=mysql.connector.connect(host="localhost", user="root", passwd="root")
        micursor=miConexion.cursor()
        micursor.execute("create database if not exists "+nombre)
        messagebox.showinfo("mensaje",f"la base de datos {nombre} se ha creado correctamente")
        miConexion.close()
        micursor.close()
        print("DB creada")
    except Error as e:
        messagebox.showwarning("Error "," la base de datos no se ha creado correctamente ")
    
def crearTablaDB(nombre):
    try:
        miConexion=mysql.connector.connect(host="localhost", user="root", passwd="root", db="Super")
        micursor=miConexion.cursor()
        micursor.execute(f"create table if not exists {nombre} (id_producto int auto_increment primary key not null unique,nombre text(30) not null, marca text(30), detalle text, vencimiento datetime, stock int, precio double, id_categoria int, foreign key (id_categoria)references categoria(id_categoria));")
        messagebox.showinfo("mensaje",f"la tabla {nombre} se ha creado correctamente")
        miConexion.close()
        micursor.close()
    except:
        messagebox.showwarning("Error "," la tabla no se ha creado correctamente ")

def actualizarDB(tabla,nomb,contra,nombActual,act):
    try:
    #conexion DB
        conexion1=mysql.connector.connect(host="localhost", user="root", passwd="root",database="superalmar")
        conn=conexion1.cursor()
    # primero verificamos que existe en la DB para actualizar    
        sql=f"update {tabla} set {nombActual}='{act}' where {nomb}='{contra}'"
        conn.execute(sql)
        conexion1.commit()
        print("*** Actulizado con exito***")
    except Error as e:
            print(" *** No se pudo realizar la operación***")
    finally:
        conn.close() 
        conexion1.close()

if __name__ == '__main__':
    #crearDB("Super")
    #crearTablaDB("producto")
    pass