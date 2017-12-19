from django import forms
from .models import Campaing, Animalito, Propietario, Barrio, Lugar
import app_campaing

class CreateCampaing(forms.ModelForm):
	fecha = forms.DateField()
	lugar = forms.ModelChoiceField(app_campaing.models.Lugar.objects.all())
	tipo = forms.ChoiceField(app_campaing.models.Campaing.TIPO)
	monto_valor_operacion = forms.IntegerField()
	monto_inter_grupo_total = forms.IntegerField()
	
	class Meta:
		model = Campaing
		fields =  ["fecha","lugar", "tipo", "monto_valor_operacion","monto_inter_grupo_total"]
		labels = {"fecha":"Fecha","lugar":"Lugar", "tipo":"Tipo","monto_valor_operacion":"Valor Intervención", "monto_inter_grupo_total":"Valor Intervenciones Cubiertas"}

	def __init__(self, *args, **kwargs):

		super(CreateCampaing, self).__init__(*args, **kwargs)
		#self.fields['nombre'].widget.attrs.update({'class' : 'mi_clase_nombre','placeholder' : 'Nombre'})
		self.fields['fecha'].widget.attrs.update({'class' : 'datepicker','placeholder' : 'Fecha', 'type' : 'text'})
		self.fields['lugar'].widget.attrs.update({'class' : 'mi_clase_nombre','placeholder' : 'Lugar'})
		self.fields['tipo'].widget.attrs.update({'class' : 'mi_clase_nombre','placeholder' : 'Tipo'})
		self.fields['monto_valor_operacion'].widget.attrs.update({'class' : 'mi_clase_nombre','placeholder' : 'Valor Intervención'})
		self.fields['monto_inter_grupo_total'].widget.attrs.update({'class' : 'mi_clase_nombre','placeholder' : 'Valores Intervenciones Cubiertas'})
		


class BuscarPaciente_pre(forms.Form):

	query = forms.IntegerField(label="Búsqueda")


class BuscarPaciente(forms.Form):

	query = forms.IntegerField(label="Búsqueda")



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
				  "nombre_mascota":"Nombre Mascota",
				  "sexo":"Sexo",
				  "descripcion":"Observaciones",
				  "turno":"Turno",
				  "abono":"Abono"}

		widget = {"especie":forms.TextInput(), 
				  "nombre_mascota":forms.TextInput(),
				  "sexo":forms.Select(), 
				  "descripcion":forms.TextInput(),
				  "turno":forms.TextInput(),
				  "abono":forms.TextInput()}		  



class AnimalitoPreinscripcionForm(forms.ModelForm):
	

	class Meta:
		model = Animalito
		fields = ("especie",				  
				  "nombre_mascota",
				  "sexo",
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



class CrearBarrio(forms.ModelForm):
	nombre = forms.CharField()
	detalle = forms.CharField()
	
	class Meta:
		model = Barrio
		fields =  ["nombre", "detalle"]
		labels = {"nombre":"Nombre del Barrio", "detalle":"Descripción"}

	def __init__(self, *args, **kwargs):

		super(CrearBarrio, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs.update({'class' : 'mi_clase_nombre','placeholder' : 'Nombre'})
		self.fields['detalle'].widget.attrs.update({'class' : 'mi_clase_nombre','placeholder' : 'Descripción del Barrio'})
		self.fields['detalle'].required=False

class CrearLugar(forms.ModelForm):
	nombre = forms.CharField()
	direccion = forms.CharField()

	class Meta:
		model = Lugar
		fields = ["nombre","direccion"]
		labels = {"nombre":"Nombre del Lugar", "direccion":"Direccion"}

	def __init__(self, *args, **kwargs):
		super(CrearLugar, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs.update({'class' : 'mi_clase_nombre','placeholder' : 'Nombre del Lugar'})
		self.fields['direccion'].widget.attrs.update({'class' : 'mi_clase_nombre','placeholder' : 'Descripción del Lugar'})