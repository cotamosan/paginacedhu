# urls.py
from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('servicios/', views.servicios, name='servicios'),
    path('Agendar/', views.Agendar, name='agendar'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('RecuperarContrasena/', views.RContrasena, name='RContrasena'),
    path('Galeria/', views.gestion_galeria, name='Galeria'),
    path('Tipdelasemana/', views.gestion_tip, name='Tipdelasemana'),
    path('Gestioncitas/', views.gestion, name='gestioncitas'),
    path('modificarservicio/', views.modificar_servicio, name='modificarservicio'),
    path('registroCita/', views.RegistroC, name='registroc'),
    path('eliminar-tip/<int:tip_id>/', views.eliminar_tip, name='eliminar_tip'),
    path('obtener-tip-actual/', views.obtener_tip_actual, name='obtener_tip_actual'),
    path('backup/', views.backup, name='backup'),
    path('api/servicios/', views.api_servicios, name='api_servicios'),
    path('api/servicios/<int:servicio_id>/', views.api_servicios, name='api_servicio_detail'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/eliminar/<str:documento>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('usuarios/editar/<str:documento>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/toggle-estado/<str:documento>/', views.toggle_estado_usuario, name='toggle_estado_usuario'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('logout/', views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)