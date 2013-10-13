from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^articles/', include('article.urls')),
	(r'^ranks/', include('comeet.urls')),
	url(r'^admin/', include(admin.site.urls)),

	# user auth urls
	url(r'^accounts/login/$', 'django_first.views.login'),
	url(r'^accounts/auth/$', 'django_first.views.auth_view'),
	url(r'^accounts/logout/$', 'django_first.views.logout'),
	url(r'^accounts/loggedin/$', 'django_first.views.loggedin'),
	url(r'^accounts/invalid/$', 'django_first.views.invalid_login'),
	url(r'^accounts/register/$', 'django_first.views.register_user'),
	url(r'^accounts/register_success/$', 'django_first.views.register_success'),
	






)


