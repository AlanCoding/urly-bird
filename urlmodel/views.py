from .models import Bookmark, Bookmarker, Tag, Click
from .forms import BookmarkForm, BookmarkerForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import View, RedirectView, ListView, \
                            DetailView, DeleteView, UpdateView


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

    def get(self, request):
        bookmark_form = BookmarkForm()
        return render(request, "index.html", {'bookmark_form':bookmark_form})

    def post(self, request):
        bmk = Bookmark.create_bookmark()
        messages.add_message(request, messages.SUCCESS,
                            "Your bookmark has been added!!1")
        return render(request, "index.html")


class ClickView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'click_view_redirect'
    url = 'http://www.google.com' # if approach fails

    def get_redirect_url(self, *args, **kwargs):
        bookmark = Bookmark.objects.get(pk=kwargs['code'])
        user = request.user
        if user is not None:
            click = Click(bookmark=bookmark, user=user)
        else:
            click = Click(bookmark=bookmark)
        click.set_time()
        click.save()
        self.url = bookmark.url
        return super(ClickView, self).get_redirect_url(*args, **kwargs)


class BookmarkView(DetailView):
    template_name = 'urlmodel/bookmark.html'
    model = Bookmark
    context_object_name = 'bookmark'

    def get_context_data(self, **kwargs):
        context = super(BookmarkView, self).get_context_data(**kwargs)
        context['bookmark'] = Bookmark.objects.get(code=kwargs['code'])
        return context
