from django.urls import path
from appcoder.views import inicio
from django.conf import settings
from django.conf.urls.static import static
from . import views 
from .views import *

urlpatterns = [
    path('', inicio),
    path('about-me/', about_me_view, name='about_me'),
    path('crear/', crear_publicacion, name='crear_publicacion'),
    path('publicaciones/', PublicacionListView.as_view(), name='publicacion_list'),
    path('publicacion/<int:pk>/', PublicacionDetailView.as_view(), name='publicacion_detail'),
    path('publicacion/<int:pk>/editar/', PublicacionUpdateView.as_view(), name='publicacion_update'),
    path('publicacion/<int:pk>/borrar/', PublicacionDeleteView.as_view(), name='publicacion_delete'),

    path('login/', login_view, name='login_view'),
    path('signup/', signup_view, name='signup_view'),
    path('logout/', logout_view, name='logout_view'),
    path('inicio-no-autenticado/', inicio_no_autenticado, name='inicio_no_autenticado'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)