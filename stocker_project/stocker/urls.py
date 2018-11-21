from django.conf.urls import url
from stocker import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cad_insumos/$', views.cad_insumos.as_view(), name='cad_insumos'),
    url(r'^cad_unidade/$', views.cad_unidade.as_view(), name='cad_unidade'),
    url(r'^listar_insumos/$', views.listar_insumos.as_view(), name='listar_insumos'),
    url(r'^add_insumos/(?P<id>\d+)/$', views.add_insumos.as_view(), name='add_insumos'),
    url(r'^retirar_insumos/(?P<id>\d+)/$', views.retirar_insumos.as_view(), name='retirar_insumos'),
]