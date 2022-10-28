from django.urls import path

from .views import base_views, assignment_views, answer_views

app_name = 'nagne'

urlpatterns = [
    # base_views.py
    path('',
         base_views.index, name='index'),
    path('<int:assignment_id>/',
         base_views.detail, name='detail'),

    # assignment_views.py
    path('assignment/create/',
         assignment_views.assignment_create, name='assignment_create'),
    path('assignment/modify/<int:assignment_id>/',
         assignment_views.assignment_modify, name='assignment_modify'),
    path('assignment/delete/<int:assignment_id>/',
         assignment_views.assignment_delete, name='assignment_delete'),

    # answer_views.py
    path('answer/create/<int:assignment_id>/',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),
    path('assignment/vote/<int:assignment_id>/', assignment_views.assignment_vote, name='assignment_vote'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),
]
