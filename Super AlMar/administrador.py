
from locale import Error
from usuario import Usuario
from producto import Producto

class Administrador(Usuario):
# hereda de la clase usuario para iniciar o registrarse
    def iniAdministrador(self):
        print(f"\t**** Bienvenido Administrador {self.apellido} {self.nombre1} ****")
        while True:
            opcion=Administrador.inicio()
            match(opcion):
                case 1:
                #Agregar producto
                    dato=Producto.pedirDatos()
                    #print(producto)
                    Producto.agregarProducto(dato)
                case 2:
                #Eliminar producto
                    Producto.verProductos()
                    id_producto=int(input("Ingrese id del producto= "))
                    Producto.eliminarProducto(id_producto)
                case 3:
                    #Modificar los datos del producto
                    Producto.verProductos()
                    dato1=input("Ingrese el numero id del producto= ")
                    nombre_actualizar=input("Ingrese el nombre de la tabla a actualizar= ")
                    dato_actual= input("Ingrese el dato que quiere actualizar= ")
                    Producto.actualizarProducto(dato1,nombre_actualizar,dato_actual)
                case 4:
                    Usuario.ver_compras()
                    n=int(input("desea ver lascompras de un usuario especifico= 1-si 0-no  "))
                    if n==1:
                        dato=int(input("Ingrese el número de ID del usuario  "))
                        Usuario.ver_compras_espec("id_usuario",dato)
                case 5:
                    print(f"Se cerro la cuenta {self.nombreUsuario}")
                    break
                
    def inicio():
        while True:
            try:
                opcion=int(input("""---->  Ingrese una opcion:    
		1 - Agregar productos
		2 - eliminar productos
		3 - Modificar los datos de los productos
		4- Ver compras realizadas por los usuarios
		5 - Salir
		"""))
                if opcion<1 or opcion>5 :
                    print(" Error al ingresar opcion ")
                    opcion= int(input("""---->  Ingrese una opcion: 
		1 - Agregar productos
		2 - eliminar productos
		3 - Modificar los datos de los productos
		4- Ver compras realizadas
		5 - Salir
	"""))
                
                break
            except Error as e:
                print(" Error al ingresar ")
        return opcion
        
                
if __name__ == '__main__':
    datos=Administrador("","cami","Cruz","Camila","",37602083,"06-08-1993","pje avellaneda","cami236@gmail.com","3875799857","123456",2)
    datos.iniAdministrador()
    pass