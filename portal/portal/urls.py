from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import views as auth_views
from apps.usuarios.views import acesso_negado
from apps.usuarios.views import dashboard, lista_usuarios
from apps.usuarios.views import logout_agradecimento
from apps.pacientes.views import lista_pacientes, novo_paciente
from apps.laudos.views import laudos_paciente, lista_laudos

def superuser_required(user):
    return user.is_superuser

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),
    path('acesso-negado/', acesso_negado, name='acesso_negado'), 
    
    # AUTENTICACAO
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='logout_agradecimento'), name='logout'),
    path('logout-agradecimento/', logout_agradecimento, name='logout_agradecimento'),
    
    # MAIN
    path('dashboard/', dashboard, name='dashboard'),
    
    # LAUDOS
    path('laudo/', include('apps.laudos.urls')),

    # PACIENTES
    path('pacientes/', lista_pacientes, name='lista_pacientes'),
    path('pacientes/<int:paciente_id>/laudos/', laudos_paciente, name='laudos_paciente'),
    path('pacientes/novo/', novo_paciente, name='novo_paciente'),

    # USUARIOS
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)