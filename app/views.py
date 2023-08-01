from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'name':'subbu','age':23,'hobbies':['cricket']}
    return render(request,'loop.html',context=d)