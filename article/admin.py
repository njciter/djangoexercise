from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("block","title","content","status")

admin.site.register(Article,ArticleAdmin)
