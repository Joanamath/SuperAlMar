
from usuario import Usuario
class Registro(Usuario):
    def registro():
        try:
            nombreUsuario= input("******* INGRESE SU NOMBRE USUARIO**********")
        # hacemos una consulta en la base de datos para saber si el usuario existe o no
        #si el ususario existe te  va a pedir que ingreses un nuevo usuario
            while(Usuario.consultarUsuario("nombre_usuario",nombreUsuario)==True):
                print("ingrese de nuevo usuario, este usuario ya existe")
                nombreUsuario= input("******* INGRESE SU NOMBRE USUARIO**********") 
            nombre1= input("******* INGRESE SU PRIMER NOMBRE **********")
            nombre2=input("********INGRESE SU SEGUNDO NOMBRE******")
            apellido=input("******* INGRESE SU APELLIDO **********")
            while True:
                try:
                    dni=int(input("******* INGRESE SU DNI **********"))
                    if dni==0:
                        print("DNI es obligatorio")
                        dni=int(input("******* INGRESE SU DNI **********"))
                    break
                except:
                    print("error al ingresar dni")
                    
            print("ingrese fecha de nacimiento= ")
            año=input("año= ")
            mes=input("mes= ")
            dia=input("dia= ")
            fecha=f"{año}-{mes}-{dia}"
            domicilio=input("******* INGRESE SU DOMICILIO **********")
            email=input("******* INGRESE SU EMAIL **********")
        # hacemos una consulta en la base de datos para saber si el email existe o no
        #si el email existe te  va a pedir que ingreses un nuevo email
            while(Usuario.consultarUsuario("email",email)==True):
                print("ingrese de nuevo email, este email ya existe")
                nombreUsuario= input("******* INGRESE SU email**********")
            telefono=input("******* INGRESE SU TELEFONO **********")
            contrasenia=input("******* INGRESE SU CONTRASENIA **********")
            while(contrasenia=="0" or contrasenia==""):
                print("contrasenia es obligatorio")
                contrasenia=input("******* INGRESE SU CONTRASENIA **********")
            tipoUsuario=int(input("""*** Ingrese tipo de Usuario
                                1- Cliente 
                                2- Administrador
                                
                                """))
            while(tipoUsuario>2 or tipoUsuario<1):
                        print("numero invalido")
                        tipoUsuario=int(input("""*** Ingrese tipo de Usuario
                            1- Cliente
                            2- Administrador
                                """))
        except:
            print("error al ingresar los datos")
            
            
        datos=[nombreUsuario,apellido,nombre1,nombre2,dni,fecha,domicilio,email,telefono,contrasenia,tipoUsuario]
        return datos

if __name__ == '__main__':
    Registro.registro()
    
