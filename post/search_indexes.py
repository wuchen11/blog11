from .models import Post
from haystack import indexes


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text  = indexes.CharField(document=True, use_template=True)
    #给title,content设置索引
    title = indexes.NgramField(model_attr='title')
    content = indexes.NgramField(model_attr='content')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        #确定在建立索引时有些记录被索引，这里我们简单地返回所有记录
        return self.get_model().objects.order_by('-created')