from django.shortcuts import render_to_response
from comeet.models import Rank
from django.http import HttpResponse
from forms	import RankForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone

def ranks(request):
	language= 'en-gb'
	session_language = 'en-gb'

	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']

	if 'lang' in request.session:
		session_language = request.session['lang']

	args = {}
	args.update(csrf(request))

	args['ranks'] = Rank.objects.all()
	args['language'] =language
	args['session_language'] = session_language
	 
	return render_to_response('ranks.html', args)



def rank(request, rank_id=1):
	return render_to_response('rank.html',
							{'rank': Rank.objects.get(id=rank_id)})


def language(request, language='en-gb'):
	response = HttpResponse("setting language to %s" % language)
	response.set_cookie('lang', language)
	request.session['lang'] = language
	return response

def create(request):
	if request.POST:
		form = RankForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			
			return HttpResponseRedirect('/ranks/all')
	else:
		form = RankForm()
	args = {}
	args.update(csrf(request))

	args['form'] = form
	return render_to_response('create_rank.html', args)

def like_rank(request, rank_id):
	if rank_id:
		a = Rank.objects.get(id=rank_id)
		a.likes += 1
		a.save()

	return HttpResponseRedirect('/ranks/get/%s' % rank_id)


def add_comment(request, rank_id):
	a = Rank.objects.get(id=rank_id)

	if request.method == "POST":
		f = CommentForm(request.POST)
		if f.is_valid():
			c = f.save(commit=False)
			c.pub_date = timezone.now()
			c.rank = a
			c.save()
			return HttpResponseRedirect('/ranks/get/%s' % rank_id)
	else:
		f = CommentForm()

	args = {}
	args.update(csrf(request))

	args['rank'] = a
	args['form'] = f

	return render_to_response('add_comment.html', args)

def search_titles(request):
	if request.method == "POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''
	#Django filter model function- takes arguments as parts of the filter. 
	#The title member variable is assosiated with the object, 
	#"filter 'title' where is contians 'search_text' / Like 'like' command
	ranks = Rank.objects.filter(title__contains=search_text)
	return render_to_response('ajax_rank_search.html', {'ranks' : ranks})



