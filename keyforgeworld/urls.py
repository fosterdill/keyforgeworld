"""keyforgeworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers
from card import views as card_views
from synergy import views as synergy_views

router = routers.DefaultRouter()
router.register(r'cards', card_views.CardViewSet, 'hi')
router.register(r'synergies', synergy_views.SynergyViewSet, 'hi')
router.register(r'turns', synergy_views.TurnViewSet, 'hi')
router.register(r'events', synergy_views.EventViewSet, 'hi')

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token),
]
