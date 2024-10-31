import threading

from django.db import transaction
from django.shortcuts import render, redirect
import datetime
from .models import Blog
# Create your views here.



def index(request):
    print("Main Thread Id-", threading.get_ident())
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        print(f"1st print statement in View  before saving the instance started at: {datetime.datetime.now().strftime('%H:%M:%S')}")
        try:
            with transaction.atomic():
                blog_instance = Blog.objects.create(
                title=title,
                body=body
                )

        except Exception as e:
            blog =Blog.objects.filter(title = title)
            print("Checking if the blog is saved in database ?",blog.exists())
            print(e)

        print(f"2nd print statement in View  after saving the instance is saved started at: ended at: {datetime.datetime.now().strftime('%H:%M:%S')}")
        return redirect('blog_list')
    return render(request,'app/home.html')

def blog_list(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'app/blog_list.html', context)