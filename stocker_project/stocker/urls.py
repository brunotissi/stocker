from django.conf.urls import url
from stocker import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^inserir_insumos/$', views.inserir_insumos.as_view(), name='inserir_insumos'),
    url(r'^cad_unidade/$', views.cad_unidade.as_view(), name='cad_unidade'),
    url(r'^listar_insumos/$', views.listar_insumos.as_view(), name='listar_insumos'),
    url(r'^edit_insumos/(?P<id>\d+)/$', views.retirar_insumos.as_view(), name='edit_insumos'),
]