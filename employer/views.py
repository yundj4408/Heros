from django.shortcuts import render, redirect

# Create your views here.
def employer_all(request):
    return render(request, 'employer/employer_list.html')