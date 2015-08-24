from django.contrib import admin
from .models import Author, Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
   list_display   = ('Sujet', 'Author', 'created')
   list_filter    = ('Author','created')
   search_fields  = ('Sujet', 'Contenu')

admin.site.register(Author)
admin.site.register(Article)
