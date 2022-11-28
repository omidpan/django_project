from django.shortcuts import render
# from django.http import HttpResponse
posts =[
    {'author':'Leo Page',
    'title':'blog post 1',
    'content':'First post content',
    'date_posted':'Augest 27 , 2022'
    },
    {'author':'Ross Stepto',
    'title':'blog post 2',
    'content':'Second post content',
    'date_posted':'Augest 28 , 2022'
    } 

]
def home(request):
    context={'posts':posts}
    return render(request,'blogs/home.html',context)

def about(request):
    return render (request,'blogs/about.html',{'title':'about'})