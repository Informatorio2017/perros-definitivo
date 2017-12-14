from django.shortcuts import render, redirect
from .forms import CreateCampaing
from .models import Campaing


def creado(request):
    return render(request, 'creado.html', {})


def ver_campanas(request):

    return render(request, 'ver_campanas.html', {'campanas':Campaing.objects.all()})


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





def inscribir_paciente(request):
       

    if request.method == "POST":
        form = BuscarPaciente(request.POST)

        if form.is_valid():

            query = form.cleaned_data["query"]

            movimientos = Movimiento.objects.filter(nro_pre_inscripcion=query)
                
            return render(request, "inscribir_paciente_resultado.html", {"query":query,"movimientos":movimientos})

    else:
        form = BuscarPaciente()

        
    return render(request,"inscribir_paciente.html",{"form":form})





def formulario_inscripcion(request):
    contexto = {}
    return render(request, "inscribir_paciente.html", contexto)
