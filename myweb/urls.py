"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from easypay import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.LandingView.as_view(), name='landing'),
    path('2', views.Landing2View.as_view(), name='landing2'),
    path('3', views.Landing3View.as_view(), name='landing3'),
    path('4', views.Landing4View.as_view(), name='landing4'),
    path('5', views.Landing5View.as_view(), name='landing5'),
    path('resultado', views.EscolhasListView.as_view(), name='resultado'),
    path('salvar_escolha/', views.salvar_escolha, name='salvar_escolha'),
]   
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
