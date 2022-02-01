from django import forms 

from .models import Post,Exp

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','slug','content','status']

class ExpForm(forms.ModelForm):
	class Meta:
		model = Exp
		fields = ['company','slug','content','role','status']
