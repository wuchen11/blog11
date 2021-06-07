import math
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views import View
from post.models import Post


class Index_view(View):

    def get(self, request, num=1):
        # 获取页数
        # num = request.GET.get('num',1)
        num = int(num)

        postList = Post.objects.all().order_by('-created')

        # 创建分页器对象
        pageObj = Paginator(postList, 2)

        # 获取当前页数据
        perPage = pageObj.page(num)
        # try:
        #     perpage_data = pageObj.page(num)
        # except PageNotAnInteger:
        #     # 返回第一页的数据
        #     perpage_data = pageObj.page(1)
        # except EmptyPage:
        #     # 返回最后一页的数据
        #     perpage_data = pageObj.page(pageObj.num_pages)

        # 每页开始页码,ceil()取整数
        begin = (num - int(math.ceil(10.0 / 2)))
        if begin < 1:
            begin = 1

        # 每页结束页码
        end = begin + 9
        if end > pageObj.num_pages:
            end = pageObj.num_pages

        if end <= 10:
            begin = 1
        else:
            begin = end - 9

        pageList = range(begin, end + 1)
        #
        return render(request, 'index.html', {'postList': perPage, 'pageList': pageList, 'currentNum': num})


# 详情页(阅读全文)
class Post_detail(View):
    def get(self, request, postid):
        postid = int(postid)

        # 根据postid查询详情
        post = Post.objects.get(id=postid)

        return render(request, 'detail.html', {'post': post})


# 关于
class Footer(View):
    def get(self, request):
        return render(request, 'footer.html')


# 根据类别id查询所有帖子
def queruPostByCreated(request, cid):
    postList = Post.objects.filter(category__id=cid)

    return render(request, 'article.html', {'postList': postList})


# 根据发帖时间查询所有帖子
def queryPostByCreated(request, year, month):
    postList = Post.objects.filter(created__year=year, created__month=month)
    return render(request, 'article.html', {'postList': postList})
