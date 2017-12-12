from django import forms
from .models import Campaing
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
		self.fields['fecha'].widget.attrs.update({'class' : 'mi_clase_nombre','placeholder' : 'Fecha'})
		self.fields['lugar'].widget.attrs.update({'class' : 'mi_clase_nombre','placeholder' : 'Lugar'})
		self.fields['tipo'].widget.attrs.update({'class' : 'mi_clase_nombre','placeholder' : 'Tipo'})
		self.fields['monto_valor_operacion'].widget.attrs.update({'class' : 'mi_clase_nombre','placeholder' : 'Valor Intervención'})
		self.fields['monto_inter_grupo_total'].widget.attrs.update({'class' : 'mi_clase_nombre','placeholder' : 'Valores Intervenciones Cubiertas'})
		

	