from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *


from .filters import VaccineFilter
from .forms import VaccineForm, RespondentForm, CreateUserForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'nurse/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'nurse/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')






def home(request):
	
	respondents = Respondent.objects.all()
	vaccines = Vaccine.objects.all()
	myFilter = VaccineFilter(request.GET, queryset=Vaccine.objects.all())
	vaccines = myFilter.qs 
	
	context = {'respondents':respondents, 'vaccines':vaccines, 'myFilter':myFilter}
	return render(request, 'nurse/list.html', context)


def form(request):
	form = RespondentForm()
	if request.method == 'POST':
		form = RespondentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('nextform')
	context = {'form':form}
	return render(request, 'nurse/form.html', context)

def nextform(request):
	form = VaccineForm()
	if request.method == 'POST':
		form = VaccineForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'nurse/form2.html', context)

	

def respondent(request, pk_test):
	respondent = Respondent.objects.get(id=pk_test)
	vaccine = respondent.vaccine_set.all()
	context = {'respondent':respondent, 'vaccine':vaccine}
	
	return render(request, 'nurse/profile.html', context)
@login_required(login_url='login')
def updateRespondent(request, pk):

	respondent = Respondent.objects.get(id=pk)
	form = RespondentForm(instance=respondent)

	if request.method == 'POST':
		form = RespondentForm(request.POST, instance=respondent)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'nurse/form.html', context)
@login_required(login_url='login')
def updateVaccine(request, pk):

	vaccine = Vaccine.objects.get(id=pk)
	form = VaccineForm(instance=vaccine)

	if request.method == 'POST':
		form = VaccineForm(request.POST, instance=vaccine)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'nurse/form2.html', context)

@login_required(login_url='login')
def deleteVaccine(request, pk):
	vaccine = Vaccine.objects.get(id=pk)
	if request.method == "POST":
		vaccine.delete()
		return redirect('/')

	context = {'item':vaccine}
	return render(request, 'nurse/delete.html', context)