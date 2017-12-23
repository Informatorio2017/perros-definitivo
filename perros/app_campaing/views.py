from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import Http404
from .forms import AnimalitoForm, PropietarioForm, AnimalitoPreinscripcionForm
from .forms import CreateCampaing, BuscarPaciente_pre, BuscarPaciente, CrearBarrio, CrearLugar, ColaboradorForm
from .models import Campaing, Animalito, Propietario, Barrio, Lugar
from .models import Colaborador, CampaingColaborador

campaning = None

def cerrar_inscripcion_campaing(request,id):
    campaing = Campaing.objects.get(id=id)
    
    template = 'confirmar_fin_inscrip.html'
    contexto = {
    "campaing":campaing,
    }
    return render(request,template,contexto)
    

def fin_campaing(request,id):
    campaing = Campaing.objects.get(id=id)
    
    template = 'confirmar_fin_campana.html'
    contexto = {
    "campaing":campaing,
    }
    return render(request,template,contexto)



#se va esta view
def creado(request):
    return render(request, 'creado.html', {})

#
def ver_campanas(request):
    return render(request, 'ver_campanas.html', {'campanas':Campaing.objects.all()})

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
    porcentaje_perros = perros * 100 /c_inscriptos
    gatos = inscriptos.filter(especie="felino").count()
    porcentaje_gatos = gatos * 100 /c_inscriptos
   

    pagados = Animalito.objects.filter(campaing=campana.id).aggregate(Sum('abono'))
    lista_atendidos = inscriptos.exclude(user_name='')
    atendidos = lista_atendidos.count()

    #parte para sacar por barrio

    barrios = Barrio.objects.all()
    estadistica = {}


    colores = (
        ("e57373","red","lighten-2"),
        ("f06292","pink","lighten-2"),
        ("ba68c8","purple","lighten-2"),
        ("9575cd","deep-purple","lighten-2"),
        ("7986cb","indigo","lighten-2"),
        ("64b5f6","blue","lighten-2"),
        ("4dd0e1","cyan","lighten-2"),
        ("4db6ac","teal","lighten-2"),
        ("81c784","green","lighten-2"),
        ("aed581","light-green","lighten-2"),
        ("dce775","lime","lighten-2"),
        ("fff176","yellow","lighten-2"),
        ("ffd54f","amber","lighten-2"),
        ("4fc3f7","light-blue","lighten-2"),
        ("ffb74d","orange","lighten-2"),
        ("ff8a65","deep-orange","lighten-2"),
        ("a1887f","brown","lighten-2"),
        ("e0e0e0","grey","lighten-2"),
        ("90a4ae","blue-grey","lighten-2"),
        ("d32f2f","red","darken-2"),
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
        ("afb42b","lime","darken-2"),
        ("fbc02d","yellow","darken-2"),
        ("ffa000","amber","darken-2"),
        ("f57c00","orange","darken-2"),
        ("e64a19","deep-orange","darken-2"),
        ("5d4037","brown","darken-2"),
        ("616161","grey","darken-2"),
        ("455a64","blue-grey","darken-2"),



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


    color = colores[5]
    color_gato = color[0]
    color_gato_nombre = color[1]
    color_gato_descripcion = color[2]

    color = colores[10]
    color_gata = color[0]
    color_gata_nombre = color[1]
    color_gata_descripcion = color[2]

    color = colores[13]
    color_perro = color[0]
    color_perro_nombre = color[1]
    color_perro_descripcion = color[2]

    color = colores[16]
    color_perra = color[0]
    color_perra_nombre = color[1]
    color_perra_descripcion = color[2]

    estadistica_sex_animal = {
    "Gatos Atendidos":(est_gatos_atendidos,color_gato,color_gato_nombre,color_gato_descripcion),
    "Gatas Atendidas":(est_gatas_atendidas,color_gata,color_gata_nombre,color_gata_descripcion),
    "Perros Atendidos":(est_perros_atendidos,color_perro,color_perro_nombre,color_perro_descripcion),
    "Perras Atendidas":(est_perras_atendidos,color_perra,color_perra_nombre,color_perra_descripcion),
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
def ver_colaboradores(request):
    return render(request, 'ver_colaboradores.html', {'colaboradores':Colaborador.objects.all()})

#
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
    campaing = Campaing.objects.get(id=id)
    if request.method == 'POST':
        dni_post = request.POST['dni']
        nombre_post = request.POST['nombre']
        apellido_post = request.POST['apellido']
        telefono_post = request.POST['telefono']
        padrino_post = True#request.POST['padrino']
        ayudante_post = False #request.POST['ayudante']
 
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
        camp_colabora.padrino = padrino_post
        camp_colabora.ayudante = ayudante_post
        camp_colabora.colaborador = colaborador
        camp_colabora.campaing = campaing

        camp_colabora.save()
        
        return redirect('../../colaborador_inscripto')

        # else:        
        #     return redirect('/Aca_si_no_valida_los_datos')
    template = 'about_campaing.html'
    contexto = {'campaing':campaing,'form':ColaboradorForm}    
    return render(request,template,contexto)


def home(request):
    contexto = {}
    return render(request, "home.html", contexto)

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


def buscar_paciente(request):

    if request.method == "POST":
        form = BuscarPaciente(request.POST)

        if form.is_valid():

            query = form.cleaned_data["query"]
            pacientes = Animalito.objects.filter(turno=query)
            
            return render(request, "buscar_paciente_resultado.html", {"query":query,"pacientes":pacientes})
    else:
        form = BuscarPaciente()

    return render(request,"buscar_paciente.html",{"form":form})


def home_admin(request):
    campanias = Campaing.objects.filter(habilitada=True)
    saldo = 0
    #campanias = Campaing.objects.get(id=1)#(habilitada=True)
    campaing = Campaing()
    if campanias:
        campaing = campanias[0] # ACÁ VA INSTANCIADA LA CAMPAÑA ACTUAL
        saldo = campaing.monto_inter_grupo_total - campaing.monto_inter_grupo_gastado
        

    animales_en_campana = Animalito.objects.filter(campaing=campaing.id)

    preinscriptos = animales_en_campana.filter(turno=None)
    inscriptos = animales_en_campana.exclude(turno=None)

    cant_preinscriptos = preinscriptos.count()
    cant_inscriptos= inscriptos.count()
  
    perros = inscriptos.filter(especie="canino").count()
    gatos = inscriptos.filter(especie="felino").count()

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
    
    }
    return render(request, "home_admin.html", contexto)


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

def pre_inscribirse(request):
    if request.method == 'POST':
        # import ipdb; ipdb.set_trace()                
        formPro = PropietarioForm(request.POST)
        formAni = AnimalitoPreinscripcionForm(request.POST)

        if formPro.is_valid() and formAni.is_valid():
            propietario = formPro.save(commit=False)        
            propietario.save()

            animalito   = formAni.save(commit=False)         
            animalito.propietario = propietario
                     
            campania = Campaing.objects.filter(habilitada=True)

            animalito.campaing = campania[0]
            animalito.save()  

            animalito.nro_pre_inscripcion = animalito.pk
            animalito.save()

            id_str = str(animalito.pk)
            return redirect('/campaing/pre_inscripto_turno/'+id_str)    
        else:        
            return redirect('/Aca_si_no_valida_los_datos')
    else:
        contexto = {"formPropietario":PropietarioForm,"formAnimalito":AnimalitoPreinscripcionForm}

        return render(request, "pre_inscribirse.html", contexto)


def ver_qr(request):
    
    campania = Campaing.objects.filter(preinscripcion=True)
    campaing =campania[0]
    campaing.url="www.amoalosperrotes.com"#url prueba

    contexto = {
    "campaing":campaing

    }
    return render(request, "ver_qr.html", contexto)    


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

def colaborador_inscripto(request):
    template = "colaborador_inscripto.html"
    contexto = {}
    return render(request, template, contexto)
