
import mysql.connector

class Registro_admi():
    def __init__(self):
        self.conexion = mysql.connector.connect(host="localhost", user="root", passwd="root",database="superalmar")
    
    def insertar_producto(self,datos):
    #conexion base de datos
            conn=self.conexion.cursor()
    #ingresamos el sql indicado
            sql="insert into productos (nombre,marca,detalle,vencimiento,stock,precio,id_categoria) values(%s,%s,%s,%s,%s,%s,%s);"
    # insertamos en la DB
            conn.execute(sql,datos)
    # le damos la orden que lo haga
            self.conexion.commit()
            conn.close() 
            
    def mostrar_producto(self):
    # conexion con la DB
        self.conexion = mysql.connector.connect(host="localhost", user="root", passwd="root",database="superalmar")
        conn=self.conexion.cursor()
    #inicia consulta de tabla
        sql="select * from productos"
        conn.execute(sql)
    #Guardamos el resultado de la consulta en una variable
        registro= conn.fetchall()
        return registro
    
    def buscar_productos(self,contra):
        conn=self.conexion.cursor()
    #inicia consulta
        sql=f"select * from productos where id_producto ='{contra}'"
        conn.execute(sql)
    #Guardamos el resultado de la consulta en una variable
        nombreP= conn.fetchall()
        conn.close() 
        return nombreP
    
    def eliminar_productos(self,contra):
        conn=self.conexion.cursor()      
        sql=f"delete from productos where id_producto ='{contra}'"
        conn.execute(sql)
        self.conexion.commit()
        conn.close() 
        
    def actualiza_productos(self,id_producto,nombre,marca,detalle,vencimiento,stock,precio,id_categoria,contra):
        conn=self.conexion.cursor()
        # primero verificamos que existe en la DB para actualizar    
        sql=f"update productos set id_producto='{id_producto}',nombre='{nombre}',marca='{marca}',detalle='{detalle}',vencimiento='{vencimiento}',stock='{stock}',precio='{precio}',id_categoria='{id_categoria}' where id_producto='{contra}'"
        conn.execute(sql)
        actual=conn.rowcount
        self.conexion.commit()
        conn.close() 
        self.conexion.close()
        return actual
    
    