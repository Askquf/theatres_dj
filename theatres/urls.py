"""theatres URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from main_app import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="My Theatres API",
        default_version='v333',
        description="Welcome to the best lab in the world"
    ))

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name = 'home'),
    path('theatre/<theatre_name>/', views.get_theatre),

    path('api/', views.AllApiLinks.as_view()),
    path('api/theatres/', views.TheatreViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'})),
    path('api/theatres/<id>', views.TheatreCount.as_view()),
    path('api/perfomances/', views.PerfomanceViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'})),
    path('api/districts/', views.DistrictViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'})),

    path('doc/', schema_view.with_ui())
]
