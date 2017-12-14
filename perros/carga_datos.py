import sqlite3

# establecer la concexión  
conexion = sqlite3.connect("db.sqlite3")

# crear un cursor para realizar la consulta
consulta = conexion.cursor()

# crear un cursor para realizar la consulta
consulta = conexion.cursor()
# insertar datos en una tabla BARRIOS
reg1 = ("SAN CAYETANO","")
reg2 = ("BELGRANO","")
reg3 = ("LA MADRID","")
reg4 = ("MITRE","")
reg5 = ("SAN ANTONIO","")
reg6 = ("SAN MARTIN","")

sql = "INSERT INTO app_campaing_barrio(nombre,detalle) VALUES(?,?)"
err = False
try:
	consulta.execute(sql,reg1)
	consulta.execute(sql,reg2)
	consulta.execute(sql,reg3)
	consulta.execute(sql,reg4)
	consulta.execute(sql,reg5)
	consulta.execute(sql,reg6)
except :
	err = True
	conexion.rollback()

if not err:
	conexion.commit()
	print("BARRIOS REGISTRADOS!")
else:
	conexion.rollback()
	print("NO SE PUDIERON REGISTRAR LOS DATOS BARRIO!")


# insertar datos en una tabla LUGARES
reg1 = ("ESCUELA 506","CALLE 10 N 123")
reg2 = ("ESCUELA 31","CALLE 12 E 9")
reg3 = ("ESCUELA 252","CALLE 23 E 86 Y 8")

sql = "INSERT INTO app_campaing_lugar(nombre,direccion) VALUES(?,?)"
err = False
try:
	consulta.execute(sql,reg1)
	consulta.execute(sql,reg2)
	consulta.execute(sql,reg3)
except :
	err = True
	conexion.rollback()

if not err:
	conexion.commit()
	print("LUGARES REGISTRADOS!")
else:
	conexion.rollback()
	print("NO SE PUDIERON REGISTRAR LOS DATOS LUGARES!")


# insertar datos en una tabla CAMPAING
reg1 = ('10/01/2017',150,2000,2000,"www.amoalosperros.com/campaing/1",1,"CASTRACION",False,False)
reg2 = ('10/02/2017',160,3000,3000,"www.amoalosperros.com/campaing/2",4,"CASTRACION",False,False)
reg3 = ('10/03/2017',170,2000,2000,"www.amoalosperros.com/campaing/3",2,"CASTRACION",False,False)
reg4 = ('10/04/2017',180,4000,4000,"www.amoalosperros.com/campaing/4",3,"CASTRACION",False,False)
reg5 = ('10/05/2017',190,3000,3000,"www.amoalosperros.com/campaing/5",1,"CASTRACION",False,False)
reg6 = ('10/06/2017',200,2000,2000,"www.amoalosperros.com/campaing/6",4,"CASTRACION",False,False)

sql = "INSERT INTO app_campaing_campaing(fecha,monto_valor_operacion,monto_inter_grupo_gastado,monto_inter_grupo_total,url,lugar_id,tipo,preinscripcion,habilitada) VALUES(?,?,?,?,?,?,?,?,?)"
err = False

try:
	consulta.execute(sql,reg1)
	consulta.execute(sql,reg2)
	consulta.execute(sql,reg3)
	consulta.execute(sql,reg4)
	consulta.execute(sql,reg5)
	consulta.execute(sql,reg6)
except :
	err = True
	conexion.rollback()

if not err:
	conexion.commit()
	print("CAMPAING REGISTRADOS!")
else:
	conexion.rollback()
	print("NO SE PUDIERON REGISTRAR LOS DATOS CAMPAING!")

# insertar datos en una tabla PROPIETARIOS
reg1 = ("RAMON","VALDEZ",12809233,"4433551",1)
reg2 = ("RAUL","GOMEZ",31890123,"4433552",2)
reg3 = ("ALEJANDRA","PERREN",23123123,"4433553",3)
reg4 = ("MARIA","PEREZ",11333221,"4433554",1)
reg5 = ("LAURA","PEREZ",16087123,"4433555",2)
reg6 = ("MARGARITA","ORTEGA",21999123,"4433556",2)

sql = "INSERT INTO app_campaing_propietario(nombre,apellido,dni,telefono,barrio_id) VALUES(?,?,?,?,?)"
err = False
try:
	consulta.execute(sql,reg1)
	consulta.execute(sql,reg2)
	consulta.execute(sql,reg3)
	consulta.execute(sql,reg4)
	consulta.execute(sql,reg5)
	consulta.execute(sql,reg6)
except :
	err = True
	conexion.rollback()

if not err:
	conexion.commit()
	print("PROPIETARIOS REGISTRADOS!")
else:
	conexion.rollback()
	print("NO SE PUDIERON REGISTRAR LOS DATOS PROPIETARIO!")

# insertar datos en una tabla ANIMALITOS
reg1 = ("PERRITO 1","DESCRIPCION","CANINO","MACHO",1,1,200,"JUAN",1,1)
reg2 = ("PERRITO 2","DESCRIPCION","CANINO","MACHO",2,2,200,"JUAN",1,2)
reg3 = ("PERRITO 3","DESCRIPCION","CANINO","MACHO",3,3,200,"JUAN",1,3)
reg4 = ("PERRITA 4","DESCRIPCION","CANINO","HEMBRA",4,4,200,"JUAN",1,1)
reg5 = ("PERRITA 5","DESCRIPCION","CANINO","HEMBRA",5,5,200,"JUAN",1,2)
reg6 = ("PERRITA 6","DESCRIPCION","CANINO","HEMBRA",6,6,200,"JUAN",1,4)
reg7 = ("GATITO 7","DESCRIPCION","FELINO","MACHO",1,1,200,"JUAN",1,1)
reg8 = ("GATITO 2","DESCRIPCION","FELINO","MACHO",2,2,200,"JUAN",1,5)
reg9 = ("GATITO 3","DESCRIPCION","FELINO","MACHO",3,3,200,"JUAN",1,5)
reg10 =("GATITA 4","DESCRIPCION","FELINO","HEMBRA",4,4,200,"JUAN",1,6)
reg11= ("GATITA 5","DESCRIPCION","FELINO","HEMBRA",5,5,200,"JUAN",1,3)
reg12 =("GATITA 6","DESCRIPCION","FELINO","HEMBRA",6,6,200,"JUAN",1,2)

reg13 = ("PERRITO 1","DESCRIPCION","CANINO","MACHO",1,1,200,"JUAN",2,1)
reg14 = ("PERRITO 2","DESCRIPCION","CANINO","MACHO",2,2,200,"JUAN",2,2)
reg15 = ("PERRITO 3","DESCRIPCION","CANINO","MACHO",3,3,200,"JUAN",2,3)
reg16 = ("PERRITA 4","DESCRIPCION","CANINO","HEMBRA",4,4,200,"JUAN",2,1)
reg17 = ("PERRITA 5","DESCRIPCION","CANINO","HEMBRA",5,5,200,"JUAN",2,2)
reg18 = ("PERRITA 6","DESCRIPCION","CANINO","HEMBRA",6,6,200,"JUAN",2,4)
reg19 = ("GATITO 7","DESCRIPCION","FELINO","MACHO",1,1,200,"JUAN",2,1)
reg20 = ("GATITO 2","DESCRIPCION","FELINO","MACHO",2,2,200,"JUAN",2,5)
reg21 = ("GATITO 3","DESCRIPCION","FELINO","MACHO",3,3,200,"JUAN",2,5)
reg22 =("GATITA 4","DESCRIPCION","FELINO","HEMBRA",4,4,200,"JUAN",2,6)
reg23= ("GATITA 5","DESCRIPCION","FELINO","HEMBRA",5,5,200,"JUAN",2,3)
reg24 =("GATITA 6","DESCRIPCION","FELINO","HEMBRA",6,6,200,"JUAN",2,2)

sql = "INSERT INTO app_campaing_animalito(nombre,descripcion,especie,sexo,nro_pre_inscripcion,turno,abono,user_name,campaing_id,propietario_id) VALUES(?,?,?,?,?,?,?,?,?,?)"
err = False
try:
	consulta.execute(sql,reg1)
	consulta.execute(sql,reg2)
	consulta.execute(sql,reg3)
	consulta.execute(sql,reg4)
	consulta.execute(sql,reg5)
	consulta.execute(sql,reg6)
	consulta.execute(sql,reg7)
	consulta.execute(sql,reg8)
	consulta.execute(sql,reg9)
	consulta.execute(sql,reg10)
	consulta.execute(sql,reg11)
	consulta.execute(sql,reg12)
	consulta.execute(sql,reg13)
	consulta.execute(sql,reg14)
	consulta.execute(sql,reg15)
	consulta.execute(sql,reg16)
	consulta.execute(sql,reg17)
	consulta.execute(sql,reg18)
	consulta.execute(sql,reg19)
	consulta.execute(sql,reg20)
	consulta.execute(sql,reg21)
	consulta.execute(sql,reg22)
	consulta.execute(sql,reg23)
	consulta.execute(sql,reg24)

except :
	err = True
	conexion.rollback()

if not err:
	conexion.commit()
	print("ANIMALITOS REGISTRADOS!")
else:
	conexion.rollback()
	print("NO SE PUDIERON REGISTRAR LOS DATOS ANIMALITOS!")


consulta.close()
conexion.close()



