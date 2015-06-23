from rest_framework import serializers
from urlmodel.models import *

class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
#    user = serializers.ReadOnlyField(source='user.username')
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    click = serializers.HyperlinkedIdentityField(view_name='click-detail')
    class Meta:
        model = Bookmark
        fields = ['URL', 'url', 'user', 'posted_at', 'title', 'description', 'click']


class ClickSerializer(serializers.HyperlinkedModelSerializer):
#    user = serializers.ReadOnlyField(source='user.username')
    user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    bookmark = serializers.HyperlinkedIdentityField(view_name='bookmark-detail')
    class Meta:
        model = Click
        fields = ['clicked_at', 'bookmark', 'user']
