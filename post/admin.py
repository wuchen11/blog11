from django.contrib import admin
from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # 显示表格列表字段
    list_display = ('title','created',)


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)

