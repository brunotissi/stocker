from django.conf.urls import url
from stocker import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]