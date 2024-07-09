from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('reserva', views.reserva, name='reserva'),
    path('cliente', views.cliente, name='cliente'),
    path('registro', views.registro, name='registro'),
    path('signout', views.signout, name='signout'),
    path('edit/', views.edit1),
    path('edit1/<rut>', views.edit),
    path('delete/<rut>', views.delete),

]