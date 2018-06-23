from django.conf.urls import url,include
from django.contrib.auth.views import LogoutView
from usuarios.views import  RegisterUserView, LoginUserView, DashboardView

urlpatterns = [
    # url(r'^$', UsuarioPageView,.usuariopage),
    url(r'^register/$', view=RegisterUserView.as_view(), name='register'),
    url(r'^login/$', view=LoginUserView.as_view(), name='login'),
    url(r'^logout/$', view=LogoutView.as_view(), name='logout'),
    url(r'^dashboard/$', view=DashboardView.as_view(), name='dashboard')
]