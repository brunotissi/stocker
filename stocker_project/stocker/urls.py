from django.conf.urls import url
from stocker import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cad_insumos/$', views.cad_insumos.as_view(), name='cad_insumos'),
    url(r'^cad_unidade/$', views.cad_unidade.as_view(), name='cad_unidade'),
    url(r'^listar_insumos/$', views.listar_insumos.as_view(), name='listar_insumos'),
    url(r'^edit_insumos/(?P<id>\d+)/$', views.edit_insumos.as_view(), name='edit_insumos'),
]