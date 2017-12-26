from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import Http404
from .forms import AnimalitoForm, PropietarioForm, AnimalitoPreinscripcionForm
from .forms import CreateCampaing, BuscarPaciente_pre, BuscarPaciente, CrearBarrio, CrearLugar, ColaboradorForm
from .models import Campaing, Animalito, Propietario, Barrio, Lugar
from .models import Colaborador, CampaingColaborador
#-------------------------------------------------------
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from django.http import HttpResponse

from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from django.contrib.auth.decorators import login_required

#-------------------------------------------------------


@login_required(login_url='login')
def cerrar_inscripcion_campaing(request,id):
    # import ipdb; ipdb.set_trace()                
    if request.session['num'] != int(id):
        return redirect('/campaing/url_inexistente/')

    campaing = Campaing.objects.get(id=id)
    
    template = 'confirmar_fin_inscrip.html'
    contexto = {"campaing":campaing,}
    return render(request,template,contexto)

@login_required(login_url='login')
def confirmar_cierre_preinscipcion(request,id):

    campaing = Campaing.objects.get(id=id)
    campaing.preinscripcion = False
    campaing.save()
    return redirect('/campaing/home_admin/')

@login_required(login_url='login')
def url_inexistente(request):
    return render(request,'url_inexistente.html',{})

@login_required(login_url='login')
def fin_campaing(request,id):
    campaing = Campaing.objects.get(id=id)
    
    template = 'confirmar_fin_campana.html'
    contexto = {
    "campaing":campaing,
    }
    return render(request,template,contexto)

@login_required(login_url='login')
def confirmar_cierre_campania(request,id):
    campaing = Campaing.objects.get(id=id)
    campaing.habilitada = False
    campaing.save()
    return redirect('/campaing/home_admin/')


#se va esta view
def creado(request):
    return render(request, 'creado.html', {})

#
def ver_campanas(request):

    return render(request, 'ver_campanas.html', {'campanas':Campaing.objects.all().exclude(habilitada=True)})

def ver_campana(request,id):
    try:
        campana= Campaing.objects.get(pk=id)
    except Campaing.DoesNotExist:
        raise Http404("No se encontro la mascota")

    campanias = Campaing.objects.filter(habilitada=True)
    #campanias = Campaing.objects.get(id=1)#(habilitada=True)
    #campaing = Campaing()

    animales_en_campana = Animalito.objects.filter(campaing=campana.id)

    preinscriptos = animales_en_campana.filter(turno=None)
    inscriptos = animales_en_campana.exclude(turno=None)


    c_inscriptos = inscriptos.count()
    c_preinscriptos = preinscriptos.count()
    
    perros = inscriptos.filter(especie="canino").count()
    gatos = inscriptos.filter(especie="felino").count()

    if c_inscriptos>0:
        porcentaje_perros = perros * 100 /c_inscriptos
        porcentaje_gatos = gatos * 100 /c_inscriptos
    else:
        porcentaje_perros = 0
        porcentaje_gatos = 0

    pagados = 0
    pagados = Animalito.objects.filter(campaing=campana.id).aggregate(Sum('abono'))
    lista_atendidos = inscriptos.exclude(user_name='')
    atendidos = lista_atendidos.count()

    #parte para sacar por barrio

    barrios = Barrio.objects.all()
    estadistica = {}


    colores = (
        ("e57373","red","lighten-2"),   #0
        ("f06292","pink","lighten-2"),  #1
        ("ba68c8","purple","lighten-2"),    #2
        ("9575cd","deep-purple","lighten-2"),
        ("7986cb","indigo","lighten-2"),
        ("64b5f6","blue","lighten-2"),  #5
        ("4dd0e1","cyan","lighten-2"),  #6
        ("4db6ac","teal","lighten-2"),
        ("81c784","green","lighten-2"), #7
        ("aed581","light-green","lighten-2"),
        ("dce775","lime","lighten-2"),  #10
        ("fff176","yellow","lighten-2"),
        ("ffd54f","amber","lighten-2"), #12
        ("4fc3f7","light-blue","lighten-2"),
        ("ffb74d","orange","lighten-2"),    #14
        ("ff8a65","deep-orange","lighten-2"),
        ("a1887f","brown","lighten-2"),
        ("e0e0e0","grey","lighten-2"),
        ("90a4ae","blue-grey","lighten-2"),
        ("d32f2f","red","darken-2"),    #19
        ("c2185b","pink","darken-2"),
        ("7b1fa2","purple","darken-2"),
        ("512da8","deep-purple","darken-2"),
        ("303f9f","indigo","darken-2"),
        ("1976d2","blue","darken-2"),
        ("0288d1","light-blue","darken-2"),
        ("0097a7","cyan","darken-2"),
        ("00796b","teal","darken-2"),
        ("388e3c","green","darken-2"),
        ("689f38","light-green","darken-2"),
        ("afb42b","lime","darken-2"),   #30
        ("fbc02d","yellow","darken-2"),
        ("ffa000","amber","darken-2"),
        ("f57c00","orange","darken-2"),
        ("e64a19","deep-orange","darken-2"),
        ("5d4037","brown","darken-2"),  #35
        ("616161","grey","darken-2"),
        ("455a64","blue-grey","darken-2"),  #37



        )
    cuenta_color = 0

    for b in barrios:
        atendidos_barrio = lista_atendidos.filter(propietario__barrio__nombre=b.nombre)

        cant = atendidos_barrio.count()
        if cant>0:
            gatos_barrio = atendidos_barrio.filter(especie="felino").count()
            perros_barrio = atendidos_barrio.filter(especie="canino").count()
            porcentaje = cant*100/atendidos

            color_individual = colores[cuenta_color]
            color_pasar = color_individual[0]
            color_nombre_pasar = color_individual[1]
            color_descripcion_pasar = color_individual[2]
            cuenta_color = cuenta_color+1
            if cuenta_color==37:
                cuenta_color=0

            estadistica[b.nombre] = (cant, porcentaje, perros_barrio, gatos_barrio, color_pasar, color_nombre_pasar, color_descripcion_pasar)

        #estadistica[b.nombre] = cant


    est_felino = lista_atendidos.filter(especie="felino")
    est_gatos_atendidos = est_felino.filter(sexo="macho").count()
    est_gatas_atendidas = est_felino.filter(sexo="hembra").count()
    est_canino = lista_atendidos.filter(especie="canino")
    est_perros_atendidos = est_canino.filter(sexo="macho").count()
    est_perras_atendidos = est_canino.filter(sexo="hembra").count()


    color = colores[7]
    color_gato = color[0]
    color_gato_nombre = color[1]
    color_gato_descripcion = color[2]

    

    color = colores[14]
    color_gata = color[0]
    color_gata_nombre = color[1]
    color_gata_descripcion = color[2]

    

    color = colores[5]
    color_perro = color[0]
    color_perro_nombre = color[1]
    color_perro_descripcion = color[2]

    

    color = colores[12]
    color_perra = color[0]
    color_perra_nombre = color[1]
    color_perra_descripcion = color[2]
    
    if atendidos > 0:
        porcentaje_gato = est_gatos_atendidos*100/atendidos
        porcentaje_gata = est_gatas_atendidas*100/atendidos
        porcentaje_perro = est_perros_atendidos*100/atendidos
        porcentaje_perra = est_perras_atendidos*100/atendidos
    else:
        porcentaje_gato = 0
        porcentaje_gata = 0
        porcentaje_perro = 0
        porcentaje_perra = 0

    estadistica_sex_animal = {
    "Gatos Atendidos":(est_gatos_atendidos,color_gato,color_gato_nombre,color_gato_descripcion,porcentaje_gato),
    "Gatas Atendidas":(est_gatas_atendidas,color_gata,color_gata_nombre,color_gata_descripcion,porcentaje_gata),
    "Perros Atendidos":(est_perros_atendidos,color_perro,color_perro_nombre,color_perro_descripcion,porcentaje_perro),
    "Perras Atendidas":(est_perras_atendidos,color_perra,color_perra_nombre,color_perra_descripcion,porcentaje_perra),
    }
    

    saldo = campana.monto_inter_grupo_total - campana.monto_inter_grupo_gastado
    #saldo = -250  era para probar que negativo salga en rojo

    contexto = {
    "campana":campana,
    'atendidos':atendidos,
    'pagados':pagados["abono__sum"],
    'campaing':campana,
    'c_inscriptos':c_inscriptos,
    'c_preinscriptos':c_preinscriptos,
    'perros':perros,
    'gatos':gatos,
    "campanias":campanias,
    "estadistica":estadistica,
    "saldo":saldo,
    "porcentaje_perros":porcentaje_perros,
    "porcentaje_gatos":porcentaje_gatos,
    "estadistica_sexo":estadistica_sex_animal,
    }
    return render(request, "ver_campana.html",contexto)

#
@login_required(login_url='login')
def ver_colaboradores(request):
    return render(request, 'ver_colaboradores.html', {'colaboradores':Colaborador.objects.all()})

#
@login_required(login_url='login')
def create_campaing(request):
    if request.method == 'POST':
        form = CreateCampaing(request.POST)
        #import ipdb
        #ipdb.set_trace()
        if form.is_valid():       
            form.save()
            return redirect('/campaing/home_admin/')
        else:        
            return redirect('/Aca_si_no_valida_los_datos')
    else:
        contexto = {"form":CreateCampaing}

        return render(request, "create_campaing.html", contexto)

def about_campaing(request,id):
    try:
       campaing = Campaing.objects.get(id=id)       
    except Campaing.DoesNotExist:
       campaing = None

    if campaing is None or campaing.habilitada == False:
        return redirect('home')

    if request.method == 'POST':
        dni_post = request.POST['dni']
        nombre_post = request.POST['nombre']
        apellido_post = request.POST['apellido']
        telefono_post = request.POST['telefono']
        colaborador_post = request.POST['colaborador']

        ayudante = False
        padrino = False

        if colaborador_post == "C":
            ayudante = True
        elif colaborador_post == "P":
            padrino = True
        else:
            ayudante = True
            padrino = True

        colaborador = Colaborador()
        colaborador.dni = dni_post
        colaborador.nombre = nombre_post
        colaborador.apellido = apellido_post
        colaborador.telefono = telefono_post
        
        # import ipdb; ipdb.set_trace()                

        resultado = Colaborador.objects.filter(dni=dni_post).first()  

        if resultado is None:
            colaborador.save()

        camp_colabora = CampaingColaborador()
        camp_colabora.padrino = padrino
        camp_colabora.ayudante = ayudante
        camp_colabora.colaborador = colaborador
        camp_colabora.campaing = campaing

        camp_colabora.save()

        id_str = str(camp_colabora.id)          
        return redirect('../../colaborador_inscripto/'+id_str)

        # else:        
        #     return redirect('/Aca_si_no_valida_los_datos')
    template = 'about_campaing.html'
    contexto = {'campaing':campaing,'form':ColaboradorForm}    
    return render(request,template,contexto)


@login_required(login_url='login')
def alta_paciente(request,id):
    if request.method == "POST":
        dar_alta = Animalito.objects.get(pk=id)
        username = request.user.username
        dar_alta.user_name = username
        dar_alta.save()

        contexto = {
        "paciente":dar_alta,
        }
        return render(request,"paciente_dado_de_alta.html",contexto)
    try:
        paciente= Animalito.objects.get(pk=id)
        # idprop= paciente.propietario
        # propietario= Propietario.objects.get(pk=idprop)
   
    except Animalito.DoesNotExist:
        raise Http404("No se encontro la mascota")
    return render(request, "alta_paciente.html",{"paciente":paciente})


@login_required(login_url='login')
def buscar_paciente(request):
    campanias = Campaing.objects.filter(habilitada=True)
    # import ipdb; ipdb.set_trace()                
       
    #campanias = Campaing.objects.get(id=1)#(habilitada=True)
    campaing = Campaing()
    if campanias:
        campaing = campanias[0]
    inscriptos_en_campana =  Animalito.objects.filter(campaing=campaing)



    if request.method == "POST":
        form = BuscarPaciente(request.POST)

        if form.is_valid():

            query = form.cleaned_data["query"]
            pacientes = inscriptos_en_campana.filter(turno=query)
            
            return render(request, "buscar_paciente_resultado.html", {"query":query,"pacientes":pacientes})
    else:
        form = BuscarPaciente()

    return render(request,"buscar_paciente.html",{"form":form})

@login_required(login_url='login')
def home_admin(request):
    campanias = Campaing.objects.filter(habilitada=True)
    # import ipdb; ipdb.set_trace()                
    
    saldo = 0
    #campanias = Campaing.objects.get(id=1)#(habilitada=True)
    campaing = Campaing()
    if campanias:
        campaing = campanias[0] # ACÁ VA INSTANCIADA LA CAMPAÑA ACTUAL
        request.session['num'] = campaing.id
        saldo = campaing.monto_inter_grupo_total - campaing.monto_inter_grupo_gastado
        

    animales_en_campana = Animalito.objects.filter(campaing=campaing.id)

    preinscriptos = animales_en_campana.filter(turno=None)
    inscriptos = animales_en_campana.exclude(turno=None)

    cant_preinscriptos = preinscriptos.count()
    cant_inscriptos= inscriptos.count()
  
    perros = inscriptos.filter(especie="canino").count()
    gatos = inscriptos.filter(especie="felino").count()

    pagados = 0
    pagados = Animalito.objects.filter(campaing=campaing.id).aggregate(Sum('abono'))
    atendidos = inscriptos.exclude(user_name='').count()
    
    

    contexto = {
    'atendidos':atendidos,
    'pagados':pagados["abono__sum"],
    'campaing':campaing,
    'c_inscriptos':cant_inscriptos,
    'c_preinscriptos':cant_preinscriptos,
    'perros':perros,
    'gatos':gatos,
    "campanias":campanias,
    "saldo":saldo,
    'preinscripcion':campaing.preinscripcion,    
    }
    return render(request, "home_admin.html", contexto)


@login_required(login_url='login')
def inscribir_paciente_pre(request):       

    if request.method == "POST":
        form = BuscarPaciente_pre(request.POST)

        if form.is_valid():
            query = form.cleaned_data["query"]

            #falta filtrar para q los animales sean solo de la campaña
            pacientes = Animalito.objects.filter(nro_pre_inscripcion=query)
            
            return render(request, "inscribir_paciente_resultado_pre.html", {"query":query,"pacientes":pacientes})
    else:
        form = BuscarPaciente_pre()
        
    return render(request,"buscar_paciente_pre.html",{"form":form})


# incripción para los pacientes NO preinscriptos
@login_required(login_url='login')
def formulario_inscripcion(request):
    if request.method == 'POST':
                        
        formPro = PropietarioForm(request.POST)
        formAni = AnimalitoForm(request.POST)

        #import ipdb
        #ipdb.set_trace()

        if formPro.is_valid() and formAni.is_valid():
            propietario = formPro.save(commit=False)        
            propietario.save()
            animalito   = formAni.save(commit=False)         
            animalito.propietario = propietario                    
            campania = Campaing.objects.filter(habilitada=True)
            animalito.campaing = campania[0]
            campania_actualizar = campania[0]
            if animalito.abono < campania_actualizar.monto_valor_operacion:
                grupo_animal = campania_actualizar.monto_valor_operacion - animalito.abono
                campania_actualizar.monto_inter_grupo_gastado = campania_actualizar.monto_inter_grupo_gastado + grupo_animal
                campania_actualizar.save()

            animalito.save()  
            id_str = str(animalito.pk)
            return redirect('/campaing/inscripto_turno/'+id_str)
        else:        
            return redirect('/Aca_si_no_valida_los_datos')
    else:
        contexto = {"formPropietario":PropietarioForm,"formAnimalito":AnimalitoForm}

        return render(request, "formulario_inscripcion.html", contexto)

# incripción para los pacientes preinscriptos
@login_required(login_url='login')
def formulario_inscripcion_preinscriptos(request,id):
    animali = Animalito.objects.get(id = id )
    # import ipdb; ipdb.set_trace()                
    if request.method == 'GET':
        formAni = AnimalitoForm(instance = animali)        
        formPro = PropietarioForm(instance = animali.propietario)    
    else:
       # import ipdb; ipdb.set_trace()                
        formAni = AnimalitoForm(request.POST,instance=animali)
        formPro = PropietarioForm(request.POST,instance=animali.propietario)
        if formPro.is_valid() and formAni.is_valid():
            formPro.save()
            formAni.save()
            id_str = str(animali.pk)
            return redirect('/campaing/inscripto_turno/'+id_str)
        else:        
            return redirect('/Aca_si_no_valida_los_datos')

    contexto = {"formPropietario":formPro,"formAnimalito":formAni}
    return render(request, "formulario_inscripcion.html", contexto)

def pre_inscribirse(request,id):
    # campanias = Campaing.objects.filter(habilitada=True)
    try:
       campaing = Campaing.objects.get(id=id)
    except Campaing.DoesNotExist:
       campaing = None

    if campaing is None or campaing.habilitada == False or campaing.preinscripcion == False:
        return redirect('home')

    if request.method == 'POST':
        # import ipdb; ipdb.set_trace()                
        formPro = PropietarioForm(request.POST)
        formAni = AnimalitoPreinscripcionForm(request.POST)

        if formPro.is_valid() and formAni.is_valid():
            propietario = formPro.save(commit=False)        
            propietario.save()

            animalito   = formAni.save(commit=False)         
            animalito.propietario = propietario
                                 
            # animalito.campaing = campanias[0]
            animalito.campaing = campaing
            animalito.save()  

            animalito.nro_pre_inscripcion = animalito.pk
            animalito.save()

            id_str = str(animalito.pk)
            return redirect('/campaing/pre_inscripto_turno/'+id_str)    
        else:        
            return redirect('/Aca_si_no_valida_los_datos')
    else:
        campana = Campaing()
    

        contexto = {
        "formPropietario":PropietarioForm,
        "formAnimalito":AnimalitoPreinscripcionForm,


        "campana":campana,


        }

        return render(request, "pre_inscribirse.html", contexto)


@login_required(login_url='login')
def listado_preinscriptos(request):
    campanias = Campaing.objects.filter(habilitada=True)
    #campanias = Campaing.objects.get(id=1)#(habilitada=True)
    campaing = Campaing()
    if campanias:
        campaing = campanias[0] # ACÁ VA INSTANCIADA LA CAMPAÑA ACTUAL
        saldo = campaing.monto_inter_grupo_total - campaing.monto_inter_grupo_gastado
        
    animales_en_campana = Animalito.objects.filter(campaing=campaing.id)
    preinscriptos = animales_en_campana.filter(turno=None)
    #inscriptos = animales_en_campana.exclude(turno=None)

    contexto = {
    'campaing':campaing,
    #'inscriptos':inscriptos,
    'preinscriptos':preinscriptos,
    }
    return render(request, "listado_preinscriptos.html", contexto)


@login_required(login_url='login')
def listado_inscriptos(request):
    campanias = Campaing.objects.filter(habilitada=True)
    #campanias = Campaing.objects.get(id=1)#(habilitada=True)
    campaing = Campaing()
    if campanias:
        campaing = campanias[0] # ACÁ VA INSTANCIADA LA CAMPAÑA ACTUAL
        saldo = campaing.monto_inter_grupo_total - campaing.monto_inter_grupo_gastado
        
    animales_en_campana = Animalito.objects.filter(campaing=campaing.id)
    #preinscriptos = animales_en_campana.filter(turno=None)
    inscriptos = animales_en_campana.exclude(turno=None)

    contexto = {
    'campaing':campaing,
    'inscriptos':inscriptos,
    #'preinscriptos':preinscriptos,
    }
    return render(request, "listado_inscriptos.html", contexto)


@login_required(login_url='login')
def ver_qr(request):
    
    campania = Campaing.objects.filter(preinscripcion=True)
    campaing =campania[0]
    campaing.url="www.amoalosperrotes.com"#url prueba

    contexto = {
    "campaing":campaing

    }
    return render(request, "ver_qr.html", contexto)    

@login_required(login_url='login')
def crear_barrio(request):
    if request.method == 'POST':
        form = CrearBarrio(request.POST)

        #import ipdb
        #ipdb.set_trace()
        if form.is_valid():       
            form.save()
            return redirect('/campaing/home_admin/')
        else:        
            return redirect('/Aca_si_no_valida_los_datos')
    else:
        contexto = {
        "form":CrearBarrio,
        "barrios": Barrio.objects.all().order_by('nombre'),

        }

        return render(request, "crear_barrio.html", contexto)

@login_required(login_url='login')
def crear_lugar(request):
    if request.method == 'POST':
        form = CrearLugar(request.POST)

        #import ipdb
        #ipdb.set_trace()
        if form.is_valid():       
            form.save()
            return redirect('/campaing/home_admin/')
        else:        
            return redirect('/Aca_si_no_valida_los_datos')
    else:
        contexto = {
        "form":CrearLugar,
        "lugares": Lugar.objects.all().order_by('nombre'),
        }

        return render(request, "crear_lugar.html", contexto)


def creat_colaborador(request,id):
    campaing = Campaing.objects.get(id=id)
    if request.method == 'POST':
        dni_post = request.POST['dni']
        nombre_post = request.POST['nombre']
        apellido_post = request.POST['apellido']
        telefono_post = request.POST['telefono']
        padrino_post = request.POST['padrino']
        ayudante_post = request.POST['ayudante']
 
        # user = authenticate(username=username_login,password=password_login)
        colaborador = Colaborador()
        colaborador.dni = dni_post
        colaborador.nombre = nombre_post
        colaborador.apellido = apellido_post
        colaborador.telefono = telefono_post

        resultado = Colaborador.objects.get(dni=dni)    
        if resultado is None:
            colaborador.save()

        camp_colabora = CampaingColaborador()
        camp_colabora.padrino = padrino_post
        camp_colabora.ayudante = ayudante_post
        camp_colabora.colaborador = colaborador
        camp_colabora.campaing = campaing

        camp_colabora.save()

        return redirect('colaborador_inscripto')
        # else:        
        #     return redirect('/Aca_si_no_valida_los_datos')
    
    contexto = {"form":ColaboradorForm}
    return render(request, "create_colaborador.html", contexto)


@login_required(login_url='login')
def inscripto_turno(request,id):
    try:
        paciente= Animalito.objects.get(pk=id)
        # idprop= paciente.propietario
        # propietario= Propietario.objects.get(pk=idprop)
   
    except Animalito.DoesNotExist:
        raise Http404("No se encontro la mascota")
    contexto = {

        "paciente":paciente,
    }
    return render(request, "inscripto_turno.html",contexto)

def pre_inscripto_turno(request,id):
    try:
        paciente= Animalito.objects.get(pk=id)
   
    except Animalito.DoesNotExist:
        raise Http404("No se encontro la mascota")
    contexto = {"paciente":paciente,}
    return render(request, "pre_inscripto_turno.html",contexto)


def colaborador_inscripto(request,id):
    try:
        campaing_colaborador= CampaingColaborador.objects.get(id=id)

    except CampaingColaborador.DoesNotExist:
        raise Http404("No se encontro la CampaingColaborador")

    if campaing_colaborador.campaing.habilitada == False:
        return redirect('home')

    contexto = {"campaing_colaborador":campaing_colaborador}
    template = "colaborador_inscripto.html"

    return render(request, template, contexto)

#REPORTES-----------------------------------------------------

class ReportePersonasPDF(View):

    def cabecera(self,pdf):
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(230, 790, u" Amo los Perros SP")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 770, u"   Estadísticas de la campaña")
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/logoamolosperros.png'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)

    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

#-----------------------------------------------------

    def tabla(self,pdf,y):
        #Creamos una tupla de encabezados para neustra tabla
        
        encabezados = ('Dueño','Nombre Mascota','Especie','Abonó', 'Turno')
 
        detalles2 = [('Mascotas inscriptas:', '1')]
        detalles = [(animalito.propietario,animalito.nombre_mascota,animalito.especie ,animalito.abono, animalito.turno) 
        for animalito in Animalito.objects.all() if animalito.nro_pre_inscripcion is None]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        # print detalles
        detalle_orden = Table(detalles2 + [encabezados] +  detalles)
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
        [
            
            ('GRID', (0, 0), (5, -1), 1, colors.black),
            ('LINEBELOW', (0, 0), (-1, 1), 2, colors.black),
            ('BACKGROUND', (0, 0), (-1, 1), colors.grey)
        ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 90,y)

    def get(self, request, *args, **kwargs):
        
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        y= 670
        for animalito in Animalito.objects.all(): 
            if animalito.nro_pre_inscripcion is None:
                y=y-16    
        self.tabla(pdf, y)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

class ReportePersonasPDF2(View):

    def cabecera(self,pdf):
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(230, 790, u" Amo los Perros SP")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 770, u"   Estadísticas de la campaña")
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/logoamolosperros.png'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 70, 730, 120, 80,preserveAspectRatio=True)

    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

#-----------------------------------------------------

    def tabla(self,pdf,y):
        #Creamos una tupla de encabezados para neustra tabla
        
        encabezados = ('Dueño','Nombre Mascota','Especie','Abonó', 'Nro preinscripcion')
        #Creamos una lista de tuplas que van a contener a las personas
        detalles2 = [('Mascotas Preinscriptas ', ':')]
        detalles = [(animalito.propietario,animalito.nombre_mascota,animalito.especie ,animalito.abono, animalito.nro_pre_inscripcion) for animalito in Animalito.objects.all() if animalito.nro_pre_inscripcion is not None]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        # print detalles
        detalle_orden = Table(detalles2 + [encabezados] +  detalles)
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
        [
            
            ('GRID', (0, 0), (5, -1), 1, colors.black),
            ('LINEBELOW', (0, 0), (-1, 1), 2, colors.black),
            ('BACKGROUND', (0, 0), (-1, 1), colors.grey)
        ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 90,y)

    def get(self, request, *args, **kwargs):
        
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        y= 670
        for animalito in Animalito.objects.all(): 
            if animalito.nro_pre_inscripcion is not None:
                y=y-16 
        self.tabla(pdf, y)
        #Con show page hacemos un corte de página para pasar a la siguiente
        #pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

