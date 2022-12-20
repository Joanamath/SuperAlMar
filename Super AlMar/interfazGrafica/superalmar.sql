-- Active: 1668573477301@@127.0.0.1@3306@superalmar
SHOW TABLES;
SELECT * FROM `productos`;
SELECT * FROM `categoria`;
SELECT * FROM `usuario`;
SELECT * FROM `tipo_usuario`;
SELECT * FROM `tipo_descuento`;
SELECT * FROM `ventas`;
SELECT * FROM `tarjeta`;
SELECT * FROM `tipo_tarjeta`;
#eliminar columnas de una tabla:
ALTER TABLE `usuario` DROP COLUMN tiene_tarjeta;
#Eliminar varias columnas de la tabla:
ALTER TABLE nombre_tabla DROP COLUMN nombre_columna, DROP COLUMN nombre_columna2;
#renombrar y/o cambiar el nombre la tabla:
ALTER TABLE producto RENAME Productos;
SELECT * FROM `productos`;
#Eliminar clave primaria
ALTER TABLE nombre_tabla DROP PRIMARY KEY;
#Eliminar clave externa
ALTER TABLE nombre_tabla DROP FOREIGN KEY nombre_columna;
#insertar una nueva columna al final de la tabla:
ALTER TABLE tipo_descuento ADD  cantidad_descuento int ;
#Añadir una nueva columna después de otra:
ALTER TABLE ventas ADD hora VARCHAR(20) AFTER fecha ;
#Añadir una nueva columna en la primera posición de la tabla:
ALTER TABLE ventas ADD FOREIGN KEY (id_tarjeta) REFERENCES tarjeta(id_tarjeta);
#Añadir un indice a una columna y eliminar un íncide:
ALTER TABLE nombre_tabla ADD INDEX (nombre_columna) ;
ALTER TABLE nombre_tabla DROP INDEX nombre_indice;
#Asignar como clave primaria a una columna:
ALTER TABLE nombre_Tabla ADD PRIMARY KEY(nombre_columna);
#Cambiar el nombre o renombrar una columna:
ALTER TABLE usuario CHANGE nombre nombre_Primario;
#Cambiar el nombre y tipo de dato de una columna:
ALTER TABLE ventas CHANGE id_descuento id_descuento INT  ;
#cambiar el tipo de dato de una columna:
ALTER TABLE ventas MODIFY fecha VARCHAR(20) ;

#eliminar TABLESPACE
DROP TABLE tipo_usuario

alter table ventas add id_venta varchar not null ;

ALTER TABLE `ventas` DROP  id_descuento ;

ALTER TABLE ventas DROP constraint id_descuento ;

ALTER TABLE ventas DROP foreign key id_descuento ;

insert table tipo_descuento ();

insert into ventas (id_venta,fecha,total,id_usuario,id_descuento,detalle_venta) values ('230010','2022-11-26','6342.20','11','230010','(4,"fideo dedalito","maroli","500grs","2023-05-25",117.50,1,4), (11,"fideo Spaghetti","favorita","500grs","2024-12-03",119.10,1,2), (14,"fideo tirabuzon","favorita","500grs","2022-08-02",115.50,1,2), (115,"bola de lomo","bermejo","xkg","2022-11-23",1080.60,7,5)');

SELECT * FROM `ventas` WHERE `fecha` = '26-11-22' AND  `total` = 6342.20 AND  `id_usuario` = 11 AND  `id_venta` = 230010 AND  `detalle_venta` like '(4,"fideo dedalito","maroli","500grs","2023-05-25",117.50,1,4), (11,"fideo Spaghetti","favorita","500grs","2024-12-03",119.10,1,2), (14,"fideo tirabuzon","favorita","500grs","2022-08-02",115.50,1,2), (115,"bola de lomo","bermejo","xkg","2022-11-23",1080.60,7,5)' AND  `id_descuento` = 000011 ;

insert into tipo_descuento (`id_descuento`,`nombre_descuento`,`cantidad_descuento` ) values (230015,"promocion",8 ) ;

CREATE TABLE tarjeta (
    id_tarjeta INTEGER AUTO_INCREMENT PRIMARY KEY,
    num_tarjeta BIGINT,
    clave_tarjeta INTEGER,
    vencimiento_tarjeta VARCHAR(20),
    nombre_tarjeta VARCHAR(50),
    id_usuario int,
    FOREIGN KEY (id_usuario) 
    REFERENCES usuario(id_usuario)
    );
CREATE TABLE tipo_tarjeta (
    id_tipo_tarjeta INTEGER AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20)
    );

insert into tipo_tarjeta(`nombre`) values ("") ;
insert into tarjeta(num_tarjeta,clave_tarjeta,vencimiento_tarjeta,nombre_tarjeta,id_usuario,banco,id_tipo_tarjeta) values(0,0," "," ",'1'," ",1);
update `tipo_descuento` set id_descuento='15824' where id_descuento='230010';
update `ventas` set `id_venta`='1582401' where `id_venta`='15824';
insert into ventas(fecha,hora,total,id_usuario,id_descuento,detalle_venta,id_tarjeta,autorizacion) values("2022-30-11","15:00",0,1,230010,"",1,"no");
