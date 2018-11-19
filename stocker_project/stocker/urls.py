from django.conf.urls import url
from stocker import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^inserir_insumos/$', views.inserir_insumos.as_view(), name='inserir_insumos'),
    url(r'^retirar_insumos/$', views.retirar_insumos, name='retirar_insumos'),
]