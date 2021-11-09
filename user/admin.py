from django.contrib import admin

from blogapp.models import Post
from user.models import *
# Register your models here.
# admin.site.register(content)
class Media:
    js = (
        '/static/kindeditor/kindeditor-all-min.js',
        '/static/kindeditor/kindeditor-all.js',
        '/static/kindeditor/config.js'
    )
admin.site.register(BlogUser)
admin.site.register(EmailVerifyRecord)


