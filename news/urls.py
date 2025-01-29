from django.urls import path
from news.views import index_root, home, articoloDetailView, listaArticoli, queryBase, giornalistaDetailView,index

app_name="news"
urlpatterns=[
    path('index_root',index_root, name="index_root"),
    path('homeview',home,name="homeview"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli", listaArticoli, name="lista_articoli"),
    path("lista_articoli/<int:pk>", listaArticoli, name="lista_articoli"),
    path("queryBase", queryBase, name="queryBase"),
    path("giornalisti/<int:pk>", giornalistaDetailView, name="giornalista_detail"),
    path('index',index, name="index"),
]