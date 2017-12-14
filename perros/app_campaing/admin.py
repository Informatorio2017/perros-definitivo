from django.contrib import admin
from .models import Lugar
from .models import Campaing
from .models import Colaborador



# Register your models here. Aca se cargar los elemntos que semuestran en el admin


admin.site.register(Lugar)
admin.site.register(Campaing)
admin.site.register(Colaborador)  