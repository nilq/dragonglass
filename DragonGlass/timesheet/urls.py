from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'([\d\w]{32})', views.index, name='index'),
]
