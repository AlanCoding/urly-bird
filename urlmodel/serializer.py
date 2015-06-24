from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.reverse import reverse
from urlmodel.models import *

class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
#    user = serializers.ReadOnlyField(source='user.username')
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    # user = serializers.HyperlinkedIdentityField(view_name='user-detail')
    # click = serializers.HyperlinkedIdentityField(view_name='click-detail')
    # user = serializers.HyperlinkedIdentityField(view_name='user-detail')
    # ctz = 2
    bookmarker = serializers.HyperlinkedIdentityField(view_name='bookmarker-detail')
    _links = SerializerMethodField()

    def get__links(self, obj):
        links = {
            "clicks": reverse('bookmark-click', kwargs=dict(bmk_id=obj.pk),
                              request=self.context.get('request')), }
        return links

    class Meta:
        model = Bookmark
        fields = ['URL', 'url', 'user', 'bookmarker', 'posted_at', 'title',
                    'description', 'total_clicks', 'click_set', '_links']

    # def get_validation_exclusions(self):
    #     exclusions = super(BookmarkerSerializer, self).get_validation_exclusions()
    #     return exclusions + ['posted_at']

    # def create(self):


class BookmarkerSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField( read_only=True)
    _links = SerializerMethodField()

    def get__links(self, obj):
        links = {
            "bookmarks": reverse('bookmarker-bookmark', kwargs=dict(bmkr_id=obj.user.pk),
                              request=self.context.get('request')), }
        return links

    class Meta:
        model = Bookmarker
        fields = ['age', 'gender', 'user', '_links','total_bookmarks', 'total_clicks']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'click_set']

class ClickSerializer(serializers.HyperlinkedModelSerializer):
#    user = serializers.ReadOnlyField(source='user.username')
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    # user = serializers.HyperlinkedIdentityField(view_name='user-detail')
    bookmark = serializers.HyperlinkedIdentityField(view_name='bookmark-detail')
    class Meta:
        model = Click
        fields = ['clicked_at', 'bookmark', 'user']
