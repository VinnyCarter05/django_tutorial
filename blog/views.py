from django.shortcuts import render

posts = [
    {
        'author': 'Vinny Carter',
        'title': 'Blog Post 1',
        'content': 'content 1',
        'date_posted': 'Jan 1, 2021'
    },
    {
        'author': 'KLow',
        'title': 'Blog Post 2',
        'content': 'content 2',
        'date_posted': 'Jan 6, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})