from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from blogs.formularios import PostForm
from blogs.models import Post

@login_required
def home(request):
    ultimos_posts = Post.objects.all().order_by("-modificado_en")[:10]
    context = {'posts': ultimos_posts}
    return render(request, "home.html", context)

@login_required
def detalle_post(request, pk):
    posible_post = Post.objects.filter(pk=pk).select_related("usuario")
    if len(posible_post) == 0:
        #no existe post
        return render(request, "404.html", status=404)
    else:
        post = posible_post[0]
        context = {'post': post}
        return render(request, "detalle_post.html", context)


class Nuevo_post(LoginRequiredMixin, View):

    def get(self, request):
        form = PostForm()
        return render(request, 'new_post_form.html', {'form': form})

    def post(self, request):
        post = Post()
        post.usuario = request.user
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            form = PostForm()
            url = reverse('pagina_detalle_post', args=[post.pk])
            message = 'Tu post se ha creado con exito '
            message += '<a href="{0}">Ver</a>'.format(url)
            messages.success(request, message)
        return render(request, 'new_post_form.html', {'form': form})


def blog_usuario(request, nombre_usuario):
    usuario = get_object_or_404(User, username=nombre_usuario)
    print(usuario)
    posts_de_usuario = Post.objects.filter(usuario=usuario).order_by('-modificado_en')

    context = {'posts': posts_de_usuario}
    return render(request, "mis_posts.html", context)



def blog_usuario_click(request, nombre_usuario, pk):
    usuario = get_object_or_404(User, username=nombre_usuario)

    posible_post = Post.objects.filter(pk=pk).select_related("usuario")
    if len(posible_post) == 0:
        return render(request, "404.html", status=404)
    else:
        post = posible_post[0]
        context = {'nombre': usuario, 'post': post}
        return render(request, "detalle_post.html", context)

