from django.contrib import admin
from blogapp.models import *
# # Register your models here.
#
admin.site.register([FriendlyLink,Comment,Tags,BlogCategory,Banner])

class Media:
    js = (
        '/static/kindeditor/kindeditor-all-min.js',
        '/static/kindeditor/kindeditor-all.js',
        '/static/kindeditor/config.js'
    )


admin.site.register(Post)