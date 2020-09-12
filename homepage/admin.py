from django.contrib import admin

from homepage.models import Author, Recipe, Favorites

# Register your models here.
admin.site.register(Author)
admin.site.register(Recipe)
admin.site.register(Favorites)
