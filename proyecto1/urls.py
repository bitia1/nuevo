"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^usuario/',include('usuarios.urls')),
    url(r'^bienesmuebles/',include('bienesmuebles.urls')),
    url(r'^bienesinmuebles/',include('bienesinmuebles.urls')),
    url(r'^$', login, {'template_name':'login.html'}, name='login')
    # url(r'^$','django.contrib.auth.views.login',
    #     {'template_name':'login.html'},name='login'),
    # url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login',
    #     name='logout'),

]