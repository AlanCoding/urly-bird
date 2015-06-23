from rest_framework import serializers
from urlmodel.models import *

class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['URL', 'url', 'posted_at', 'title', 'description']
