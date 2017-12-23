from django import forms
from .models import Campaing, Animalito, Propietario, Barrio, Lugar, Colaborador
import app_campaing


class CreateCampaing(forms.ModelForm):
	fecha = forms.DateField()
	lugar = forms.ModelChoiceField(app_campaing.models.Lugar.objects.all())
	
	tipo = forms.ChoiceField(app_campaing.models.Campaing.TIPO)
	monto_valor_operacion = forms.IntegerField(label="Costo de la Intervención")
	monto_inter_grupo_total = forms.IntegerField(label="Dinero disponible para cubrir intervenciones por parte del grupo")
	
	class Meta:
		model = Campaing
		fields =  ["fecha","lugar", "tipo", "monto_valor_operacion","monto_inter_grupo_total"]
		#labels = {"fecha":"Fecha","lugar":"Lugar", "tipo":"Tipo","monto_valor_operacion":"Valor Intervención", "monto_inter_grupo_total":"Valor Intervenciones Cubiertas"}

	def __init__(self, *args, **kwargs):

		super(CreateCampaing, self).__init__(*args, **kwargs)
		#self.fields['nombre'].widget.attrs.update({'class' : 'mi_clase_nombre','placeholder' : 'Nombre'})
		self.fields['fecha'].widget.attrs.update({'class' : 'datepicker','placeholder' : 'Fecha', 'type' : 'text'})
		self.fields['lugar'].widget.attrs.update({'placeholder' : 'Lugar'})
		self.fields['tipo'].widget.attrs.update({'placeholder' : 'Tipo'})
		self.fields['monto_valor_operacion'].widget.attrs.update({'placeholder' : 'Valor Intervención',})
		self.fields['monto_inter_grupo_total'].widget.attrs.update({'placeholder' : 'Dinero Disponible para grupo'})
		

class BuscarPaciente_pre(forms.Form):

	query = forms.IntegerField(label="Ingrese el N° de preinscripción")


class BuscarPaciente(forms.Form):

	query = forms.IntegerField(label="Ingrese el N° de turno")


class ColaboradorForm(forms.Form):
	dni=forms.CharField(max_length=8,label='DNI')
	apellido = forms.CharField(max_length = 30,label='Apellido')
	nombre=forms.CharField(max_length=30,label='Nombre')
	telefono = forms.CharField(max_length = 20,label='Teléfono')	
	padrino = forms.BooleanField(required=False, label='Padrino', widget=forms.CheckboxInput())
	ayudante = forms.BooleanField(required=False, label='Colaborador', widget=forms.CheckboxInput())

class PropietarioForm(forms.ModelForm):
	class Meta:
		model = Propietario
		fields = ("dni", 
				  "apellido",
				  "nombre", 
				  "telefono",
				  "barrio")

		labels = {"dni":"DNI", 
				  "apellido":"Apellido",
				  "nombre":"Nombre", 
				  "telefono":"Teléfono",
				  "barrio":"Barrio"}

		widget = {"dni":forms.TextInput(), 
				  "apellido":forms.TextInput(),
				  "nombre":forms.TextInput(), 
				  "telefono":forms.TextInput(),
				  "barrio":forms.Select()}

	def __init__(self, *args, **kwargs):

		super(ColaboradorForm, self).__init__(*args, **kwargs)
		self.fields['dni'].widget.attrs.update({'type' : 'number'})
		self.fields['telefono'].widget.attrs.update({'type' : 'number'})

	

class AnimalitoForm(forms.ModelForm):
	class Meta:
		model = Animalito
		fields = ("especie",				  
				  "nombre_mascota",
				  "sexo",
				  "descripcion",
				  "turno",
				  "abono")

		labels = {"especie":"Especie",
				  "sexo":"Sexo",
				  "nombre_mascota":"Nombre Mascota",
				  "descripcion":"Observaciones",
				  "turno":"Turno",
				  "abono":"Abono"}

		widget = {"especie":forms.TextInput(), 
				  "nombre_mascota":forms.TextInput(),
				  "sexo":forms.Select(), 
				  "descripcion":forms.TextInput(),
				  "turno":forms.TextInput(),
				  "abono":forms.TextInput()}		  

	def __init__(self, *args, **kwargs):

		super(AnimalitoForm, self).__init__(*args, **kwargs)
		self.fields['descripcion'].required=False



class AnimalitoPreinscripcionForm(forms.ModelForm):
	
	class Meta:
		model = Animalito
		fields = ("especie",				  
				  "sexo",
				  "nombre_mascota",
				  "descripcion")

		labels = {"especie":"Especie",
				  "nombre_mascota":"Nombre Mascota",
				  "sexo":"Sexo",
				  "descripcion":"Observaciones"
				  }

		widget = {"especie":forms.TextInput(), 
				  "nombre_mascota":forms.TextInput(),
				  "sexo":forms.Select(), 
				  "descripcion":forms.TextInput()
				  }	

	def __init__(self, *args, **kwargs):

		super(AnimalitoPreinscripcionForm, self).__init__(*args, **kwargs)
		self.fields['descripcion'].required=False


class CrearBarrio(forms.ModelForm):
	nombre = forms.CharField(label="Nombre del Barrio")
	detalle = forms.CharField(label="Descripción")
	
	class Meta:
		model = Barrio
		fields =  ["nombre", "detalle"]
		#labels = {"nombre":"Nombre del Barrio", "detalle":"Descripción"}

	def __init__(self, *args, **kwargs):

		super(CrearBarrio, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs.update({'placeholder' : 'Nombre'})
		self.fields['detalle'].widget.attrs.update({'placeholder' : 'Descripción del Barrio'})
		self.fields['detalle'].required=False

class CrearLugar(forms.ModelForm):
	nombre = forms.CharField(label="Nombre del lugar")
	direccion = forms.CharField(label="Dirección")

	class Meta:
		model = Lugar
		fields = ["nombre","direccion"]
		#labels = {"nombre":"Nombre del Lugar", "direccion":"Direccion"}

	def __init__(self, *args, **kwargs):
		super(CrearLugar, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs.update({'placeholder' : 'Nombre del Lugar'})
		self.fields['direccion'].widget.attrs.update({'placeholder' : 'Descripción del Lugar'})