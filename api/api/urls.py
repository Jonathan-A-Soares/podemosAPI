"""api URL Configuration

"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from core.views import AlunoViewSet
from core.views import NoticeViewSet
from core.views import CursoView
from core.views import ExtraView
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import(TokenObtainPairView,TokenRefreshView)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alunos',AlunoViewSet)
router.register(r'noticias',NoticeViewSet)
router.register(r'cursos',CursoView)
router.register(r'extras', ExtraView)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/login/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    #path('token-auth',obtain_jwt_token)
    

]
