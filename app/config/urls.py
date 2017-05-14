# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views
from django.views.generic import TemplateView
from django.views import defaults as default_views

from visual_site_elements.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    # url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    # url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # Your stuff: custom urls includes go here
    # url(r'^images/', include('django_images.urls')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    # url(r'^pages/', include('django.contrib.flatpages.urls')),  # for flatpages urls
    url(r'^pages/hakkimizda/$', views.flatpage, {'url': '/hakkimizda/'}, name='hakkimizda'),
    url(r'^pages/hizmetlerimiz/$', views.flatpage, {'url': '/hizmetlerimiz/'}, name='hizmetlerimiz'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
