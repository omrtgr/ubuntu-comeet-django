from tastypie.resources import ModelResource
from tastypie.constants import ALL
from models import Article


class ArticleResource(ModelResource):
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'
        filtering = { "title" : ALL } #/ All filters are permitted like : { "title" : "contains" }
        #for http://192.168.56.101:8080/articles/api/article/?format=json&title__contains=Mike