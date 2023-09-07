from django.urls import re_path, include
from django.contrib import admin
from . import views


app_name="perros"
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^campaing/', include('app_campaing.urls')),
    re_path(r'^$',views.home,name= 'home' ),
    re_path(r'^login/',views.login,name= 'login' ),
    re_path(r'^logout/',views.logout,name= 'logout' ),
    re_path(r'^creditos/', views.creditos, name="creditos"),
]
