
#url campaing

from django.conf.urls import url
from . import views

urlpatterns = [

  

    url(r'^create_campaing/', views.create_campaing, name="create_campaing"),
   

]
