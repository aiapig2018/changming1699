from django.contrib import admin
from .models import Post, Category, Tag
from django_summernote.admin import SummernoteModelAdmin

# 注册产品页模型类
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'image', 'category', 'author']


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)  # 给content字段添加富文本



admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)



