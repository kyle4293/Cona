from django.shortcuts import render, get_object_or_404
from ..models import Post
import logging
logger = logging.getLogger('nagne')

def index(request):
    return render(request, 'base.html')


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'nagne/post_detail.html', context)