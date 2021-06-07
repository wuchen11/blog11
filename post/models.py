from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
# 分类表
class Category(models.Model):
    cname = models.CharField(max_length=30, unique=True, verbose_name='类别名称')

    class Meta:
        db_table = 't_category'
        verbose_name_plural = u'类别'

    def __str__(self):
        return u'类别:%s' % self.cname


# 标签表  多对多
class Tag(models.Model):
    tname = models.CharField(max_length=30, unique=True, verbose_name='标签名称')

    class Meta:
        db_table = 't_tag'
        verbose_name_plural = u'标签'

    def __str__(self):
        return u'Tag:%s' % self.tname


# 文章
class Post(models.Model):
    title = models.CharField(max_length=80, unique=True, verbose_name='标题')
    # null数据库不为空,blank表单不为空,RichTextUploadingField使用富文本
    content = RichTextUploadingField(null=True, blank=True, verbose_name='内容')
    created = models.DateTimeField(auto_created=True, verbose_name='创建日期')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    class Meta:
        db_table = 't_Post'
        verbose_name_plural = u'文章'

    def __str__(self):
        return u'Post:%s' % self.title
