from django.contrib import admin
from .models import *

# Register your models here.
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'URL', 'code', "posted_at", "title", "description"]

class BookmarkerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'age', 'gender']

class TagAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'text']

class ClickAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'user', 'clicked_at']

# custom user
# from django.contrib.auth.admin import UserAdmin

# UserAdmin.list_display += ('bookmarker',)  # don't forget the commas
# UserAdmin.list_filter += ('bookmarker',)
# UserAdmin.fieldsets += ('bookmarker',)


# Register your models here.
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Bookmarker, BookmarkerAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Click, ClickAdmin)
