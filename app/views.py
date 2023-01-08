from django.shortcuts import render

# Create your views here.
def latest(request):
    return render(request,'latest.html')
