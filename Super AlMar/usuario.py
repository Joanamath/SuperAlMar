from datetime import datetime
from conexionMySQL import Conexion

class Usuario:
    def __init__ (self,id_usuario=0,nombreUsuario="",apellido="",nombre1="",nombre2="",dni=0,fecha="",domicilio="",email="",telefono="",contraseña="",tipoUsuario=0):
        self.__id_usuario=id_usuario
        self.__nombreUsuario=nombreUsuario
        self.__nombre1= nombre1
        self.__nombre2= nombre2
        self.__apellido= apellido
        self.__dni= dni
        self.__fecha= fecha
        self.__domicilio= domicilio
        self.__email= email
        self.__telefono= telefono
        self.__contraseña=contraseña
        self.__tipoUsuario=tipoUsuario
        
    @property
    def id_usuario(self):
        return self.__id_usuario
    @id_usuario.setter
    def id_usuario(self,nuevoIdUs):
        self.__id_usuario=nuevoIdUs
    
    @property
    def nombreUsuario(self):
        return self.__nombreUsuario
    @nombreUsuario.setter
    def nombreUsuario(self,nuevoNombreUsuario):
        self.__nombreUsuario=nuevoNombreUsuario
        
    @property
    def nombre1(self):
        return self.__nombre1
    @nombre1.setter
    def nombre1(self,nuevoNombre):
        self.__nombre1=nuevoNombre
    
    @property
    def nombre2(self):
        return self.__nombre2
    @nombre2.setter
    def nombre2(self,nuevoNombre):
        self.__nombre2=nuevoNombre
    
    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self,nuevoApellido):
        self.__apellido=nuevoApellido
        
    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self,nuevoDNI):
        self.__dni=nuevoDNI
        
    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self,nuevoFecha):
        self.__fecha=nuevoFecha
        
    @property
    def domicilio(self):
        return self.__domicilio
    @domicilio.setter
    def domicilio(self,nuevo):
        self.__domicilio=nuevo
        
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,nuevoEmail):
        self.__email=nuevoEmail
        
    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self,nuevoTel):
        self.__telefono=nuevoTel
    
    @property
    def contraseña(self):
        return self.__contraseña
    @contraseña.setter
    def contraseña(self,nuevoContra):
        self.__contraseña=nuevoContra
        
    @property
    def tipoUsuario(self):
        return self.__tipoUsuario
    @tipoUsuario.setter
    def tipoUsuario(self,nuevoTipo):
        self.__tipoUsuario=nuevoTipo
    
    def esMayor(fecha):
        dt=datetime.now() # Fecha y hora actual
        if((fecha-dt)>=18):
            return True
        else:
            return False
# se cosulta en la BD si tal dato1=dato2 existe en la BD si no existe te da Flase y si existe te da True
    def consultarUsuario(dato1,dato2):
        #print(Conexion.consultaDB("Usuario",dato1,dato2))
        if Conexion.consultaDB("usuario",dato1,dato2)==[]:
            return False
        else:
            return True
# me devuelve todos los datos del usuario
    def datosUsuario(dato1,dato2):
        consulta=Conexion.consultaDB("usuario",dato1,dato2)
        if consulta !=[]:
            return consulta
        
# mayormente se lo usa en el registro para   ingresar el usuario a la DB
    def agregaUsuario(datos):
        Conexion.insertarDB("usuario",datos)
        return Usuario.datosUsuario("nombre_usuario",datos[0])
        
# se lo usara cuando el usuario quiera eliminar su cuenta
    def  eliminarUsuario(nombre,dato):
        Conexion.eliminarDB("usuario",nombre,dato)
        
# id y datos 1 se identifica el usuario que quiero modificar
# nombreAct y dato2 es por lo que se quiere mdificar
    def modificarUsuario(id,nombreAct,dato1,dato2):
        Conexion.actualizarDB("usuario",id,dato1,nombreAct,dato2)
#
    def ver_compras():
        consulta=Conexion.vertablasDB("ventas")
        for dato in consulta:
            print(dato)
            
    def ver_compras_espec(dato1,dato2):
        consulta=Conexion.consultaDB("ventas",dato1,dato2)
        if consulta !=[]:
            return consulta
    
    def agregaVentas(datos):
        Conexion.insertarDB("ventas",datos)
        return Usuario.datosUsuario("id_venta",datos[0])
        
    def modificarVentas(nombreAct,dato1,dato2):
        Conexion.actualizarDB("ventas","id_venta",dato1,nombreAct,dato2)
    
    def inserarTarjeta(dato):
        Conexion.insertarDB("tarjeta",dato)
        
    def __str__(self):
        cadena=f"""Nombre Usuario= {self.__nombreUsuario}
            Primer Nombre=  {self.__nombre1}
            Segundo Nombre= {self.__nombre2}
            Apellido=  {self.__apellido}
            dni= "{str(self.__dni)}
            Fecha de Nacimiento= {self.__fecha}
            domicilio= {self.__domicilio}
            email= {self.__email}
            telefono= {self.__telefono}
            contraseña= {self.__contraseña}"""
        if self.__tipoUsuario==1:
            cadena=f"""{cadena}
            Tipo de Usuario= Cliente"""
        elif  self.tipoUsuario==2:
            cadena=f"""{cadena}
            Tipo de Usuario= Administrador"""
        return cadena
    
if __name__ == '__main__':
    print(Usuario.consultarUsuario("nombre_usuario","1253"))
    pass