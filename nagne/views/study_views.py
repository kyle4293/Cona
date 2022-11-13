from django.shortcuts import render, get_object_or_404

def study(request):
    return render(request, 'nagne/study.html')