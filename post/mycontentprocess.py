from django.db.models import *

from post.models import Post


def getRightInfo(request):
    # 1.右侧分类
    # category__cname是标签名,category是ID,c是数量
    r_catepose = Post.objects.values('category__cname', 'category').annotate(c=Count("*")).order_by('-c')
    # 2.右侧最近文章
    r_near = Post.objects.all().order_by('-created')[:3]

    # 3.右侧归档日期
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("select created,count('*') c from t_post GROUP BY DATE_FORMAT(created,'%Y-%m') order by created desc,c desc;")
    r_fill_post = cursor.fetchall

    return {'r_catepose': r_catepose, 'r_near': r_near, 'r_fill_post': r_fill_post}
