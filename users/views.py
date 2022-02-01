from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
	"""Register new user"""
	if request.method != 'POST':
		#display blank registration form
		form = UserCreationForm()
	else:
		#process complete form
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			#log in user and redirect to home page
			login(request, new_user)
			return redirect('student_posts:home')

	#display a blank or invalid form
	context = {'form': form}
	return render(request,'registration/register.html', context)