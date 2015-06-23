from rest_framework import serializers
from urlmodel.models import *

class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Bookmark
        fields = ['URL', 'url', 'user', 'posted_at', 'title', 'description']
