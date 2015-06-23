"""urly_bird URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from urlmodel import views as site_views
from urlmodel.models import Bookmark, Bookmarker

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^login/$',  'django.contrib.auth.views.login',  name='view_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='view_logout'),
    url(r'^register/$', CreateView.as_view(
                template_name='registration/register.html',
                form_class=UserCreationForm, success_url='../index.html'),
                name='view_register'),
    url(r'^accounts/profile', site_views.BookmarkerView.as_view(), name='dashboard'),
    # url(r'^register/$', site_views.RegisterView.as_view(), name='view_register'),
    # my pages
    url(r'^index.html$', site_views.IndexPageView.as_view(), name='view_index'),
    url(r'^(?P<code>\w+)$', site_views.ClickView.as_view(), name='click'),
    url(r'^u/(?P<user_id>\d+)$', site_views.BookmarkerView.as_view(), name='bookmarker'),
    url(r'^b/(?P<code>\w+)$', site_views.BookmarkView.as_view(), name='bookmark'),
    url(r'^bmk_list.html$', ListView.as_view(
                    model=Bookmark,
                    template_name="lists/bmk_list.html",
                    context_object_name='bookmarks',
                    paginate_by=10
                    ), name='bmk_list'),

    url(r'^usr_list.html$', ListView.as_view(
                    model=Bookmarker,
                    template_name="lists/usr_list.html",
                    context_object_name='bookmarkers',
                    paginate_by=10
                    ), name='usr_list'),
]
