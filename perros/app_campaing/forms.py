from django import forms
from .models import Campaing, Animalito, Propietario
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
	pass

class BuscarPaciente(forms.Form):

	query = forms.IntegerField(label="Búsqueda")


# class  FormularioInscripcion(forms.Form):
# 	especie = forms.ModelChoiceField(app_campaing.models.Animalito.ESPECIE)
# 	dni = forms.CharField(max_length = 8)
# 	apellido = forms.CharField(max_length = 50)
# 	nombre = forms.CharField(max_length = 50)
# 	telefono = forms.CharField(max_length = 20)
# 	barrio = forms.ModelChoiceField(app_campaing.models.Barrio.objects.all())
# 	nombre_paciente = forms.CharField(max_length = 30)
# 	sexo = forms.ModelChoiceField(app_campaing.models.Animalito.SEXO)
# 	descripcion = forms.CharField(max_length = 50)
# 	turno = forms.IntegerField()
# 	abono = forms.IntegerField()

# 	class Meta:			
# 		labels = {"especie":"Especie",
# 				  "dni":"DNI", 
# 				  "apellido":"Apellido",
# 				  "nombre":"Nombre", 
# 				  "telefono":"Teléfono",
# 				  "barrio":"Barrio",
# 				  "nombre_paciente":"Nombre Mascota",
# 				  "sexo":"Sexo",
# 				  "descripcion":"Observaciones",
# 				  "turno":"Turno","abono":"Abono"}

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
	
	# def __init__(self, *args, **kwargs):
	# 	super(CreateCampaing, self).__init__(*args, **kwargs)
	# 	self.fields['fecha'].widget.attrs.update({'class' : 'mi_clase_fecha','placeholder' : 'Fecha'})
	# 	self.fields['lugar'].widget.attrs.update({'class' : 'mi_clase_lugar','placeholder' : 'Lugar'})


class AnimalitoForm(forms.ModelForm):
	class Meta:
		model = Animalito

		fields = ("especie",				  
				  "nombre",
				  "sexo",
				  "descripcion",
				  "turno",
				  "abono")

		labels = {"especie":"Especie",
				  "nombre":"Nombre Mascota",
				  "sexo":"Sexo",
				  "descripcion":"Observaciones",
				  "turno":"Turno",
				  "abono":"Abono"}

		widget = {"especie":forms.TextInput(), 
				  "nombre":forms.TextInput(),
				  "sexo":forms.Select(), 
				  "descripcion":forms.TextInput(),
				  "turno":forms.TextInput(),
				  "abono":forms.TextInput()}		  

