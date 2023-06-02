from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('fears/', views.fear_index, name='fear-index'),
  path('accounts/', include('django.contrib.auth.urls')),
]