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
from rest_framework import viewsets
from .serializer import *

# Create your views here.
class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

class ClickViewSet(viewsets.ModelViewSet):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer

class UserBmkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
    def get_queryset(self, user_id):
        pass


class BmkClickViewSet(viewsets.ModelViewSet):
    serializer_class = ClickSerializer
    queryset = Click.objects.all()
    def get_queryset(self, bmk_id):
        pass




class BookmarkerView(views.ListView):
    template_name = 'urlmodel/bookmarker.html'
#    model = Bookmark
    paginate_by = 20
    context_object_name = 'bookmarks'
    bookmarker = None

    def dispatch(self, *args, **kwargs):
        if 'bookmarker_id' in self.kwargs:
            self.bookmarker = Bookmarker.objects.get(pk=self.kwargs['bookmarker_id'])
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

        # bmk = Bookmark(URL=request.POST.get('URL'), posted_at=now_t,
        #                 title=request.POST.get('title'),
        #                 description=request.POST.get('description'))
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
        bmkr = Bookmarker()
        bmkr.user = usr
        bmkr.save()

        password = usr.password
        usr.set_password(password)
        usr.save()


        usr = authenticate(username=usr.username,
                            password=password)
        login(self.request, usr)
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Congratulations, {}, on creating your new account! You are now logged in.".format(
                usr.username))

        # bmkr = Bookmarker()
        # bmkr.user = self.object
        # bmkr.save()

        return redirect('view_index')



class BookmarkView(views.DetailView):
    template_name = 'urlmodel/bookmark.html'
    model = Bookmark
    context_object_name = 'bookmark'

    def get_context_data(self, **kwargs):
        context = super(BookmarkView, self).get_context_data(**kwargs)
        context['bookmark'] = Bookmark.objects.get(code=kwargs['code'])
        return context
