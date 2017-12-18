from django.contrib import admin

from blogs.models import Categoria, Post

admin.site.site_header = "Wordplease"
admin.site.register(Categoria)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','creado_en', 'modificado_en')
    list_filter = ('categoria', 'usuario')
    search_fields = ('titulo', 'resumen', 'cuerpo_del_post')