from conexionMySQL import Conexion

class Producto(Conexion):
    
    def __init__(self,idProducto=0,nombre="",marca="",detalle="",vencimiento="",stock=0,precio=0.0,id_categoria=0):
        self.__idProducto=idProducto
        self.__nombre=nombre
        self.__marca=marca
        self.__detalle=detalle
        self.__vencimiento=vencimiento
        self.__stock=stock
        self.__precio=precio
        self.__id_categoria=id_categoria
    
    @property
    def idProducto(self):
        return self.__idProducto
    @idProducto.setter
    def idProducto(self,nuevoID):
        self.__idProducto=nuevoID

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nuevoNombre):
        self.__nombre=nuevoNombre
        
    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self,nuevoMarca):
        self.__marca=nuevoMarca
          
    @property
    def detalle(self):
        return self.__detalle
    @detalle.setter
    def detalle(self,nuevoDetalle):
        self.__detalle=nuevoDetalle
        
    @property
    def vencimiento(self):
        return self.__vencimiento
    @vencimiento.setter
    def vencimiento(self,nuevoVenc):
        self.__vencimiento=nuevoVenc
        
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self,nuevoStock):
        self.__stock=nuevoStock
        
    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self,nuevoPrecio):
        self.__precio=nuevoPrecio
        
    @property
    def id_categoria(self):
        return self.__id_categoria
    @id_categoria.setter
    def id_categoria(self,nuevoIdCategoria):
        self.__id_categoria=nuevoIdCategoria


# comienza las funciones que realizan con producto
    def verProductos():
        lista=Conexion.vertablasDB("productos")
        for db in lista:
            print(db)
            
    def consultarProducto(dato1,dato2):
    #print(Conexion.consultaDB("producto",dato1,dato2))
        if Conexion.consultaDB("productos",dato1,dato2)!=[]:
            return True
        else:
            return False
        
    # me devuelve todos los datos del producto
    def datosproducto(dato1,dato2):
        consulta=Conexion.consultaDB(dato1,dato2)
        if consulta !=[]:
            return consulta
        
    def agregarProducto(datos):
        Conexion.insertarDB("productos", datos)
        
    def eliminarProducto(id_producto):
        Conexion.eliminarDB("productos","id_producto",id_producto)
        
    def actualizarProducto(dato1,nombre_actualizar,dato_actual):
        Conexion.actualizarDB("productos","id_producto",dato1,nombre_actualizar,dato_actual)
    
    def pedirDatos():
        try:
            id_categoria=int(input("""Ingrese categoria del producto= 
                                1-Mercaderias
                                2-Bedidas
                                3-Dulces
                                4-Lacteos
                                5-Limpieza
                                6-Bazar
                                7-Carniceria
                                """))        
            nombre=input("Ingrese nombre del producto= ")
            marca=input("Ingrese la marca del producto= ")
            detalle=input("Ingrese detalle del producto(litros, kg)= ")
            vencimiento=input("Ingrese  la fecha de vencimiento= ")
            stock=int(input("Ingrese el stock del producto= "))
            precio=float(input("Ingrese el precio del producto= "))
            datos=(nombre,marca,detalle,vencimiento,stock,precio,id_categoria)
            return datos
        except:
            print("Error al ingresar datos")
            
    def __str__(self):
        cadena=f"""Nombre Producto= {self.__nombre}
            Marca=  {self.__marca}
            Detalles= "{str(self.__detalle)}
            Fecha de Vencimiento= {self.__vencimiento}
            Stock= {str(self.__stock)}
            Precio= {str(self.__precio)}"""
        match self.__id_categoria:
            case 1:
                cadena=f"""{cadena}
                Tipo de Categoria= Mercaderia"""
            case 2:
                cadena=f"""{cadena}
                Tipo de Categoria= Bedidas"""
            case 3:
                cadena=f"""{cadena}
                Tipo de Categoria= Dulces"""
            case 4:
                cadena=f"""{cadena}
                Tipo de Categoria= Lacteos"""
            case 5:
                cadena=f"""{cadena}
                Tipo de Categoria= Limpieza"""
            case 6:
                cadena=f"""{cadena}
                Tipo de Categoria= Bazar"""
            case 7:
                cadena=f"""{cadena}
                Tipo de Categoria= Carniceria"""
        return cadena
       
if __name__ == '__main__':
    
    #Producto.verProductos()
    #datos=Producto.pedirDatos()
    #Producto.agregarProducto(datos)
    datos=("Cubiertos","AlMar","3 unidades  tenedor cuchara cuchillo","2025-11-01",225,230.0,6)
    Producto.agregarProducto(datos)
    pass