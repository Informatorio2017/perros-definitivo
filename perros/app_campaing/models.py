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
	telefono = models.CharField(max_length = 20)
	dni = models.CharField(max_length = 8)
	def __str__(self):
		return self.nombre
		return self.apellido

class Barrio(models.Model):
	nombre = models.CharField(max_length = 50)
	detalle = models.CharField(max_length = 120,null=True)

	def __str__(self):
		return self.nombre

class Propietario(models.Model):
	nombre = models.CharField(max_length = 50)
	apellido = models.CharField(max_length = 50)
	dni = models.CharField(max_length = 8)
	telefono = models.CharField(max_length = 20)	
	barrio = models.ForeignKey(Barrio, related_name="propietario")
	
	def __str__(self):
		return self.nombre

class Campaing(models.Model):
	TIPO = (("castracion","Castración"),("vacunacion","Vacunación"))
	fecha = models.DateField()
	
	lugar = models.ForeignKey(Lugar, related_name="campaings")
	colaborador = models.ManyToManyField(Colaborador, through = "CampaingColaborador")
	tipo = models.CharField(max_length = 10, choices = TIPO)	
	monto_valor_operacion = models.IntegerField()
	monto_inter_grupo_gastado = models.IntegerField(default=0)
	monto_inter_grupo_total = models.IntegerField()
	url = models.CharField(max_length = 200)
	preinscripcion = models.BooleanField(default=True)
	habilitada = models.BooleanField(default=True)

	#def __str__(self):
		#return self.lugar
		#return "self.fecha"
		#return self.tipo

		
class Animalito(models.Model):
	
	ESPECIE = (("canino","Canino"),("felino","Felino"))
	SEXO = (("macho","Macho"),("hembra","Hembra"))

	propietario = models.ForeignKey(Propietario, related_name="animalitos")
	nombre = models.CharField(max_length = 30)
	descripcion = models.CharField(max_length = 50)
	especie = models.CharField(max_length = 10, choices = ESPECIE)
	sexo = models.CharField(max_length = 10, choices = SEXO)
	nro_pre_inscripcion = models.IntegerField()
	turno = models.IntegerField()
	abono = models.IntegerField()
	campaing = models.ForeignKey(Campaing, related_name = "animalitos")
	user_name = models.CharField(max_length = 30)

	def __str__(self):
		return self.nombre

class CampaingColaborador(models.Model):
	padrino = models.BooleanField()
	ayudante = models.BooleanField()
	campaing = models.ForeignKey(Campaing)
	colaborador = models.ForeignKey(Colaborador)
		
	class Meta:
		unique_together=("campaing","colaborador")



