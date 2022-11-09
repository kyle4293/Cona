from django.urls import path

from .views import base_views, post_views, answer_views, about_views, portfolio_views, community_views, contact_views

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
    #portfolio_views.py
    path('portfolio/',
         portfolio_views.portfolio, name='portfolio'),
    #community_views.py
    path('community/',
         community_views.community, name='community'),
    #contact_views.py
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

    # answer_views.py
    path('answer/create/<int:post_id>/',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),
    path('post/vote/<int:post_id>/', post_views.post_vote, name='post_vote'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),
]
