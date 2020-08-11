from django.contrib import admin
from .models import Users, Article, Comment, Recomment, Ads
# Register your models here.

admin.site.register(Article)
admin.site.register(Users)
admin.site.register(Comment)
admin.site.register(Ads)
admin.site.register(Recomment)