from django import forms
from nagne.models import Post, Comment, Assignment, Answer

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'content']

        labels = {
            'subject': '제목',
            'content': '내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '답변',
        }

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['subject', 'content', 'study_name']

        labels = {
            'study_name' : '스터디',
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