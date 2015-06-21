from django import forms
from django.contrib.auth.models import User
from .models import Bookmark, Bookmarker, Click
# Profile

class BookmarkForm(forms.ModelForm):

    class Meta:
        model = Bookmark
        fields = ('URL', 'title', 'description',)
#        blank = True

class BookmarkerForm(forms.ModelForm):

    class Meta:
        model = Bookmarker
        fields = ('age', 'gender')
