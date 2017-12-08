from django.http import HttpResponse
from django.shortcuts import render

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



