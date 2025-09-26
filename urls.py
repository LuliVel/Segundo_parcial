from django.urls import path
from . import views

urlpatterns = [
    path('videos/', views.videos_view, name='videos'),
    path('usuarios/', views.usuarios_view, name='usuarios'),
    path('creditos/', views.creditos_view, name='creditos'),
]
