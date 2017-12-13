
#url campaing

from django.conf.urls import url
from . import views

urlpatterns = [

  

    url(r'^create_campaing/', views.create_campaing, name="create_campaing"),
    url(r'^creado/', views.creado, name="creado"),



	url(r'^home/', views.home, name="home"),    
   

]
