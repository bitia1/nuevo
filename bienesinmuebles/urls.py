from django.conf.urls import url,include
from .views import BienesInmueblesmView

urlpatterns = [
    url(r'^mapa/$', view=BienesInmueblesmView.as_view(), name='mapa'),
]