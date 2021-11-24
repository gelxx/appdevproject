from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
# Create your views here.

def register(request):
	if request.user.is_authenticated:
		return redirect('cyberinscriber:myhome_view')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
			user = form.cleaned_data.get('username')
			messages.success(request,'Account was created for ' + user)

			return redirect('cyberinscriber:login_view')

	context = {
		'form':form
	}
	return render(request,'users/register.html',context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('cyberinscriber:myhome_view')
	else:
		if request.method =='POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request,user)
				return redirect('cyberinscriber:myhome_view')
		else:
			#messages.info(request,'Username or Password is incorrect!')
			#messages.info(request)
			return render(request,'users/log_in.html',{})

			context ={}
			return render(request,'users/log_in.html',context)

	
@login_required(login_url = 'cyberinscriber:login_view')
def logOutUser(request):
	logout(request)
	return redirect('cyberinscriber:login_view')


def LandingView(request):
		return render(request, 'landingpage.html',{} )


@login_required(login_url = 'cyberinscriber:login_view')
def MyHomeView(request):
	notes = Notes.objects.all()
	context = {
		'cNotes': notes
	}
	return render(request,'myhome.html', context)



