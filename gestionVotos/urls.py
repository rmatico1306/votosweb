from django.urls import path
from gestionVotos import views
urlpatterns = [

    
    path('busquedas_actas/', views.busquedas_actas),
    path('buscar/', views.buscar),
    path('contacto/', views.contacto),
    path('resultados_votos/', views.resultados_votaciones),
    
]