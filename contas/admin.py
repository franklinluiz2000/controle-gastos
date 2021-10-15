from django.contrib import admin
from django.utils import translation
from .models import Categoria
from .models import Transacao


admin.site.register(Categoria)
admin.site.register(Transacao)
