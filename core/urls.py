from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perdidos_lista/', views.perdidos_lista, name='perdidos_lista'),
    path('achados_lista/', views.achados_lista, name='achados_lista'),

]