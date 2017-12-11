from django.shortcuts import render
from .forms import CreateCampaing

# Create your views here.
def create_campaing(request):

	contexto = {"form":CreateCampaing}

	return render(request, "create_campaing.html", contexto)