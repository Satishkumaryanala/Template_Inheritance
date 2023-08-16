from django.shortcuts import render

# Create your views here.

def child(request):
    return render(request,'child.html')