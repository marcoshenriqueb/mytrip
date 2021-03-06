"""myview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from home.views import HomePageView, CorporateView, LeadView, ServicePageView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^lead/$', LeadView.as_view(), name='lead'),
    url(r'^corporate/$', CorporateView.as_view(), name='corporate'),
    url(r'^(?P<uri>[a-z0-9-]+)/$', ServicePageView.as_view(), name='service'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)