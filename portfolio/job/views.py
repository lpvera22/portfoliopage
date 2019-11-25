from django.shortcuts import render

def home(request):
    return render(request,'job/index.html')

def job_details(request):
    return render(request,'job/detail.html')


