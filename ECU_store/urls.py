"""
URL configuration for ECU_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from db_ecu.views import ecu_tables, create_ecu
from user.views import sing_up
from add_ecu.views import add_ecu


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ECU-tables/', ecu_tables, name='ecu-tables'),
    path('create-ecu/', create_ecu, name='create-ecu'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sing-up/', sing_up, name='sing-up'),
    path('add-ecu/', add_ecu, name='add-ecu'),
]
