from django.contrib import admin

from blogs.models import Categoria, Post

admin.site.site_header = "Wordplease"
admin.site.register(Categoria)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','resumen', 'url_foto', 'fecha_publicacion')
    list_filter = ('categoria', 'usuario', 'fecha_publicacion')
    search_fields = ('titulo', 'resumen', 'cuerpo_del_post')