from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('fears/', views.fear_index, name='fear-index'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup', views.signup, name='signup'),
  path('fears/<int:fear_id>/', views.fear_detail, name='fear-detail'),
  path('fears/create/', views.FearCreate.as_view(), name='fear-create'),
  path('fears/<int:pk>/update/', views.FearUpdate.as_view(), name='fear-update'),
  path('fears/<int:pk>/delete/', views.FearDelete.as_view(), name='fear-delete'),
  path('fears/<int:fear_id>/add_photo/', views.add_photo, name='add-photo'),
]