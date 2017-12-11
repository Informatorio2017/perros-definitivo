from django import forms
from .models import Campaing






class CreateCampaing(forms.ModelForm):

	

	fecha = forms.DateField()
	
	lugar = forms.CharField()
	
	tipo = forms.CharField()

	monto_valor_operacion = forms.IntegerField()
	
	monto_inter_grupo_total = forms.IntegerField()
	
	class Meta:
		model = Campaing
		fields =  ("fecha","lugar", "tipo", "monto_valor_operacion","monto_inter_grupo_total")
		labels = {"fecha":"Fecha","lugar":"Lugar", "tipo":"Tipo","monto_valor_operacion":"Valor Intervención", "monto_inter_grupo_total":"Valor Intervenciones Cubiertas"}

	def __init__(self, *args, **kwargs):

		super(CreateCampaing, self).__init__(*args, **kwargs)
		#self.fields['nombre'].widget.attrs.update({'class' : 'mi_clase_nombre','placeholder' : 'Nombre'})
		self.fields['lugar'].widget.attrs.update({'class' : 'mi_clase_nombre','placeholder' : 'Lugar'})
		