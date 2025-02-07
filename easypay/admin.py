from django.contrib import admin

# Register your models here.
from .models import Objeto, Escolha
admin.site.register(Objeto)
admin.site.register(Escolha)