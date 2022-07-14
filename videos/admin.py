from django.contrib import admin
from videos import models


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    fields = ['release_year', 'title', 'length']
    search_fields = ['title']
    list_filter = ['release_year', 'length']
    list_display = ['title', 'length', 'release_year']
    list_editable = ['length']


# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)