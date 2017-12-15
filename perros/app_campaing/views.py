from django.shortcuts import render, redirect
from django.db.models import Sum
from .forms import CreateCampaing, BuscarPaciente, AnimalitoForm, PropietarioForm, AnimalitoPreinscripcionForm



from .forms import CreateCampaing, BuscarPaciente_pre, BuscarPaciente

from .models import Campaing, Animalito, Propietario
from .models import Colaborador
from django.http import Http404

def creado(request):
    return render(request, 'creado.html', {})


def ver_campanas(request):

    return render(request, 'ver_campanas.html', {'campanas':Campaing.objects.all()})

def ver_colaboradores(request):

    return render(request, 'ver_colaboradores.html', {'colaboradores':Colaborador.objects.all()})

def create_campaing(request):
    if request.method == 'POST':
        form = CreateCampaing(request.POST)
        if form.is_valid():       
            form.save()
            return redirect('/campaing/creado/')
        else:        
            return redirect('/Aca_si_no_valida_los_datos')
    else:
        contexto = {"form":CreateCampaing}

        return render(request, "create_campaing.html", contexto)
        

def home(request):

    contexto = {}
    return render(request, "home.html", contexto)

def alta_paciente(request,id):
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
    campanias = Campaing.objects.get(id=1)#(habilitada=True)
    campaing = campanias# ACÁ VA INSTANCIADA LA CAMPAÑA ACTUAL
    c_inscriptos = Animalito.objects.filter(campaing=campaing.id).count()
    inscriptos = Animalito.objects.filter(campaing=campaing.id)
    perros = inscriptos.filter(especie="CANINO").count()
    gatos = inscriptos.filter(especie="FELINO").count()
    pagados = Animalito.objects.filter(campaing=campaing.id).aggregate(Sum('abono'))
    atendidos = inscriptos.exclude(user_name='').count()
    contexto = {'atendidos':atendidos, 'pagados':pagados["abono__sum"],'campaing':campaing,'c_inscriptos':c_inscriptos, 'perros':perros, 'gatos':gatos}
    return render(request, "home_admin.html", contexto)




def inscribir_paciente_pre(request): 
       


    if request.method == "POST":
        form = BuscarPaciente_pre(request.POST)

        if form.is_valid():
            query = form.cleaned_data["query"]



            pacientes = Animalito.objects.filter(nro_pre_inscripcion=query)

                
            return render(request, "inscribir_paciente_resultado_pre.html", {"query":query,"pacientes":pacientes})


    else:
        form = BuscarPaciente_pre()

        
    return render(request,"buscar_paciente_pre.html",{"form":form})


def formulario_inscripcion(request):

    if request.method == 'POST':
        form = FormularioInscripcion(request.POST)
        if form.is_valid():

            #crear animalito
            #crear propietario
            animal = Animalito()
            propietario = Propietario()
            #asignarles los datos del form

            animal.especie = form.POST["especie"]
            propietario.dni = form.POST["dni"]
            propietario.apellido = form.POST["apellido"]
            propietario.nombre = form.POST["nombre"]
            propietario.telefono = form.POST["telefono"]
            propietario.barrio = form.POST["barrio"]
            animal.nombre = form.POST["nombre_paciente"]
            animal.sexo = form.POST["sexo"]
            animal.descripcion = form.POST["descripcion"]
            animal.turno = form.POST["turno"]
            animal.abono = form.POST["abono"]
                     
            #relacionar animal con propietario
            #guardar animal y propietario

            propietario.save()
            animal.propietario = propietario
            campania = Campaing.objects.filter(habilitada=True)
            animal.campaing = campania
            animal.save()
        
            return redirect('/campaing/creado/')
        else:        
            return redirect('/Aca_si_no_valida_los_datos')
    else:
        contexto = {"formPropietario":PropietarioForm,"formAnimalito":AnimalitoForm}

        return render(request, "formulario_inscripcion.html", contexto)




def pre_inscribirse(request):
    if request.method == 'POST':

        form_propietario = PropietarioForm(request.POST)
        form_animalito = AnimalitoPreinscripcionForm(request.POST)

        if form_propietario.is_valid() and form_animalito.is_valid():

            #crear animalito
            #crear propietario
            animal = Animalito()
            propietario = Propietario()
            #asignarles los datos del form

            animal.especie = form_animalito.POST["especie"]
            propietario.dni = form_propietario.POST["dni"]
            propietario.apellido = form_propietario.POST["apellido"]
            propietario.nombre = form_propietario.POST["nombre"]
            propietario.telefono = form_propietario.POST["telefono"]
            propietario.barrio = form_propietario.POST["barrio"]
            animal.nombre = form_animalito.POST["nombre"]
            animal.sexo = form_animalito.POST["sexo"]
            animal.descripcion = form_animalito.POST["descripcion"]
                     
            #relacionar animal con propietario
            #guardar animal y propietario

            propietario.save()
            animal.propietario = propietario
            campania = Campaing.objects.filter(habilitada=True)
            animal.campaing = campania[0]
            animal.save()
        
            return redirect('/campaing/creado/')
        else:        
            return redirect('/Aca_si_no_valida_los_datos')
    else:
        contexto = {"formPropietario":PropietarioForm,"formAnimalito":AnimalitoPreinscripcionForm}

        return render(request, "pre_inscribirse.html", contexto)