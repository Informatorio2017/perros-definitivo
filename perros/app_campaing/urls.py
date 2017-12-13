
#url campaing

from django.conf.urls import url
from . import views

urlpatterns = [

  

    url(r'^create_campaing/', views.create_campaing, name="create_campaing"),
    url(r'^creado/', views.creado, name="creado"),


    #home campaing
	url(r'^home/', views.home, name="home"),

	#
	url(r'^buscar_paciente/', views.buscar_paciente, name="buscar_paciente"),
	
	url(r'^home/', views.home, name="home"),
	url(r'^home/', views.home, name="home"),
	url(r'^home/', views.home, name="home"),
	url(r'^home/', views.home, name="home"),
   




]
