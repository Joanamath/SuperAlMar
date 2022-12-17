from mysql.connector import Error
import mysql.connector

class Conexion():
    
    def conexion():
        conexion1=mysql.connector.connect(host="localhost", user="root", passwd="root",database="superalmar")
#llamamos a la función connect pasando la ubicación de nuestro servidor que es 'localhost',
# el usuario que por defecto al instalar MySQL se creó el usuario 'root' 
# y la clave de ese usuario "root"
        cursor1=conexion1.cursor()
#a partir del objeto 'conexion1' que es de la clase 'MySQLConnection' llamamos al método 'cursor':
        cursor1.execute("select * from usuario")
# con "select * from producto" podemos ver que contiene la tabla producto
# con "describe producto" me muestrala estructura de la tabla
#con "show tables" te muestra todas las tablas que tiene esa bd
# con "show database" te muestra todo las base de datos
# 'cursor1' llamamos al método execute y le pasamos como parámetro un comando SQL, en este caso 'show databases':
#Mediante un for podemos ver todas las bases de datos existentes en nuestro servidor de MySQL
        for db in cursor1:
          print(db)
       # conexion1.close() 
#Finalmente cerramos la conexión con el servidor de MySQL  
        #print("******conecto a la base de datos ******")
       
#INSERTAR
    def insertarDB(nomb,datos):
        try:
    #conexion base de datos
            conexion1=mysql.connector.connect(host="localhost", user="root", passwd="root",database="superalmar")
            conn=conexion1.cursor()
        #ingresamos el sql indicado
            if nomb=="usuario":
                sql="insert into usuario(nombre_cuenta,apellido,nombre1,nombre2,dni,fecha_nacimiento,domicilio,email,telefono,contrasenia,id_tipo_usuario) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            elif nomb=="productos":
                sql="insert into productos(nombre,marca,detalle,vencimiento,stock,precio,id_categoria) values(%s,%s,%s,%s,%s,%s,%s);"
            elif nomb=="categoria":
                sql="insert into categoria(nombre_categoria) values(%s);"
            elif nomb=="ventas":
                sql="insert into ventas(fecha,hora,total,id_usuario,id_descuento,detalle_venta,id_tarjeta,autorizacion) values(%S,%s,%s,%s,%s,%s,%s,%s);"
            elif nomb=="tarjeta":
                sql="insert into tarjeta(num_tarjeta,clave_tarjeta,vencimiento_tarjeta,nombre_tarjeta,id_usuario,banco,id_tipo_tarjeta) values(%s,%s,%s,%s,%s,%s,%s);"
    # insertamos en la DB
            print(sql)
            print(datos)
            conn.execute(sql,datos)
    # le damos la orden que lo haga
            conexion1.commit()
            print(f"*** {nomb} se inserto con exito***")
        except Error as e:
            print("*** No se pudo realizar la operación***")
        finally:
            conn.close() 
            conexion1.close()
            
# VER TABLA COMPLETA
    def vertablasDB(tabla):
        try:
    # conexion con la DB
            conexion1=mysql.connector.connect(host="localhost", user="root", passwd="root",database="superalmar")
            conn=conexion1.cursor()
    #inicia consulta de tabla
            sql="select * from "+tabla
            conn.execute(sql)
    #Guardamos el resultado de la consulta en una variable
            lista= conn.fetchall()
            print(f"***La tabla {tabla} existe***")
            return lista
        except Error as e:
                print(f"*** {tabla} No exite en la DB***")
                return []
        finally:
            conn.close() 
            conexion1.close()
            
# HACER CONSULTAS EN LA DB

    def consultaDB(tabla,nomb,contra):
        try:
    # conexion a la DB
            conexion1=mysql.connector.connect(host="localhost", user="root", passwd="root",database="superalmar")
            conn=conexion1.cursor()
    #inicia consulta
            sql=f"select * from {tabla} where {nomb}='{contra}'"
            conn.execute(sql)
    #Guardamos el resultado de la consulta en una variable
            fila= conn.fetchall()
        # ¿? PORQUE CUANDO PONGO NONE IGUAL INGRESA AL IF, SI ESTA VACIO
            if fila!=[]:
                #print(f"*** El {nomb}={contra} existe***")
                return fila[0]
            else:
                #print("*** No exite en la DB***")
                return []
        except Error as e:
                return " *** No se pudo realizar la operación***"
        finally:
            conn.close() 
            conexion1.close()
            
#ACTUALIZAR DATOS 
    def actualizarDB(tabla,nomb,contra,nombActual,act):
        try:
        #conexion DB
            conexion1=mysql.connector.connect(host="localhost", user="root", passwd="root",database="superalmar")
            conn=conexion1.cursor()
        # primero verificamos que existe en la DB para actualizar    
            if(Conexion.consultaDB(tabla,nomb,contra)!=[]):
                sql=f"update {tabla} set {nombActual}='{act}' where {nomb}='{contra}'"
                conn.execute(sql)
                conexion1.commit()
                print("*** Actulizado con exito***")
                print(Conexion.consultaDB(tabla,nomb,contra))
            
        except Error as e:
                print(" *** No se pudo realizar la operación***")
        finally:
            conn.close() 
            conexion1.close()
        
#ELIMINAR DATOS
    def eliminarDB(tabla,nomb,contra):
        try:
            conexion1=mysql.connector.connect(host="localhost", user="root", passwd="root",database="superalmar")
            conn=conexion1.cursor()      
            if Conexion.consultaDB(tabla,nomb,contra)!=[]: 
                sql1=f"delete from {tabla} where {nomb}='{contra}'"
                conn.execute(sql1)
                conexion1.commit()
                print(f"{tabla} con {nomb}={contra} eliminado")   
        except Error as e:
                print(" *** No se pudo realizar la operación***")
        finally:
            conn.close() 
            conexion1.close()
            
    def eliminarTablaDB(tabla):
        try:
            conexion1=mysql.connector.connect(host="localhost", user="root", passwd="root",database="superalmar")
            conn=conexion1.cursor()   
            if Conexion.vertablasDB(tabla)!=False:     
                sql1="delete from "+tabla
                conn.execute(sql1)
                conexion1.commit()
                print(f"*** Tabla {tabla} eliminado***")   
        except Error as e:
                print(" *** No se pudo realizar la operación***")
        finally:
            conn.close()   
            conexion1.close()  
            #hola
if __name__ == '__main__':
    #Conexion.conexion()
    #Conexion.vercategorias()
    #print(Conexion.vertablasDB("detalleventa"))
    #print(Conexion.vertablasDB("maximo"))
    datos=("caramelo","1/2 Hora","sabor Anetol","2025-12-05",'20','10','3')
    Conexion.insertarDB("productos",datos)
    #print(Conexion.datosUsuarios())
    #dato=("joa","Peralta","Joana","37602083","1993-08-06","Barrio siglo21","joana@gmail.com",387579987,"JoanaM236",2,True)
    #Conexion.insertar("usuario",dato)
    #Conexion.eliminarUsuario("id_usuario","7")
    #Conexion.existeProducto("id_producto","69")
    #Conexion.eliminarDB("producto","id_producto","138")
    #Conexion.actualizarDB("producto","id_producto","135","marca","Bermejo")
    #Conexion.actualUsuario("id_usuario","6","telefono","387542568")
    #Conexion.actualCat("id_categoria","7","nombre_categoria","Carniceria")
    #print(Conexion.consultaDB("usuario","nombre_usuario","cruzCam"))
    pass