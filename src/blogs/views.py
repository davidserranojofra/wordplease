from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from blogs.formularios import PostForm
from blogs.models import Post


def home(request):
    ultimos_posts = Post.objects.all().order_by("-fecha_publicacion")[:10]
    context = {'posts': ultimos_posts}
    return render(request, "home.html", context)


def detalle_post(request, pk):
    posible_post = Post.objects.filter(pk=pk).select_related("categoria")
    if len(posible_post) == 0:
        #no existe post
        return render(request, "404.html", status=404)
    else:
        post = posible_post[0]
        context = {'post': post}
        return render(request, "detalle_post.html", context)


class Nuevo_post(View):

    def get(self, request):
        form = PostForm()
        return render(request, 'new_post_form.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            form = PostForm()
            url = reverse('pagina_detalle_post', args=[post.pk])
            message = 'Tu post se ha creado con exito '
            message += '<a href="{0}">Ver</a>'.format(url)
            messages.success(request, message)
        return render(request, 'new_post_form.html', {'form': form})
