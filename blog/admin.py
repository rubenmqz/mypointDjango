from django.contrib import admin
from blog.models import Post, Category

#TODO: Personalizar nombres de modelos en español (singular/plural)

admin.site.register(Post)
admin.site.register(Category)