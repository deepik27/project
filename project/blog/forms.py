from django import forms
from blog.models import Comment

class Email_form (forms.Form):
    name=forms.CharField()
    email= forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False, widget=forms.Textarea)

class CommentForm (forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name', 'email', 'body')
