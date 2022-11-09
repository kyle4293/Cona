from django.shortcuts import render, get_object_or_404

def contact(request):
    return render(request, 'nagne/contact.html')