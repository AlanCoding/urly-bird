from .models import Bookmark, Bookmarker, Tag, Click
from .forms import BookmarkForm, BookmarkerForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import View, RedirectView, ListView, \
                            DetailView, DeleteView, UpdateView
from django.conf import settings

from django.utils import timezone
import pytz

class BookmarkerView(ListView):
    template_name = 'urlmodel/bookmarker.html'
#    model = Bookmark
    paginate_by = 20
    context_object_name = 'bookmarks'
    bookmarker = None

    def dispatch(self, *args, **kwargs):
        self.bookmarker = Bookmarker.objects.get(pk=self.kwargs['bookmarker_id'])
        return super(GenreView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.bookmarker.bookmark_set.order_by('-posted_at')

    def get_context_data(self, **kwargs):
        context = super(BookmarkerView, self).get_context_data(**kwargs)
        context['bookmarker'] = self.bookmarker
        return context


class IndexView(View):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['bookmark_form'] = BookmarkForm()
        return context

    def get(self, request, *args, **kwargs):
        bookmark_form = BookmarkForm()
        return render(request, self.template_name, {'bookmark_form':bookmark_form})

    def post(self, request, *args, **kwargs):
        timezone.activate(settings.TIME_ZONE)
        now_t = timezone.now()
        timezone.deactivate()

        bmk = Bookmark(URL=request.POST.get('URL'), posted_at=now_t,
                        title=request.POST.get('title'),
                        description=request.POST.get('description'))
        bmk.code = Bookmark.objects.allocate_code()
        bmk.save()

        messages.add_message(request, messages.SUCCESS,
                            "Your bookmark has been added!!1")
        bookmark_form = BookmarkForm()
        return render(request, self.template_name, {'bookmark_form':bookmark_form})


class ClickView(RedirectView):
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


class BookmarkView(DetailView):
    template_name = 'urlmodel/bookmark.html'
    model = Bookmark
    context_object_name = 'bookmark'

    def get_context_data(self, **kwargs):
        context = super(BookmarkView, self).get_context_data(**kwargs)
        context['bookmark'] = Bookmark.objects.get(code=kwargs['code'])
        return context
