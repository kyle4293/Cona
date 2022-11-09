from django.shortcuts import render, get_object_or_404

def community(request):
    return render(request, 'nagne/community.html')