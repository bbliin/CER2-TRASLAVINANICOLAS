"""
URL configuration for CER2-TRASLAVINANICOLAS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="inicio"),
    path('materiales',views.materiales, name="materiales"),
    path('puntos',views.puntos, name="puntos"),
    path('metricas',views.metricas, name="metricas"),
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/',views.salir, name='salir'),
    path('solicitud', views.solicitud, name='solicitud'),
    path('solicitud/<int:id>/',views.solicitud, name='solicitud'),
    path('recomendaciones',views.recomendaciones, name='recomendaciones'),
]

