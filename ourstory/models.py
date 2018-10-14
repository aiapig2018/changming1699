from __future__ import unicode_literals
from django.db import models
from django.utils.six import python_2_unicode_compatible
from ckeditor_uploader.fields import RichTextUploadingField
 
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=70)
    #返回str类型
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



 
class Article(models.Model):
    title = models.CharField(u"博客标题",max_length = 100)        #博客标题
    category = models.CharField(u"博客标签",max_length = 50,blank = True)       #博客标签
    pub_date = models.DateTimeField(u"发布日期",auto_now_add = True,editable=True)       #博客发布日期
    update_time = models.DateTimeField(u'更新时间',auto_now=True,null=True)
    content = models.TextField(blank=True, null=True)  # 博客文章正文
    image = models.ImageField("故事背景图",upload_to='ourstory/%Y/%m/%d', db_index=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)

 
    def __unicode__(self):
        return self.title
 
    class Meta:     #按时间下降排序
        ordering = ['-pub_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"





