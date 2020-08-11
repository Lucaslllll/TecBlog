from django import forms

from .models import Users, Article, Comment, Recomment, Ads


class UsersForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = '__all__'

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = '__all__'

class RecommentForm(forms.ModelForm):
	class Meta:
		model = Recomment
		fields = '__all__'
		