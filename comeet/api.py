from tastypie.resources import ModelResource
from tastypie.constants import ALL
from models import Rank


class RankResource(ModelResource):
    class Meta:
        queryset = Rank.objects.all()
        resource_name = 'rank'
        filtering = { "title" : ALL } #/ All filters are permitted like : { "title" : "contains" }
        #for http://192.168.56.101:8080/ranks/api/rank/?format=json&title__contains=Mike