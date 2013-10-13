from django.conf.urls import patterns, include, url
from api import RankResource

rank_resource = RankResource()

urlpatterns = patterns('',
	url(r'^all/$', 'comeet.views.ranks'),
	url(r'^get/(?P<rank_id>\d+)/$', 'comeet.views.rank'),
	url(r'^language/(?P<language>[a-z\-]+)/$', 'comeet.views.language'),
	url(r'^create/$', 'comeet.views.create'),
	url(r'^like/(?P<rank_id>\d+)/$', 'comeet.views.like_rank'),
	
	url(r'^search/$', 'comeet.views.search_titles'),
	url(r'^api/', include(rank_resource.urls)),



	)

