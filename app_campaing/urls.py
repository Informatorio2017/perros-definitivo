from django.urls import re_path
from . import views

app_name = 'app_campaing'

urlpatterns = [
    re_path(r'^create_user/', views.create_user, name="create_user"),

    #Crear Campaña###########################
    re_path(r'^create_campaing/', views.create_campaing, name="create_campaing"),
    #home admin admin campaña
    re_path(r'^home_admin/', views.home_admin, name="home_admin"),

    #listado campañas
    re_path(r'^ver_campanas/', views.ver_campanas, name="ver_campanas"),
    #ver campaña
       #alta paciente / id
    re_path(r'^ver_campana/([0-9]+)$', views.ver_campana, name="ver_campana"),


    #ver enlace y codigo qr del enlace
    re_path(r'^ver_qr/', views.ver_qr, name="ver_qr"),

    #####falta finalizar inscripcion pública campaña confirmar (campaña_id)
    re_path(r'^close_inscription_campaing/([0-9]+)$', views.cerrar_inscripcion_campaing, name="cerrar_inscripcion_campaing"),
    re_path(r'^confirmar_cierre_preinscipcion/([0-9]+)$', views.confirmar_cierre_preinscipcion, name="confirmar_cierre_preinscipcion"),
    #####falta finalizar campaña confirmar (campaña_id)
    re_path(r'^end_campaing/([0-9]+)$', views.fin_campaing, name="fin_campaing"),

    re_path(r'^confirmar_cierre_campania/([0-9]+)$', views.confirmar_cierre_campania, name="confirmar_cierre_campania"),

    re_path(r'^url_inexistente/', views.url_inexistente, name="url_inexistente"),

    #Colaborador################

    #alta colaborador
    ###falta alta colaborador (publica)
    #ver lista colaboradores de una campaña
    re_path(r'^ver_colaboradores/([0-9]+)$', views.ver_colaboradores, name="ver_colaboradores"),
        #falta meter /campaña id

    #animalito#############33

    #formulario preinscripcion
    re_path(r'^pre_inscribirse/(?P<id>\d+)/$', views.pre_inscribirse, name="pre_inscribirse"),
    #preinscrip ok
        #falta (donde te muestre numero preincripcion etc)
    #busqueda de preiscripto, o enlace a inscripcion
    re_path(r'^inscribir_paciente_pre/', views.inscribir_paciente_pre, name="inscribir_paciente_pre"),
    #formulario inscripcion
        #con datos preinscriptos
    re_path(r'^formulario_inscripcion_preinscriptos/(?P<id>\d+)/$', views.formulario_inscripcion_preinscriptos, name="formulario_inscripcion_preinscriptos"),

        #formulario limpio
    re_path(r'^formulario_inscripcion/', views.formulario_inscripcion, name="formulario_inscripcion"),

    #buscarlo para darlo de alta
    re_path(r'^buscar_paciente/', views.buscar_paciente, name="buscar_paciente"),
    re_path(r'^listado_preinscriptos/', views.listado_preinscriptos, name="listado_preinscriptos"),
    re_path(r'^listado_inscriptos/', views.listado_inscriptos, name="listado_inscriptos"),
    #alta paciente / id
    re_path(r'^alta_paciente/([0-9]+)$', views.alta_paciente, name="alta_paciente"),

    re_path(r'^inscripto_turno/([0-9]+)$', views.inscripto_turno, name="inscripto_turno"),

    #lugares y barrios #############3

    #crear barrio
    re_path(r'^crear_barrio/', views.crear_barrio, name="crear_barrio"),
    #crear lugar
    re_path(r'^crear_lugar/', views.crear_lugar, name="crear_lugar"),
    #FALTa
        #ver lugares
        #ver barrios

    #crear usuarios
    re_path(r'^about_campaing/(?P<id>\d+)/$', views.about_campaing, name="about_campaing"),

    re_path(r'^pre_inscripto_turno/(?P<id>\d+)/$', views.pre_inscripto_turno, name="pre_inscripto_turno"),

    re_path(r'^reporte_personas_pdf/$',views.ReportePersonasPDF.as_view(), name="reporte_personas_pdf"),
    re_path(r'^reporte_personas_pdf2/$',views.ReportePersonasPDF2.as_view(), name="reporte_personas_pdf2"),

    re_path(r'^colaborador_inscripto/(?P<id>\d+)/$', views.colaborador_inscripto, name="colaborador_inscripto"),
]
