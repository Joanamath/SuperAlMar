
import datetime
from locale import Error
from usuario import Usuario
from producto import Producto

class Cliente(Usuario):
    
# es el usuario Cliente donde ereda los atributos de usuario y registrarse e iniciar cesion
    
    def iniCliente(self):
# el cliente ingresa a la pagina para realizar compras o ver catalogos de productos
        print(f"**** Bienvenido {self.nombre1} {self.apellido}")
        Cliente.inicio()
        while True:
            opcion=Cliente.inicio()
            match(opcion):
                case 1:
                    Producto.verProductos()
                    eleccion=int(input("Ingrese el número id del producto= "))
                    cantidad=int(input("Ingresar cantidad que quiere comprar"))
                    #asigno lo que retorna datosproducto a dato
                    dato=Producto.datosproducto("id_producto",eleccion)
                    # objeto Producto
                    prod=Producto(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7])
                    cadena=f"({dato},{cantidad})"
                    suma=prod.precio*cantidad
                    while int(input("deseaseguir eligiendo productos= 1-si 0-no "))==1:
                        Producto.verProductos()
                        eleccion=int(input("Ingrese el número id del producto= "))
                        cantidad=int(input("Ingresar cantidad que quiere comprar"))
                        dato=Producto.datosproducto("id_producto",eleccion)
                        prod=Producto(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7])
                        cadena=f"{cadena},({dato},{cantidad})"
                        suma=suma+(prod.precio*cantidad)
                    descuento=int(input("Si tiene algun descuento ingrese el número del descuento=  "))
                    if descuento=="\n":
                        descuento=0
                    fecha= datetime.now.date()
                    hora=datetime.now.time()
                    venta=(fecha,hora,suma,self.id_usuario,descuento,cadena,0,"No")
                    final=Usuario.agregaVentas(venta)
                case 2:
                    ("id_venta","fecha","hora","total","id_usuario","id_descuento","detalle_venta","id_tarjeta","autorizacion")
                    for i  in range[len(final)]:
                        print(f"{cadena[i]}={final[i]}")
                    if int(input(" desea autorizar compra= 1-si 0-no "))==1:
                        num_tarjeta=input("Ingrese el numero de la tarjeta(ej 1234 5678 9101 1213)= ")
                        clave_tarjeta=int(input("Ingrese codigo cvv (ej: 579)= "))
                        vencimiento=input("Ingrese fecha de vencimiento que figura en la tarjeta (ej:202-12 )= ")
                        nombre=input("Ingrese nombre como figura en la tarjeta= ")
                        banco=input("Ingrese nombre del banco o si es efectivo= ")
                        id_tipo_tarjeta=int(input("""tipo de pago
                                                  1-Credito
                                                  2-Debito
                                                  3-Mercado Pago
                                                  4-RapiPago
                                                  5-Pago Express
                                                  """))
                        dato=[num_tarjeta,clave_tarjeta,vencimiento,nombre,self.id_usuario,banco,id_tipo_tarjeta]
                        Usuario.inserarTarjeta(dato)
                        Usuario.modificarVentas(final[0],"autorizacion","si")
                        print("Compra realizada")
                case 3:
                    Usuario.ver_compras_espec("id_usuario",self.id_usuario)
                case 4:
                    nom=input("Ingrese el nombre del dato que quiere modificar(ej: domicilio,nombre,contraseña)= ")
                    modif=input("Valor por el que quiere modificarlo= ")
                    Usuario.modificarUsuario("id_usuario",self.id_usuario,nom,modif)
                case 5:
                    print(f"Se cerro la cuenta {self.nombreUsuario}")
                    break
    
    def inicio():
        # solo muestray retorna la opcion que tiene el cliente
        while True:
            try:
                opcion=int(input("""
                1 - Seleccionar productos
                2 - Ver carrito
                3 - Historial de compras realizadas
                4 - actulizar sus datos 
                5 - Salir 
                """))
                if opcion<1 or opcion>5 :
                    print(" Error al ingresar opcion ")
                    opcion= int(input("""
                1 - Seleccionar productos
                2 - Ver carrito
                3 - Historial de compras realizadas
                4 - actulizar sus datos 
                5 - Salir 
                """))
                
                break
            except Error as e:
                print(" Error al ingresar ")
        return opcion
# 1- primero ver si los productostienen stock para despues mostrarle a los clientes
    # mostrar productos y seleccionar productos con la cantidad a comprar
#2- ver productos seleccionados y dejar que cliente pueda eliminar si no quiere comprar un producto o el stock
    #2a) autorizar compra que el cliente ingrese tarjeta  o el modo de pago, o descuento que tenga,
    # verificar si la tarjeta tiene fondos suficientes pata la compra, autorizar la compra y ver ticket
    #2b) no autorizar compra 
#3- traer de la base de datos todo los id_compras y detalles de las mismas para que el cliente pueda ver todas sus compras realizadas
#4- si el cliente cambio de domicilio u tarjeta pueda actualizar las mismas 
#5-salir de la aplicacion y dejar un mensaje de salida
if __name__ == '__main__':
    datos=Cliente("","cami","Cruz","Camila","",37602083,"06-08-1993","pje avellaneda","cami236@gmail.com","3875799857","123456",1)
    datos.iniCliente()
        
