from django.contrib import admin
from .models import Usuario
from .models import Aluno
from .models import Noticias
from .models import Cursos
from .models import Extras

admin.site.register(Usuario)
admin.site.register(Aluno)
admin.site.register(Noticias)
admin.site.register(Cursos)
admin.site.register(Extras)


