from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import settings

urlpatterns = [
    # Examples:
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
