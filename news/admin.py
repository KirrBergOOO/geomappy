from django.contrib import admin
from .models import Articles
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Articles, ArticlesAdmin)
