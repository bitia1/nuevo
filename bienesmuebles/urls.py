from django.conf.urls import url,include
from .views import homeview, ArtuculoView

urlpatterns = [
    url(r'^$', homeview),
    url(r'^nuevo/$', view=ArtuculoView.as_view(), name='register'),
]