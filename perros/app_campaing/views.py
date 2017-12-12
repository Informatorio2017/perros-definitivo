from django.shortcuts import render, redirect
from .forms import CreateCampaing




def creado(request):
	return render(request, 'creado.html', {})	


def create_campaing(request):

	

    if request.method == 'POST':

        form = CreateCampaing(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/campaing/creado/')
        else:
        	return redirect('/creado/')

    else:
    	contexto = {"form":CreateCampaing}
    	return render(request, "create_campaing.html", contexto)
    	

    
        

    