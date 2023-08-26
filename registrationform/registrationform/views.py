from django.shortcuts import render

def function(request):
    return render(request, 'admin/index.html')