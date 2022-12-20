from registro import Registro
from usuario import Usuario
from administrador import Administrador
from cliente import Cliente
while True:
    try:
        opcion=int(input("""\n\t<<<<< BIENVENIDOS A SUPER ALMAR >>>>>
                    *** Ingrese una opcion ***
                    1- INGRESAR
                    2- REGISTRARSE
                    """))
        while opcion<1 or opcion>2:
                    opcion=int(input("""\n\t<<<<< BIENVENIDOS A SUPER ALMAR >>>>>
                    *** Ingrese una opcion ***
                    1- INGRESAR
                    2- REGISTRARSE
                    """))
        break
    except:
        print(" Erro al ingresar opción ")
            
match(opcion):
    case 1:
        usuario=input("ingrese nombre de usuario= ")
        contrasenia=input("ingrese contraseña= ")
        if Usuario.consultarUsuario("nombre_usuario",usuario)==True:
            datos=Usuario.datosUsuario("nombre_usuario",usuario)
            persona=Usuario(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],datos[9],datos[10],datos[11])
            if persona.tipoUsuario==1:
                persona1=Cliente(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],datos[9],datos[10],datos[11])
                persona1.iniCliente()
            else:
                persona2=Administrador(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],datos[9],datos[10],datos[11])
                persona2.iniAdministrador()
        else:
            print("El Usuario o Contraseña ingresada es invalido")
    case 2:
        datos= Registro.registro()
        datos=Usuario.agregaUsuario(datos)
        print("Se gano un descuento por Registrarse (15% en su primera compra) el número de descuento es 230010 ")
        persona=Usuario(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],datos[9],datos[10],datos[11])
        if(persona.tipoUsuario==1):
            persona1=Cliente(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],datos[9],datos[10],datos[11])
            persona1.iniCliente()
        elif persona.tipoUsuario==2:
            persona2=Administrador(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],datos[9],datos[10],datos[11])
            persona2.iniAdministrador()