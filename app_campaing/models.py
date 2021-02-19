from django.db import models

# Create your models here.

class Lugar(models.Model):
	nombre = models.CharField(max_length = 120)
	direccion = models.CharField(max_length = 120)

	def __str__(self):
		return self.nombre

class Colaborador(models.Model):

	nombre = models.CharField(max_length = 30)
	apellido = models.CharField(max_length = 30)
	telefono = models.IntegerField()
	dni = models.IntegerField(unique=True)
	def __str__(self):
		return self.nombre
		return self.apellido

class Barrio(models.Model):
	nombre = models.CharField(max_length = 50)
	detalle = models.CharField(max_length = 120,null=True,default="")

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['nombre']


class Propietario(models.Model):
	nombre = models.CharField(max_length = 50)
	apellido = models.CharField(max_length = 50)
	dni = models.IntegerField()
	telefono = models.IntegerField()	
	barrio = models.ForeignKey(Barrio, related_name="propietario", on_delete=models.PROTECT)
	
	def __str__(self):
		return self.nombre

class Campaing(models.Model):
	TIPO = (("castracion","Castración"),) #solo castraciones
	#TIPO = (("castracion","Castración"),("vacunacion","Vacunación")) #con vacunaciones
	fecha = models.DateField()
	lugar = models.ForeignKey(Lugar, related_name="campaings", on_delete=models.PROTECT)
	colaborador = models.ManyToManyField(Colaborador, through = "CampaingColaborador")
	tipo = models.CharField(max_length = 10, choices = TIPO)	
	monto_valor_operacion = models.IntegerField()
	monto_inter_grupo_gastado = models.IntegerField(default=0)
	monto_inter_grupo_total = models.IntegerField()
	url = models.CharField(max_length = 200)
	preinscripcion = models.BooleanField(default=True)
	habilitada = models.BooleanField(default=True)
	def __str__(self):
		#return self.fecha
		return self.tipo

		
class Animalito(models.Model):
	
	ESPECIE = (("canino","CANINO"),("felino","FELINO"))
	SEXO = (("macho","MACHO"),("hembra","HEMBRA"))

	propietario = models.ForeignKey(Propietario, related_name="animalitos", on_delete=models.PROTECT)
	nombre_mascota = models.CharField(max_length = 30, null=True)
	descripcion = models.CharField(max_length = 50, null=True)
	especie = models.CharField(max_length = 10, choices = ESPECIE)
	sexo = models.CharField(max_length = 10, choices = SEXO)
	nro_pre_inscripcion = models.IntegerField(null=True)
	turno = models.IntegerField(null=True)
	abono = models.IntegerField(null=True)
	campaing = models.ForeignKey(Campaing, related_name = "animalitos", on_delete=models.PROTECT)
	user_name = models.CharField(max_length = 30, null=True, default="")

	def __str__(self):

		return self.nombre_mascota


class CampaingColaborador(models.Model):
	padrino = models.BooleanField()
	ayudante = models.BooleanField()
	campaing = models.ForeignKey(Campaing, on_delete=models.PROTECT)
	colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
		
	class Meta:
		unique_together=("campaing","colaborador")