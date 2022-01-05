from django.contrib import admin

# Register your models here.

from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title", "author"]

    list_display_links = ["title","author"] # link vererek sayfaları açmak

    search_fields = ["title"] #arama özelliği ekleme

    list_filter = ["created_date"]
    
    class Meta:
        model = Article


