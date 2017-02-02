from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext

# Create your views here.

def login(request):
	if 'user' in request.session:
		return HttpResponseRedirect('/loggedin/')
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html',c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user 	 = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		request.session['user'] = user.username
		return HttpResponseRedirect('/loggedin/')
	else:
		context = {
			'error'	:	'Error'
		}
		return render(request, 'login.html', context)

def loggedin(request):
	if 'user' in request.session:
		user = request.session['user']
		return render_to_response('loggedin.html',
								{ 	'full_name' 	: request.user.username,
								}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login/')

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	context = {
		'logout' : 'Successful'
	}
	return render(request, 'login.html', context)

def check(request):
	if 'user' in request.session:
		return HttpResponseRedirect('/loggedin/')
	else:
		return HttpResponseRedirect('/login/')