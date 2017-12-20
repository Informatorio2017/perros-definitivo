
#url campaing

from django.conf.urls import url
from . import views

app_name = 'app_campaing'

urlpatterns = [


    #home publica##################
    
	url(r'^home/', views.home, name="home"),
	#Urls Campaña##########33333

	#Crear Campaña###########################
    url(r'^create_campaing/', views.create_campaing, name="create_campaing"),
    #home admin admin campaña
	url(r'^home_admin/', views.home_admin, name="home_admin"),    
	
	#listado campañas
    url(r'^ver_campanas/', views.ver_campanas, name="ver_campanas"),
    #ver campaña
   	#alta paciente / id 
	url(r'^ver_campana/([0-9]+)$', views.ver_campana, name="ver_campana"),


    #ver enlace y codigo qr del enlace
	url(r'^ver_qr/', views.ver_qr, name="ver_qr"),

	#####falta finalizar inscripcion pública campaña confirmar (campaña_id)
	url(r'^close_inscription_campaing/([0-9]+)$', views.cerrar_inscripcion_campaing, name="cerrar_inscripcion_campaing"),
	#####falta finalizar campaña confirmar (campaña_id)
	url(r'^end_campaing/([0-9]+)$', views.fin_campaing, name="fin_campaing"),
    

	#Colaborador################

	#alta colaborador
	###falta alta colaborador (publica)
	#ver lista colaboradores
    url(r'^ver_colaboradores/', views.ver_colaboradores, name="ver_colaboradores"),
    	#falta meter /campaña id

	
	#animalito#############33

	#formulario preinscripcion
	url(r'^pre_inscribirse/', views.pre_inscribirse, name="pre_inscribirse"),
	#preinscrip ok
		#falta (donde te muestre numero preincripcion etc)
	#busqueda de preiscripto, o enlace a inscripcion
	url(r'^inscribir_paciente_pre/', views.inscribir_paciente_pre, name="inscribir_paciente_pre"),
	#formulario inscripcion
		#con datos preinscriptos
	url(r'^formulario_inscripcion_preinscriptos/(?P<id>\d+)/$', views.formulario_inscripcion_preinscriptos, name="formulario_inscripcion_preinscriptos"),
	
		#formulario limpio
	url(r'^formulario_inscripcion/', views.formulario_inscripcion, name="formulario_inscripcion"),
	
	#buscarlo para darlo de alta
	url(r'^buscar_paciente/', views.buscar_paciente, name="buscar_paciente"),
	#alta paciente / id 
	url(r'^alta_paciente/([0-9]+)$', views.alta_paciente, name="alta_paciente"),



	#lugares y barrios #############3

	#crear barrio
	url(r'^crear_barrio/', views.crear_barrio, name="crear_barrio"),
	#crear lugar
	url(r'^crear_lugar/', views.crear_lugar, name="crear_lugar"),
	#FALTa
		#ver lugares
		#ver barrios


	#login###############
		#login
		#logout
		#crear usuarios
		



]
