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
import .serializer as s

# Create your views here.
class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = s.BookmarkSerializer


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
        return super(GenreView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.bookmarker.bookmark_set.order_by('-posted_at')

    def get_context_data(self, **kwargs):
        context = super(BookmarkerView, self).get_context_data(**kwargs)
        context['bookmarker'] = self.bookmarker
        return context


class IndexPageView(views.CreateView):
    template_name = 'index.html'
    model = Bookmark
    # fields = ['URL', 'title', 'description']
    form_class = BookmarkForm

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
        bmk = Bookmarker()
        bmk.save()
        form.instance.bookmarker = bmk
        # bmk.save()

        messages.add_message(request, messages.SUCCESS,
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

        return redirect('view_index')



class BookmarkView(views.DetailView):
    template_name = 'urlmodel/bookmark.html'
    model = Bookmark
    context_object_name = 'bookmark'

    def get_context_data(self, **kwargs):
        context = super(BookmarkView, self).get_context_data(**kwargs)
        context['bookmark'] = Bookmark.objects.get(code=kwargs['code'])
        return context
