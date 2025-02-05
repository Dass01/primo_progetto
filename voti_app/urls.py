from django.urls import path
from voti_app.views import view_a, view_b, view_c, view_d


app_name="voti_app"
urlpatterns=[
    path('listaMaterie',view_a, name="listaMaterie"),
    path('listaVoti',view_b, name="listaVoti"),
    path('media_studenti',view_c, name="media_studenti"),
    path('max_min',view_d, name="max_min"),
    
]