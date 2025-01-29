from django.urls import path
from prima_app.views import homepage,welcome,lista, chi_siamo,variabili,index,index_root

app_name="prima_app"
urlpatterns=[
    path('index_root',index_root, name="index_root"),
    path('homepage',homepage, name="homepage"),
    path('welcome',welcome, name="welcome"),
    path('lista',lista, name="lista"),
    path('chi_siamo',chi_siamo, name="chi_siamo"),
    path('variabili',variabili, name="variabili"),
    path('',index, name="index"),
]