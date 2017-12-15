from django.shortcuts import render, redirect
from .forms import CreateCampaing, BuscarPaciente_pre
from .forms import CreateCampaing, BuscarPaciente, AnimalitoForm, PropietarioForm
from .models import Campaing, Animalito, Propietario
from .models import Colaborador

campaning = None

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


def buscar_paciente(request):
    contexto = {}
    return render(request, "base.html", contexto)

def home_admin(request):
    campaing = Campaing.objects.filter(habilitada=True)
    contexto = {'campaing':campaing}
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
    
    return render(request,"buscar_paciente.html",{"form":form})

def formulario_inscripcion(request):
    if request.method == 'POST':
        # import ipdb; ipdb.set_trace()                
        formPro = PropietarioForm(request.POST)
        formAni = AnimalitoForm(request.POST)

        if formPro.is_valid() and formAni.is_valid():
            #crear animalito
            #crear propietario
            propietario = formPro.save(commit=False)        
            propietario.save()

            animalito   = formAni.save(commit=False)         
            animalito.propietario = propietario
                     
            campania = Campaing.objects.filter(habilitada=True)

            animalito.campaing = campania[0]
            animalito.save()  
        
            return redirect('/campaing/creado/')
        else:        
            return redirect('/Aca_si_no_valida_los_datos')
    else:
        contexto = {"formPropietario":PropietarioForm,"formAnimalito":AnimalitoForm}

        return render(request, "formulario_inscripcion.html", contexto)


