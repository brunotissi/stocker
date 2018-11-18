from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from stocker import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stocker/', include('stocker.urls')),
    url(r'^admin/', admin.site.urls),
]