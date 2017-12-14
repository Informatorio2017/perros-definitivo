from django.contrib import admin
from .models import Lugar
from .models import Campaing
from .models import Animalito
from .models import Propietario
from .models import Barrio


# Register your models here.


admin.site.register(Lugar)
admin.site.register(Campaing)
admin.site.register(Animalito)
admin.site.register(Propietario)
admin.site.register(Barrio)
