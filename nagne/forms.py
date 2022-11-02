from django import forms
from nagne.models import Post, Answer

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'content']

        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변',
        }