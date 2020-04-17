from django.contrib import admin
from .models import Aluno
from .models import Noticias
from .models import Cursos

admin.site.register(Aluno)
admin.site.register(Noticias)
admin.site.register(Cursos)


