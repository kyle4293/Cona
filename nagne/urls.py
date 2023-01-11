from django.urls import path

from .views import base_views, comment_views, post_views, answer_views, about_views, portfolio_views, study_views, contact_views

app_name = 'nagne'

urlpatterns = [
    # base_views.py
    path('',
         base_views.index, name='index'),
    path('<int:post_id>/',
         base_views.detail, name='detail'),

    # about_views.py
    path('about/',
         about_views.about, name='about'),

    # portfolio_views.py
    path('portfolio/',
         portfolio_views.portfolio, name='portfolio'),

    # study_views.py
    path('study/list/',
         study_views.study_list, name='study_list'),
    path('study/list/<str:study_name>',
         study_views.study_list, name='assignment_list'),
    path('study/<int:assignment_id>/',
         study_views.assignment_detail, name='assignment_detail'),
    path('assignment/create/',
         study_views.assignment_create, name='assignment_create'),
    path('assignment/modify/<int:assignment_id>/',
         study_views.assignment_modify, name='assignment_modify'),
    path('assignment/delete/<int:assignment_id>/',
         study_views.assignment_delete, name='assignment_delete'),

    # answer_views.py
    path('answer/create/<int:assignment_id>/',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),
    path('assignment/vote/<int:assignment_id>/', study_views.assignment_vote, name='assignment_vote'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),

    # contact_views.py
    path('contact/',
         contact_views.contact, name='contact'),

    # post_views.py
    path('post/list/',
         post_views.post_list, name='post_list'),
    path('post/create/',
         post_views.post_create, name='post_create'),
    path('post/modify/<int:post_id>/',
         post_views.post_modify, name='post_modify'),
    path('post/delete/<int:post_id>/',
         post_views.post_delete, name='post_delete'),

    # comment_views.py
    path('comment/create/<int:post_id>/',
         comment_views.comment_create, name='comment_create'),
    path('comment/modify/<int:comment_id>/',
         comment_views.comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>/',
         comment_views.comment_delete, name='comment_delete'),
    path('post/vote/<int:post_id>/', post_views.post_vote, name='post_vote'),
    path('comment/vote/<int:comment_id>/', comment_views.comment_vote, name='comment_vote'),
]
