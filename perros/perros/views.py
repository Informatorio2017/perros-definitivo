from django.shortcuts import render,redirect
from .forms import LoginForm, CreateUserForm
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app_campaing.models import Campaing

def base(request):
	return render(request, "base.html", {})

def home(request):
	campanias = Campaing.objects.filter(habilitada=True)
	campaing = Campaing()
	if campanias:
		campaing = campanias[0] # ACÁ VA INSTANCIADA LA CAMPAÑA ACTUAL

	contexto = {'campaing':campaing}
	return render(request,"home.html",contexto)

def login(request):
	if request.user.is_authenticated():
		return redirect('app_campaing:home_admin')	
	#  5 tipos de mensajes. de éxito, de error, de informacion, de debug, de wardning
	
	if request.method == "POST":
		username_login = request.POST['username']
		password_login = request.POST['password']
 
		user = authenticate(username=username_login,password=password_login)
		if user is not None:
			login_django(request,user)
			return redirect('app_campaing: home_admin')
		else:
			messages.error(request, 'Usuario o password incorrecto!!')

	form = LoginForm()
	contexto={'form':form}
	return render(request,'login.html',contexto)

@login_required(login_url='login')
def home_usuario(request):
	contexto={'username':request.user.username}
	return render(request,'home.html',contexto)

@login_required(login_url='login')
def logout(request):
	logout_django(request)
	return redirect('login')

def create_user(request):
	form = CreateUserForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(user.password)	
			user.save()

			return redirect('login')

	contexto = {'form':form}
	return render(request,'create_user.html',contexto)