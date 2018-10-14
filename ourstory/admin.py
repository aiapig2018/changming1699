from django.contrib import admin
from ourstory.models import Article,Category,Tag
# Register your models here.
 
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')
 
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)