from stocker import views
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView
from django.conf.urls.i18n import i18n_patterns

class MyRegistrationView(RegistrationView):
    def get_sucess_url(self, user):
        return '/stocker/'

urlpatterns = [
]

urlpatterns += i18n_patterns(
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.redirect_view, name='redirect_view'),
    url(r'^stocker/', include('stocker.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'accounts/', include('registration.backends.simple.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
