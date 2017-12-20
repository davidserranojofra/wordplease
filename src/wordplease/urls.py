"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blogs.views import home, detalle_post, Nuevo_post, blog_usuario, blog_usuario_click
from usuarios.api import ListarblogsAPI, ListarActualizarBorrarUsuarios
from usuarios.views import LoginView, LogoutView, ListadoBlogs, signup

urlpatterns = [
    #admin Django
    path('admin/', admin.site.urls),

    #usuarios
    path('login', LoginView.as_view(), name='pagina_login'),
    path('logout', LogoutView.as_view(), name='pagina_logout'),
    path('signup', signup, name='pagina_signup'),

    #blogs
    path('new-post', Nuevo_post.as_view(), name="pagina_nuevo_post"),
    #path('posts/<int:pk>', detalle_post, name="pagina_detalle_post"),
    path('blogs/<slug:nombre_usuario>/<int:pk>', blog_usuario_click, name="pagina_detalle_post_usuario"),
    path('blogs/<slug:nombre_usuario>', blog_usuario, name="pagina_posts_propios"),
    path('blogs/', ListadoBlogs.as_view(), name="pagina_listado_blogs"),
    path('', home, name="pagina_inicio"),

    #API REST

    #API de usuarios

    #API de blogs
    path('api/1.0/blogs/', ListarblogsAPI.as_view(), name='api_listar_blogs'),




    #API de blogs

    #API de posts


]
