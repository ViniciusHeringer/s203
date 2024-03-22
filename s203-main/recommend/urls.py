from django.urls import path
from django.urls import path
from .views import CriarUsuariosView, ListaUsuariosView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signUp, name='signup'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('watch/', views.watch, name='watch'),
    path('recommend/', views.recommend, name='recommend'),
    path('criar-usuarios/', CriarUsuariosView.as_view(), name='criar_usuarios'),
    path('listar-usuarios/', ListaUsuariosView.as_view(), name='listar_usuarios'),
]


]