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

from blogs.api import ListarPostsAPI, PostDetalleAPI
from blogs.views import home, Nuevo_post, blog_usuario, blog_usuario_click
from usuarios.api import UsuarioDetalleAPI, RegistroUsuario, ListadoBlogsUsuarios
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
    path('blogs/<slug:nombre_usuario>/<int:pk>', blog_usuario_click, name="pagina_detalle_post_usuario"),
    path('blogs/<slug:nombre_usuario>', blog_usuario, name="pagina_posts_propios"),
    path('blogs/', ListadoBlogs.as_view(), name="pagina_listado_blogs"),
    path('', home, name="pagina_inicio"),



    #API REST

    #API de usuarios
    path('api/1.0/usuarios/<int:pk>', UsuarioDetalleAPI.as_view(), name='api_listar_usuarios_detalle'),
    path('api/1.0/usuarios/', RegistroUsuario.as_view(), name='api_registrar_usuarios'),

    #API de posts
    path('api/1.0/blogs/<usuario>', ListarPostsAPI.as_view(), name='api_listar_posts'),
    path('api/1.0/posts/<int:pk>', PostDetalleAPI.as_view(), name='api_detalle_posts'),

    # API de blogs
    path('api/1.0/blogs/', ListadoBlogsUsuarios.as_view(), name='api_listar_blogs')



]
