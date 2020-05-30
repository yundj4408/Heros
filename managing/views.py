from django.shortcuts import render, redirect

# Create your views here.
def Notice_all(request):
    return render(request, 'managing/Notice.html')

def FAQ_all(request):
    return render(request, 'managing/FAQ.html')