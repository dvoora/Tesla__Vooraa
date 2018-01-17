"""rent_home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import *
from app.updates import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create/owner/', CreateOwner.as_view(),name='Create owner'),
    url(r'^list/owner/', ListOwners.as_view(),name='Create owner'),
    url(r'^delete/owner/', DeleteOwner.as_view(),name='Create owner'),
    url(r'^update/owner/', UpdateOwner.as_view(),name='Create owner'),
    url(r'^create/homeasset/', CreateHomeAssests.as_view(),name='Create owner'),
    url(r'^list/homeasset/', ListHomeAssests.as_view(),name='Create owner'),
    url(r'^delete/homeasset/', DeleteHomeAssests.as_view(),name='Create owner'),
    url(r'^update/homeasset/', UpdateHomeAssests.as_view(),name='Create owner'),
    url(r'^create/renter/', CreateRenter.as_view(),name='Create owner'),
    url(r'^list/renter/', ListRenter.as_view(),name='Create owner'),
    url(r'^delete/renter/', DeleteRenter.as_view(),name='Create owner'),
    url(r'^update/renter/', UpdateRenter.as_view(),name='Create owner'),
	url(r'^bookroom/', BookRoom.as_view(),name='Create owner'),  
	url(r'^checkavailable/', CheckAvailabilty.as_view(),name='Create owner'),
	url(r'^cancelroom/', CancelBookedRoom.as_view(),name='Create owner'),
]
