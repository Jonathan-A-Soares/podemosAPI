"""api URL Configuration

"""
from django.contrib import admin
from django.urls import path,include
from core.views import AlunoViewSet
from core.views import NoticeViewSet
from core.views import CursoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alunos',AlunoViewSet)
router.register(r'noticias',NoticeViewSet)
router.register(r'cursos',CursoView)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
