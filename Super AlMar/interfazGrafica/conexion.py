
import mysql.connector
from mysql.connector import Error
class Conexion():
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
    
    def mostrar_ventas(self):
        # conexion con la DB
        self.conexion = mysql.connector.connect(host="localhost", user="root", passwd="root",database="superalmar")
        conn=self.conexion.cursor()
    #inicia consulta de tabla
        sql="select * from ventas"
        conn.execute(sql)
    #Guardamos el resultado de la consulta en una variable
        registro= conn.fetchall()
        return registro
        
    def buscar_usuario(self,usuario):
        try:
    # conexion a la DB
            conexion1=mysql.connector.connect(host="localhost", user="root", passwd="root",database="superalmar")
            conn=conexion1.cursor()
    #inicia consulta
            sql=f"select * from usuario where nombre_usuario ='{usuario}'"
            conn.execute(sql)
    #Guardamos el resultado de la consulta en una variable
            fila= conn.fetchall()
        # ¿? PORQUE CUANDO PONGO NONE IGUAL INGRESA AL IF, SI ESTA VACIO
            if fila!=[]:
                #print(f"*** El {nomb}={contra} existe***")
                return fila
            else:
                #print("*** No exite en la DB***")
                return []
        except Error as e:
                return " *** No se pudo realizar la operación***"
        finally:
            conn.close() 
            conexion1.close()
    
    def nombre_usuario(self,datos):
        nombre =['apellido','nombre1','nombre2','dni','domicilio','email','telefono']
        cadena=f"""
        {nombre[0]}={datos[2]}   {nombre[1]}={datos[3]}   {nombre[2]}={datos[4]} 
        {nombre[3]}={datos[5]}   {nombre[4]}={datos[7]} 
        {nombre[5]}={datos[8]}   {nombre[6]}={datos[9]}"""
        return cadena
        
    def buscar_descuento(self,contra):
        conn=self.conexion.cursor()
    #inicia consulta
        sql=f"select * from descuento where id_descuento ='{contra}'"
        conn.execute(sql)
    #Guardamos el resultado de la consulta en una variable
        nombreP= conn.fetchall()
        conn.close() 
        return nombreP
    
    def buscar_tarjeta(self,contra):
        conn=self.conexion.cursor()
    #inicia consulta
        sql=f"select * from tarjeta where id_tarjeta ='{contra}'"
        conn.execute(sql)
    #Guardamos el resultado de la consulta en una variable
        nombreP= conn.fetchall()
        conn.close() 
        return nombreP
    
    def buscar_contrasenia(self, contra):
        try:
    # conexion a la DB
            conexion1=mysql.connector.connect(host="localhost", user="root", passwd="root",database="superalmar")
            conn=conexion1.cursor()
    #inicia consulta
            sql=f"select * from usuario where  ='{contra}'"
            conn.execute(sql)
    #Guardamos el resultado de la consulta en una variable
            fila= conn.fetchall()
        # ¿? PORQUE CUANDO PONGO NONE IGUAL INGRESA AL IF, SI ESTA VACIO
            if fila!=[]:
                #print(f"*** El {nomb}={contra} existe***")
                return fila
            else:
                #print("*** No exite en la DB***")
                return []
        except Error as e:
                return " *** No se pudo realizar la operación***"
        finally:
            conn.close() 
            conexion1.close()
            
    def insertar_usuario(self,datos):
        try:
    #conexion base de datos
            conexion1=mysql.connector.connect(host="localhost", user="root", passwd="root",database="superalmar")
            conn=conexion1.cursor()
        #ingresamos el sql indicado
            sql="insert into usuario(nombre_cuenta,apellido,nombre1,nombre2,dni,fecha_nacimiento,domicilio,email,telefono,contrasenia,id_tipo_usuario) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
             # insertamos en la DB
            print(sql)
            conn.execute(sql,datos)
    # le damos la orden que lo haga
            conexion1.commit()
            print("*** Usuario se inserto con exito***")
        except Error as e:
            print("*** No se pudo realizar la operación***")
        finally:
            conn.close() 
            conexion1.close()
            