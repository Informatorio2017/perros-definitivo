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
reg3 = ("LAMADRID","")
reg4 = ("MITRE","")
reg5 = ("JUAN DOMINGO PERON","")
reg6 = ("SARMIENTO","")
reg7 = ("CENTRO","")
reg8 = ("NUEVO","")
reg9 = ("PRIMERO DE MAYO","")
reg10 = ("DON ORIONE","")
reg11 = ("ORO BLANCO","")
reg12 = ("EVITA","")
reg13 = ("LOMA LINDA","")
reg14 = ("MATADERO","")
reg15 = ("TECHO DIGNO","")
reg16 = ("EX CAESA","")
reg17 = ("SAN CARLOS","")
reg18 = ("ARCE","")
reg19 = ("NESTOR KIRCHNER","")
reg20 = ("LA SALADA","")
reg21 = ("ENSANCHE SUR","")
reg22 = ("OBLIGADO","")
reg23 = ("NUEVO VITÓN","")
reg24 = ("JUAN XXIII","")
reg25 = ("LA ESPERANZA","")
reg26 = ("SANTA CATALINA","")
reg27 = ("SANTA ANA","")
reg28 = ("EL PICAFLOR","")
reg29 = ("ENSANCHE NORTE","")
reg30 = ("SAENZ PEÑA","")
reg31 = ("EULOGIO CACERES","")
reg32 = ("SANTA MONICA","")
reg33 = ("134 VIVIENDAS","")
reg34 = ("OBRERO","")
reg35 = ("SANTA TERESITA","")
reg36 = ("NALÁ","")
reg37 = ("NAM QOM","")
reg38 = ("TOBA","")
reg39 = ("RESERVA ESTE","")
reg40 = ("MONSEÑOR DE CARLO","")
reg41 = ("PROGRESO","")
reg42 = ("BANCARIO","")
reg43 = ("MUNICIPAL","")
reg44 = ("ZAFRA","")
reg45 = ("SAN JOSE","")
reg46 = ("MILENIUM","")
reg47 = ("17 DE OCTUBRE","")
reg48 = ("PABLO VI","")
reg49 = ("SAN MARTÍN","")
reg50 = ("ISLA SOLEDAD","")
reg51 = ("CEMENTERIO","")
reg52 = ("PIÑEYRO","")
reg53 = ("PUIGBÓ","")
reg54 = ("MARIANO MORENO","")
reg55 = ("JARDÍN","")
reg56 = ("TIRO FEDERAL","")
reg57 = ("GINES BENITEZ","")
reg58 = ("YAPEYU","")
reg59 = ("RAMSEYER","")
reg60 = ("SANTA ELENA","")
reg61 = ("PUERTA DEL SOL","")
reg62 = ("JOSE RUCCI","")
reg63 = ("PARQUE NORTE","")
reg64 = ("SAGRADO CORAZON","")
reg65 = ("COLON","")
reg66 = ("FIBRALIN","")
reg67 = ("FEDERAL 20 VIVIENDAS","")
reg68 = ("AIPO","")
reg69 = ("SOLIDARIO","")
reg70 = ("4 DE JUNIO","")
reg71 = ("2 DE ABRIL","")
reg72 = ("FONAVI","")
reg73 = ("ALBORADA","")






sql = "INSERT INTO app_campaing_barrio(nombre,detalle) VALUES(?,?)"
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
	consulta.execute(sql,reg25)
	consulta.execute(sql,reg26)
	consulta.execute(sql,reg27)
	consulta.execute(sql,reg28)
	consulta.execute(sql,reg29)
	consulta.execute(sql,reg30)
	consulta.execute(sql,reg31)
	consulta.execute(sql,reg32)
	consulta.execute(sql,reg33)
	consulta.execute(sql,reg34)
	consulta.execute(sql,reg35)
	consulta.execute(sql,reg36)
	consulta.execute(sql,reg37)
	consulta.execute(sql,reg38)
	consulta.execute(sql,reg39)
	consulta.execute(sql,reg40)
	consulta.execute(sql,reg41)
	consulta.execute(sql,reg42)
	consulta.execute(sql,reg43)
	consulta.execute(sql,reg44)
	consulta.execute(sql,reg45)
	consulta.execute(sql,reg46)
	consulta.execute(sql,reg47)
	consulta.execute(sql,reg48)
	consulta.execute(sql,reg49)
	consulta.execute(sql,reg50)
	consulta.execute(sql,reg51)
	consulta.execute(sql,reg52)
	consulta.execute(sql,reg53)
	consulta.execute(sql,reg54)
	consulta.execute(sql,reg55)
	consulta.execute(sql,reg56)
	consulta.execute(sql,reg57)
	consulta.execute(sql,reg58)
	consulta.execute(sql,reg59)
	consulta.execute(sql,reg60)
	consulta.execute(sql,reg61)
	consulta.execute(sql,reg62)
	consulta.execute(sql,reg63)
	consulta.execute(sql,reg64)
	consulta.execute(sql,reg65)
	consulta.execute(sql,reg66)
	consulta.execute(sql,reg67)
	consulta.execute(sql,reg68)
	consulta.execute(sql,reg69)
	consulta.execute(sql,reg70)
	consulta.execute(sql,reg71)
	consulta.execute(sql,reg72)
	consulta.execute(sql,reg73)




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
reg1 = ("ESCUELA 352 VICTORIA WAKS","CALLE 9 e/ 4 y 6 Monseñor de Carlo")


sql = "INSERT INTO app_campaing_lugar(nombre,direccion) VALUES(?,?)"
err = False
try:
	consulta.execute(sql,reg1)

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
reg1 = ('2017-12-16',200,2000,2000,"www.amoalosperros.com/campaing/1",1,"castracion",False,False)


sql = "INSERT INTO app_campaing_campaing(fecha,monto_valor_operacion,monto_inter_grupo_gastado,monto_inter_grupo_total,url,lugar_id,tipo,preinscripcion,habilitada) VALUES(?,?,?,?,?,?,?,?,?)"
err = False

try:
	consulta.execute(sql,reg1)

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
reg1 = ("LORE","VALDEZ",12809233,"4433551",1)
reg2 = ("LORE","GOMEZ",31890123,"4433552",2)
reg3 = ("LORE","PERREN",23123123,"4433553",3)
reg4 = ("IRMA","BANEGA",11333221,"4433554",1)
reg5 = ("MARIANA","KUCIO",16087123,"4433555",2)
reg6 = ("SUSI","ORTEGA",21999144,"4433556",2)
reg7 = ("MARIA","ACOSTA",21999443,"155660",2)
reg8 = ("JUANA","ORTEGA",21999222,"4444556",5)
reg9 = ("FLORENCIA","SORATI",23399123,"4433446",2)
reg10 = ("SUSI","BORECHEVICH",21399123,"44335599",6)
reg11 = ("TANIA","FRENCH",21999433,"4433556",1)
reg12 = ("TANIA ","VALDEZ",21995523,"4433511",2)
reg13 = ("MATIAS","FERNANDEZ",25599123,"403447",2)
reg14 = ("ISABEL","BORDA",21955384,"143898",2)
reg15 = ("ANTONIA","BONFANTI",21999123,"597208",1)
reg16 = ("MARIELA","MALINA",21994423,"369685",6)
reg17 = ("SOLEDAD","GALEANO",21996623,"616150",1)
reg18 = ("MONICA","NAVARRO",21119123,"588208",3)
reg19 = ("LEO","MEDINA",21999144,"597266",1)
reg20 = ("ROCIO","MAIDANA",21999553,"3644583666",1)
reg21 = ("MALENA","MENDOZA",21995523,"462427",1)
reg22 = ("MONICA","ARRIGIN",21977123,"358987",4)
reg23 = ("MONICA","JIMENEZ",21977123,"358987",4)
reg24 = ("LORE","MEDINA",26699188,"588208",5)
reg25 = ("VERONICA","FILOSI",26889188,"599208",2)
reg26 = ("KAREN","ABREGÙ",26699228,"456612",1)
reg27 = ("PAOLA","FARIA",26699554,"306999",3)
reg28 = ("JOSE","DOMBROSKY",26699645,"548127",5)
reg29 = ("KIKI","LOPEZ",26699778,"588211",6)
reg30 = ("KARINA","MOYANO",26623118,"588779",3)
reg31 = ("KIKI","MOLINA",26633778,"587411",6)
reg32 = ("GRISELDA","VERON",26699712,"594511",4)
reg33 = ("LORE","GALA",26699664,"581111",2)
reg34 = ("DANIELA","ZARATTI",22139778,"666411",6)
reg35 = ("CLAUDIO","ADAM",26699462,"367090",1)
reg36 = ("GRISELDA","SANABRIA",26693348,"364480",6)
reg37 = ("SUSI","BENITEZ",26699645,"585411",2)
reg38 = ("ELIANA","GARCIA",26459778,"588211",2)
reg39 = ("MARCELA","MORDCA",25559778,"585551",2)
reg40 = ("MARINA","GONGORA",26621378,"566611",3)
reg41 = ("HERNAN","PINTOS",54699778,"582111",1)
reg42 = ("MARCELA","LOPEZ",24699778,"564211",6)
reg43 = ("LORE","GALARZA",26698578,"564541",5)
reg44 = ("DOLORES","MONZON",36558578,"564888",2)
reg45 = ("PAOLA","VERA",26698578,"609568",4)
reg46 = ("MARIA","LOPEZ",46598578,"732981",2)
reg47 = ("VANESA","AGUILAR",24598578,"702441",2)
reg48 = ("TAMARA","BULBOA",26666548,"136116",1)
reg49 = ("ESTELA","CAMPOS",26695548,"609111",1)
reg50 = ("FANNY","RENAULT",66698578,"331082",2)
reg51 = ("MARIA","MASSON",93698578,"351663",3)
reg52 = ("MONICA","BENITEZ",26696678,"122406",4)
reg53 = ("DANIEL","PICCOLI",26622578,"606225",2)
reg54 = ("MAGDALENA","LEGUIZA",26698212,"3624663309",3)
reg55 = ("MARI","RETAMOZO",26222578,"609555",6)
reg56 = ("JOSEFINA","SILVA",26545578,"504039",2)
reg57 = ("JOSE","OCAMPO",20364261,"609125",1)
reg58 = ("JONATAN ERALDO","VILLORDO",26222546,"580835",4)
reg59 = ("NICOLAS","LUNA",20452578,"730242",6)
reg60 = ("JONATAN","VILLORDO",20255578,"605425",2)
reg61 = ("RUBEN","ROMERO",20288578,"129797",3)
reg62 = ("JUANA","ENCINA",23554478,"609555",6)
reg63 = ("MARILU","ESCOBAR",27544478,"609778",1)
reg64 = ("EVELIN","CABRAL",27666478,"727152",4)
reg65 = ("ANALIA","FIGUEROA",27665478,"401809",2)
reg66 = ("PATRICIA","MUÑOZ",23551278,"506814",3)
reg67 = ("VIRGINIA","GALLUCI",23554124,"204970",1)
reg68 = ("MARIO","OBREGON",20544478,"528198",5)
reg69 = ("ROMINA","SOSA",27554478,"669555",2)
reg70 = ("ANA","PEREZ",23554478,"609512",3)
reg71 = ("ALEJANDRA","SOSA",27554478,"609511",4)
reg72 = ("LORE","HANDEN",23555578,"621155",6)
reg73 = ("REBECA","RAMIREZ",27224478,"656655",4)
reg74 = ("ANGEL","NUÑEZ",20444478,"609655",2)
reg75 = ("ROSANA","FERNANDEZ",27684478,"645722",3)
reg76 = ("MARIA","RIOS",27664478,"457353",1)

sql = "INSERT INTO app_campaing_propietario(nombre,apellido,dni,telefono,barrio_id) VALUES(?,?,?,?,?)"
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
	consulta.execute(sql,reg25)
	consulta.execute(sql,reg26)
	consulta.execute(sql,reg27)
	consulta.execute(sql,reg28)
	consulta.execute(sql,reg29)
	consulta.execute(sql,reg30)
	consulta.execute(sql,reg31)
	consulta.execute(sql,reg32)
	consulta.execute(sql,reg33)
	consulta.execute(sql,reg34)
	consulta.execute(sql,reg35)
	consulta.execute(sql,reg36)
	consulta.execute(sql,reg37)
	consulta.execute(sql,reg38)
	consulta.execute(sql,reg39)
	consulta.execute(sql,reg40)
	consulta.execute(sql,reg41)
	consulta.execute(sql,reg42)
	consulta.execute(sql,reg43)
	consulta.execute(sql,reg44)
	consulta.execute(sql,reg45)
	consulta.execute(sql,reg46)
	consulta.execute(sql,reg47)
	consulta.execute(sql,reg48)
	consulta.execute(sql,reg49)
	consulta.execute(sql,reg50)
	consulta.execute(sql,reg51)
	consulta.execute(sql,reg52)
	consulta.execute(sql,reg53)
	consulta.execute(sql,reg54)
	consulta.execute(sql,reg55)
	consulta.execute(sql,reg56)
	consulta.execute(sql,reg57)
	consulta.execute(sql,reg58)
	consulta.execute(sql,reg59)
	consulta.execute(sql,reg60)
	consulta.execute(sql,reg61)
	consulta.execute(sql,reg62)
	consulta.execute(sql,reg63)
	consulta.execute(sql,reg64)
	consulta.execute(sql,reg65)
	consulta.execute(sql,reg66)
	consulta.execute(sql,reg67)
	consulta.execute(sql,reg68)
	consulta.execute(sql,reg69)
	consulta.execute(sql,reg70)
	consulta.execute(sql,reg71)
	consulta.execute(sql,reg72)
	consulta.execute(sql,reg73)
	consulta.execute(sql,reg74)
	consulta.execute(sql,reg75)
	consulta.execute(sql,reg76)


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
reg1 = ("FIRULAIS","DESCRIPCION","felino","macho",1,1,200,"LORE",1,1)
reg2 = ("PLUTO","DESCRIPCION","felino","macho",2,2,200,"LORE",1,2)
reg3 = ("DONI","DESCRIPCION","felino","macho",3,3,200,"LORE",1,3)
reg4 = ("ASLAN","DESCRIPCION","felino","macho",4,4,200,"IRMA",1,4)
reg5 = ("LAIK","DESCRIPCION","felino","macho",5,5,200,"MARIANA",1,5)
reg6 = ("BENITO","DESCRIPCION","felino","macho",6,6,200,"SUSI",1,6)
reg7 = ("BRUNO","DESCRIPCION","felino","macho",7,1,200,"SUSI",1,6)
reg8 = ("CHANEL","DESCRIPCION","felino","hembra",8,2,200,"MARIA",1,7)
reg9 = ("DONATELO","DESCRIPCION","felino","macho",9,3,200,"JUANA",1,8)
reg10 =("MARYLIN","DESCRIPCION","felino","hembra",10,4,200,"JUANA",1,8)
reg11 = ("LASSIE","DESCRIPCION","felino","hembra",11,5,200,"FLORENCIA",1,9)
reg12 =("LAIKA","DESCRIPCION","felino","hembra",12,6,200,"SUSI",1,10)
reg13 = ("COCO","DESCRIPCION","felino","macho",13,1,200,"TANIA",1,11)
reg14 = ("BRUNO","DESCRIPCION","felino","macho",14,2,200,"TANIA",1,12)
reg15 = ("DANTE","DESCRIPCION","felino","macho",15,3,200,"MATIAS",1,13)
reg16 = ("ATILA","DESCRIPCION","felino","hembra",16,4,200,"ISABEL",1,14)
reg17 = ("DUQUE","DESCRIPCION","felino","macho",17,5,200,"ISABEL",1,14)
reg18 = ("ALEX","DESCRIPCION","felino","macho",18,6,200,"ANTONIA",1,15)
reg19 = ("COPITO","DESCRIPCION","felino","macho",19,1,200,"ANTONIA",1,15)
reg20 = ("LAILA","DESCRIPCION","felino","hembra",20,2,200,"ANTONIA",1,15)
reg21 = ("ANGEL","DESCRIPCION","felino","macho",21,3,200,"MARIELA",1,16)
reg22 =("DIEGO","DESCRIPCION","felino","macho",22,4,200,"SOLEDAD",1,17)
reg23 = ("CAMILO","DESCRIPCION","felino","macho",23,5,200,"MONICA",1,18)
reg24 =("DARWIN","DESCRIPCION","felino","macho",24,6,200,"LEO",1,19)
reg25 =("CHESTER","DESCRIPCION","felino","macho",25,6,200,"ROCIO",1,20)
reg26 =("BLACKY","DESCRIPCION","felino","macho",26,6,200,"MALENA",1,21)
reg27 =("APOLO","DESCRIPCION","felino","macho",27,6,200,"MONICA",1,22)
reg28 =("COCA","DESCRIPCION","felino","hembra",28,6,200,"MONICA",1,23)
reg29 =("APOLO","DESCRIPCION","canino","macho",29,6,200,"LORE",1,24)
reg30 =("DUQUE","DESCRIPCION","canino","macho",30,6,200,"LORE",1,24)
reg31 =("ATILA","DESCRIPCION","canino","hembra",31,6,200,"LORE",1,24)
reg32 =("MIA","DESCRIPCION","canino","hembra",31,6,200,"LORE",1,24)
reg33 =("NINO","DESCRIPCION","canino","macho",33,6,200,"LORE",1,24)
reg34 =("KIRA","DESCRIPCION","canino","hembra",34,6,200,"LORE",1,24)
reg35 =("LUNA","DESCRIPCION","canino","hembra",35,6,200,"LORE",1,24)
reg36 =("FELIX","DESCRIPCION","canino","macho",36,6,200,"LORE",1,24)
reg37 =("PUPI","DESCRIPCION","canino","macho",37,6,200,"LORE",1,24)
reg38 =("TITO","DESCRIPCION","canino","macho",38,6,200,"LORE",1,24)
reg39 =("NINA","DESCRIPCION","canino","hembra",39,6,200,"LORE",1,24)
reg40 =("MISHA","DESCRIPCION","canino","hembra",40,6,200,"VERONICA",1,25)
reg41 =("DARWIN","DESCRIPCION","canino","macho",41,6,200,"KAREN",1,26)
reg42 =("PELUSA","DESCRIPCION","felino","macho",42,6,200,"PAOLA",1,27)
reg43 =("LOLA","DESCRIPCION","canino","hembra",43,6,200,"JOSE",1,28)
reg44 =("PEPE","DESCRIPCION","felino","macho",44,6,200,"KIKI",1,29)
reg45 =("LULU","DESCRIPCION","canino","hembra",45,6,200,"KIKI",1,29)
reg46 =("LUPI","DESCRIPCION","felino","hembra",46,6,200,"KIKI",1,29)
reg47 =("KIWI","DESCRIPCION","felino","macho",47,6,200,"KARINA",1,30)
reg48 =("AGATA","DESCRIPCION","felino","hembra",48,6,200,"KARINA",1,30)
reg49 =("CLEO","DESCRIPCION","felino","hembra",49,6,200,"KIKI",1,31)
reg50 =("YAGO","DESCRIPCION","felino","macho",50,6,200,"KIKI",1,31)
reg51 =("CATALINA","DESCRIPCION","canino","hembra",51,6,200,"GRISELDA",1,32)
reg52 =("CLOE","DESCRIPCION","felino","hembra",52,6,200,"LORE",1,33)
reg53 =("YASU","DESCRIPCION","canino","macho",53,6,200,"DANIELA",1,34)
reg54 =("ATENEA","DESCRIPCION","felino","hembra",54,6,200,"CLAUDIO",1,35)
reg55 =("DINA","DESCRIPCION","felino","hembra",55,6,200,"GRISELDA",1,36)
reg56 =("GALO","DESCRIPCION","canino","macho",56,6,200,"SUSI",1,37)
reg57 =("YEILA","DESCRIPCION","felino","hembra",57,6,200,"ELIANA",1,38)
reg58 =("YAGOT","DESCRIPCION","felino","macho",58,6,200,"MARCELA",1,39)
reg59 =("HANNA","DESCRIPCION","canino","hembra",59,6,200,"MARINA",1,40)
reg60 =("IRIS","DESCRIPCION","canino","hembra",60,6,200,"HERNAN",1,41)
reg61 =("NICK","DESCRIPCION","canino","macho",61,6,200,"MARCELA",1,42)
reg62 =("HEIDI","DESCRIPCION","canino","hembra",62,6,200,"LORE",1,43)
reg63 =("GATUBELA","DESCRIPCION","felino","hembra",63,6,200,"LORE",1,43)
reg64 =("FRIDA","DESCRIPCION","felino","hembra",64,6,200,"LORE",1,43)
reg65 =("EVA","DESCRIPCION","canino","hembra",65,6,200,"LORE",1,43)
reg66 =("RINGO","DESCRIPCION","canino","macho",66,6,200,"LORE",1,43)
reg67 =("YAYO","DESCRIPCION","canino","macho",67,6,200,"LORE",1,43)
reg68 =("EMILIO","DESCRIPCION","felino","macho",68,6,200,"LORE",1,43)
reg69 =("NOA","DESCRIPCION","canino","hembra",69,6,200,"LORE",1,43)
reg70 =("XICO","DESCRIPCION","felino","macho",70,6,200,"DOLORES",1,44)
reg71 =("NICA","DESCRIPCION","canino","hembra",71,6,200,"PAOLA",1,45)
reg72 =("ZIPI","DESCRIPCION","canino","hembra",72,6,200,"PAOLA",1,45)
reg73 =("NICA","DESCRIPCION","canino","hembra",73,6,200,"MARIA",1,46)
reg74 =("LOLA","DESCRIPCION","felino","hembra",74,6,200,"VANESA",1,47)
reg75 =("RITA","DESCRIPCION","felino","hembra",75,6,200,"TAMARA",1,48)
reg76 =("REINA","DESCRIPCION","canino","hembra",76,6,200,"ESTELA",1,49)
reg77 =("QUIRA","DESCRIPCION","canino","hembra",77,6,200,"FANNY",1,50)
reg78 =("PERLA","DESCRIPCION","felino","hembra",78,6,200,"MARIA",1,51)
reg79 =("PEPA","DESCRIPCION","felino","hembra",79,6,200,"MONICA",1,52)
reg80 =("USA","DESCRIPCION","canino","hembra",80,6,200,"DANIEL",1,53)
reg81 =("UMMA","DESCRIPCION","canino","hembra",81,6,200,"MAGDALENA",1,54)
reg82 =("VALENTINA","DESCRIPCION","felino","hembra",82,6,200,"MARI",1,55)
reg83 =("XANA","DESCRIPCION","felino","hembra",83,6,200,"MARI",1,55)
reg84 =("YUNA","DESCRIPCION","canino","hembra",84,6,200,"JOSEFINA",1,56)
reg85 =("YIN","DESCRIPCION","felino","hembra",85,6,200,"JOSE",1,57)
reg86 =("XILUM","DESCRIPCION","canino","macho",86,6,200,"JONATAN",1,58)
reg87 =("VICENTE","DESCRIPCION","canino","macho",87,6,200,"NICOLAS",1,59)
reg88 =("UCHIE","DESCRIPCION","felino","macho",88,6,200,"JONATAN",1,60)
reg89 =("XIRRI","DESCRIPCION","felino","macho",89,6,200,"RUBEN",1,61)
reg90 =("UNAI","DESCRIPCION","canino","macho",90,6,200,"JUANA",1,62)
reg91 =("TITO","DESCRIPCION","felino","macho",91,6,200,"JUANA",1,62)
reg92 =("YAGUI","DESCRIPCION","canino","hembra",92,6,200,"JUANA",1,62)
reg93 =("ZEUS","DESCRIPCION","felino","hembra",93,6,200,"JUANA",1,62)
reg94 =("FIFI","DESCRIPCION","canino","hembra",94,6,200,"JUANA",1,62)
reg95 =("PEPE","DESCRIPCION","canino","macho",95,6,200,"JUANA",1,62)
reg96 =("MIMI","DESCRIPCION","canino","hembra",96,6,200,"JUANA",1,62)
reg97 =("NANA","DESCRIPCION","felino","hembra",97,6,200,"JUANA",1,62)
reg98 =("LOLO","DESCRIPCION","felino","macho",98,6,200,"JUANA",1,62)
reg99 =("SUSI","DESCRIPCION","canino","hembra",99,6,200,"JUANA",1,62)
reg100 =("DARI","DESCRIPCION","felino","macho",100,6,200,"JUANA",1,62)
reg101 =("IGOR","DESCRIPCION","felino","macho",101,6,200,"MARILU",1,63)
reg102 =("NALA","DESCRIPCION","canino","hembra",102,6,200,"EVELIN",1,64)
reg103 =("LARA","DESCRIPCION","felino","hembra",103,6,200,"ANALIA",1,65)
reg104 =("UNAI","DESCRIPCION","canino","macho",104,6,200,"PATRICIA",1,66)
reg105 =("KIARA","DESCRIPCION","canino","hembra",105,6,200,"VIRGINIA",1,67)
reg106 =("ISSIS","DESCRIPCION","canino","hembra",106,6,200,"MARIO",1,68)
reg107 =("JULI","DESCRIPCION","felino","hembra",107,6,200,"ROMINA",1,69)
reg108 =("POLI","DESCRIPCION","canino","macho",108,6,200,"ANA",1,70)
reg109 =("MINA","DESCRIPCION","canino","hembra",109,6,200,"ALEJANDRA",1,71)
reg110 =("PERLITA","DESCRIPCION","felino","hembra",110,6,200,"LORE",1,72)
reg111 =("ONIX","DESCRIPCION","canino","hembra",111,6,200,"REBECA ",1,73)
reg112 =("INDIA","DESCRIPCION","felino","hembra",112,6,200,"ANGEL",1,74)
reg113 =("YUKI","DESCRIPCION","canino","hembra",113,6,200,"ROSANA",1,75)
reg114 =("YANIRA","DESCRIPCION","felino","hembra",114,6,200,"MARIA",1,76)


sql = "INSERT INTO app_campaing_animalito(nombre_mascota,descripcion,especie,sexo,nro_pre_inscripcion,turno,abono,user_name,campaing_id,propietario_id) VALUES(?,?,?,?,?,?,?,?,?,?)"
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
	consulta.execute(sql,reg25)
	consulta.execute(sql,reg26)
	consulta.execute(sql,reg27)
	consulta.execute(sql,reg28)
	consulta.execute(sql,reg29)
	consulta.execute(sql,reg30)
	consulta.execute(sql,reg31)
	consulta.execute(sql,reg32)
	consulta.execute(sql,reg33)
	consulta.execute(sql,reg34)
	consulta.execute(sql,reg35)
	consulta.execute(sql,reg36)
	consulta.execute(sql,reg37)
	consulta.execute(sql,reg38)
	consulta.execute(sql,reg39)
	consulta.execute(sql,reg40)
	consulta.execute(sql,reg41)
	consulta.execute(sql,reg42)
	consulta.execute(sql,reg43)
	consulta.execute(sql,reg44)
	consulta.execute(sql,reg45)
	consulta.execute(sql,reg46)
	consulta.execute(sql,reg47)
	consulta.execute(sql,reg48)
	consulta.execute(sql,reg49)
	consulta.execute(sql,reg50)
	consulta.execute(sql,reg51)
	consulta.execute(sql,reg52)
	consulta.execute(sql,reg53)
	consulta.execute(sql,reg54)
	consulta.execute(sql,reg55)
	consulta.execute(sql,reg56)
	consulta.execute(sql,reg57)
	consulta.execute(sql,reg58)
	consulta.execute(sql,reg59)
	consulta.execute(sql,reg60)
	consulta.execute(sql,reg61)
	consulta.execute(sql,reg61)
	consulta.execute(sql,reg63)
	consulta.execute(sql,reg64)
	consulta.execute(sql,reg65)
	consulta.execute(sql,reg66)
	consulta.execute(sql,reg67)
	consulta.execute(sql,reg68)
	consulta.execute(sql,reg69)
	consulta.execute(sql,reg70)
	consulta.execute(sql,reg71)
	consulta.execute(sql,reg72)
	consulta.execute(sql,reg73)
	consulta.execute(sql,reg74)
	consulta.execute(sql,reg75)
	consulta.execute(sql,reg76)
	consulta.execute(sql,reg77)
	consulta.execute(sql,reg78)
	consulta.execute(sql,reg79)
	consulta.execute(sql,reg80)
	consulta.execute(sql,reg81)
	consulta.execute(sql,reg82)
	consulta.execute(sql,reg83)
	consulta.execute(sql,reg84)
	consulta.execute(sql,reg85)
	consulta.execute(sql,reg86)
	consulta.execute(sql,reg87)
	consulta.execute(sql,reg88)
	consulta.execute(sql,reg89)
	consulta.execute(sql,reg90)
	consulta.execute(sql,reg91)
	consulta.execute(sql,reg92)
	consulta.execute(sql,reg93)
	consulta.execute(sql,reg94)
	consulta.execute(sql,reg95)
	consulta.execute(sql,reg96)
	consulta.execute(sql,reg97)
	consulta.execute(sql,reg98)
	consulta.execute(sql,reg99)
	consulta.execute(sql,reg100)
	consulta.execute(sql,reg101)
	consulta.execute(sql,reg102)
	consulta.execute(sql,reg103)
	consulta.execute(sql,reg104)
	consulta.execute(sql,reg105)
	consulta.execute(sql,reg106)
	consulta.execute(sql,reg107)
	consulta.execute(sql,reg108)
	consulta.execute(sql,reg109)
	consulta.execute(sql,reg110)
	consulta.execute(sql,reg111)
	consulta.execute(sql,reg112)
	consulta.execute(sql,reg113)
	consulta.execute(sql,reg114)


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



