from django.urls import path
from .views import index_corsi, view_a, view_b, view_c, view_d, view_e, view_f

app_name="corsi_formazione"
urlpatterns=[
    path('index_corsi',index_corsi, name="index_corsi"),
    path('view_a',view_a, name="view_a"),
    path('view_b/<int:pk>',view_b, name="view_b"),
    path('view_c',view_c, name="view_c"),
    path('view_d',view_d, name="view_d"),
    path('view_e',view_e, name="view_e"),
    path('view_f',view_f, name="view_f"),
   
]