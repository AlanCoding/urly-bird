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
from rest_framework import routers

from urlmodel import views as v
from urlmodel import models as m


router = routers.DefaultRouter()
router.register(r'bmks', v.BookmarkViewSet)
router.register(r'clk',  v.ClickViewSet)
router.register(r'usr',  v.BookmarkerViewSet)


urlpatterns = [
    # Django management pages
    url(r'^admin/', include(admin.site.urls)),
    # API Pages
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
            # lower level views in API-land
    # url(r'^usr/(?P<pk>\d+)', v.BookmarkerListView, name='bookmarker-list' )
    url(r'^usr/(?P<bmkr_id>\d+)/bmks/', v.BookmarkerBookmarkList.as_view(), name="bookmarker-bookmark"),
    # url(r'^usr/(?P<bmkr_id>\d+)/bmks/(?P<bmk_id>\d+)/', v.BookmarkerBookmarkClickList,
    #                                             name="bookmarker-bookmark-click")
    # url(r'^bmks/(?P<pk>\d+)/', v.BookmarkListView, name='bookmark-list')
    url(r'^bmks/(?P<bmk_id>\d+)/clicks/', v.BookmarkClickList.as_view(), name="bookmark-click"),
    # url(r'^clk/(?P<pk>\d+)', v.ClickListView, name='click-list' )

    # App pages
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^login/$',  'django.contrib.auth.views.login',  name='view_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='view_logout'),
    url(r'^register/$', v.MyRegisterView.as_view(), name='view_register'),
    url(r'^accounts/profile', v.BookmarkerView.as_view(), name='dashboard'),
    # my pages
    url(r'^index.html$', v.IndexPageView.as_view(), name='view_index'),
    url(r'^(?P<code>\w+)$', v.ClickView.as_view(), name='click'),
    url(r'^u/(?P<user_id>\d+)$', v.BookmarkerView.as_view(), name='bookmarker'),
    url(r'^b/(?P<code>\w+)$', v.BookmarkView.as_view(), name='bookmark'),
    url(r'^bmk_list.html$', ListView.as_view(
                    model=m.Bookmark,
                    template_name="lists/bmk_list.html",
                    context_object_name='bookmarks',
                    paginate_by=10
                    ), name='bmk_list'),

    url(r'^usr_list.html$', ListView.as_view(
                    model=m.Bookmarker,
                    template_name="lists/usr_list.html",
                    context_object_name='bookmarkers',
                    paginate_by=10
                    ), name='usr_list'),
]
