from django.contrib import admin

from .models import *

admin.site.register(Film)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Poster)