from .models import Bookmark, Bookmarker, Tag, Click
from .forms import BookmarkForm, BookmarkerForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import django.views.generic as views

from django.views.generic.edit import CreateView
from django.conf import settings

from django.contrib.auth.models import User

from django.utils import timezone
import pytz

# for viewset stuff
from rest_framework import viewsets, permissions, generics, filters
import urlmodel.serializer as ser
import urlmodel.permissions as per
from django.views.decorators.http import require_http_methods
# import django_filters
#
# class BookmarkerFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(name="username", lookup_type="icontains")
#     # notes = django_filters.CharFilter(name="notes", lookup_type="icontains")
#
#     class Meta:
#         model = User
#         fields = ['username', ]

# view sets

# @require_http_methods(["GET", "PUT", "DELETE", "POST"])
class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = ser.BookmarkSerializer
    # permission_classes = (permissions.IsAuthenticated,
    #                       IsOwnerOrReadOnly)
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_class = BookmarkerFilter
    queryset = Bookmark.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def get_paginate_by(self):
        """
        Use smaller pagination for HTML representations.
        """
        if self.request.accepted_renderer.format == 'html':
            return 5
        return 20

class ClickViewSet(viewsets.ModelViewSet):
    queryset = Click.objects.all()
    serializer_class = ser.ClickSerializer

class BookmarkerViewSet(viewsets.ModelViewSet):
    queryset = Bookmarker.objects.all()
    serializer_class = ser.BookmarkerSerializer

# lower level in API

class BookmarkerBookmarkList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ser.BookmarkSerializer

    def initial(self, request, *args, **kwargs):
        self.bookmarker = Bookmarker.objects.get(pk=kwargs['bmkr_id'])
        self.user = self.bookmarker.user
        super().initial(request, *args, **kwargs)

    def get_queryset(self):
        return self.user.bookmark_set

    def perform_create(self, serializer):
        usr = self.request.user
        if usr != self.user:
            raise PermissionDenied

        timezone.activate(settings.TIME_ZONE)
        now_t = timezone.now()
        timezone.deactivate()

        the_code = Bookmark.objects.allocate_code()

        serializer.save(posted_at=now_t, user=self.user, code=the_code)


class BookmarkClickList(generics.ListCreateAPIView):
    serializer_class = ser.ClickSerializer

    def initial(self, request, *args, **kwargs):
        self.bookmark = Bookmark.objects.get(pk=kwargs['bmk_id'])
        super().initial(request, *args, **kwargs)

    def get_queryset(self):
        return self.bookmark.click_set

    def perform_create(self, serializer):
        timezone.activate(settings.TIME_ZONE)
        now_t = timezone.now()
        timezone.deactivate()
        serializer.save(bookmark=self.bookmark, user=self.request.user, clicked_at=now_t)



# list sets # redundant with ViewSet
# class ClickListView(generics.ListCreateAPIView):
#     permission_classes = (permissions.IsAuthenticated, )
#     serializer_class = ser.ClickSerializer
#
#     def initial(self, request, *args, **kwargs):
#         self.user = User.objects.get(pk=kwargs['user_id'])
#         super.initial(request, *args, **kwargs)
#
#     def get_queryset(self):
#         return self.user.click_set
#
#
# class BookmarkerListView(generics.ListCreateAPIView):
#
#
# class ListView(generics.ListCreateAPIView):



# class UserBmkViewSet(viewsets.ModelViewSet):
#     permission_classes = (permissions.IsAuthenticated, )
#     serializer_class = ser.BookmarkSerializer
#     queryset = Bookmark.objects.all()
#     def get_queryset(self, user_id):
#         user = User.objects.get(pk=user_id)
#         pass
#
#
# class BmkClickViewSet(viewsets.ModelViewSet):
#     serializer_class = ser.ClickSerializer
#     queryset = Click.objects.all()
#     def get_queryset(self, bmk_id):
#         pass




class BookmarkerView(views.ListView):
    template_name = 'urlmodel/bookmarker.html'
#    model = Bookmark
    paginate_by = 20
    context_object_name = 'bookmarks'
    bookmarker = None

    def dispatch(self, *args, **kwargs):
        if 'user_id' in self.kwargs:
            self.bookmarker = Bookmarker.objects.get(pk=self.kwargs['user_id'])
        else:
            self.bookmarker = self.request.user.bookmarker
        return super(BookmarkerView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.bookmarker.user.bookmark_set.order_by('-posted_at')

    def get_context_data(self, **kwargs):
        context = super(BookmarkerView, self).get_context_data(**kwargs)
        context['bookmarker'] = self.bookmarker
        return context


class IndexPageView(views.CreateView):
    template_name = 'index.html'
    model = Bookmark
    # fields = ['URL', 'title', 'description']
    form_class = BookmarkForm
    success_url = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super(IndexPageView, self).get_context_data(**kwargs)
    #     context['bookmark_form'] = BookmarkForm()
    #     return context
    #
    # def get(self, request, *args, **kwargs):
    #     bookmark_form = BookmarkForm()
    #     return render(request, self.template_name, {'bookmark_form':bookmark_form})

    # def post(self, request, *args, **kwargs):
    def form_valid(self, form):
        timezone.activate(settings.TIME_ZONE)
        now_t = timezone.now()
        timezone.deactivate()

        form.instance.posted_at = now_t
        form.instance.code = Bookmark.objects.allocate_code()
        user = self.request.user

        if user is not None and user.is_authenticated():
            form.instance.user = user
        else:
            form.instance.user = User.objects.get(pk=1)
#        bmk = Bookmarker()
#        bmk.save()
#        form.instance.bookmarker = bmk
        # bmk.save()
        messages.add_message(self.request, messages.SUCCESS,
                            "Your bookmark has been added!!1")
        #bookmark_form = BookmarkForm()
        # return render(request, self.template_name, {'bookmark_form':bookmark_form})
        return super(IndexPageView, self).form_valid(form)


class ClickView(views.RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'click_view_redirect'
    url = 'http://www.google.com' # if approach fails

    def get_redirect_url(self, *args, **kwargs):
        bookmark = Bookmark.objects.get(code=kwargs['code'])
#        user = request.user
#        if user is not None:
#            click = Click(bookmark=bookmark, user=user)
#        else:
        click = Click(bookmark=bookmark)
        click.set_time()
        click.save()
        self.url = bookmark.URL
        return super(ClickView, self).get_redirect_url(*args, **kwargs)


class MyRegisterView(views.CreateView):
    template_name = 'registration/register.html'
    success_url = '/'
    form_class = UserCreationForm
    model = User

    def get_context_data(self, **kwargs):
        context = super(MyRegisterView, self).get_context_data(**kwargs)
        context['bookmarker_form'] = BookmarkerForm()
        return context

    def form_valid(self, form):
#        bmkr.save()
#        form.instance.bookmarker = bmkr
        # self.object = form.save(commit=False)
        # self.object.save()

        usr = form.save()
        bookmarker_instance = BookmarkerForm(self.request.POST)
        bmkr = Bookmarker()
        bmkr.user = usr
        bmkr.save()

        password = usr.password
        usr.set_password(password)
        usr.save()


        usr = authenticate(username=usr.username,
                            password=password)
        login(self.request, usr)
        messages.add_message(self.request, messages.SUCCESS,
            "Congratulations, {}, on creating your new account! You are now logged in.".format(
                usr.username))

        # bmkr = Bookmarker()
        # bmkr.user = self.object
        # bmkr.save()

        return redirect('view_index')



class BookmarkView(views.ListView):
    template_name = 'urlmodel/bookmark.html'
    model = Bookmark
    context_object_name = 'clicks'
    bmk = None

    def get_queryset(self):
        self.bmk = Bookmark.objects.get(code=self.kwargs['code'])
        return self.bmk.click_set.all()

    def get_context_data(self, **kwargs):
        context = super(BookmarkView, self).get_context_data(**kwargs)
        context['bookmark'] = self.bmk
        return context
