from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import PostCreationForm
from .models import Post

# Create your views here.

# posts=[
#     {
#         "id":1,
#         "title":"Attack on Titan",
#         "author":"Isayama"
#     },
#     {
#         "id":2,
#         "title":"One Punch Man",
#         "author":"ONE"
#     },
#     {
#         "id":3,
#         "title":"Berserk",
#         "author":"Miura"
#     }
# ]



def index(request:HttpRequest):
    name = request.GET.get("name") or "World"   
    
    posts = Post.objects.all()
    
    context = {
        "name":name,
        "posts":posts,
        "title":"Home Page",
    }
    
    return render(request,'index.html', context)


def about(request):
    
    context = {
        "title":"About Page",
    }
    return render(request,'about.html', context)

def services(request):
    context = {
        "title":"Services Page",
    }
    return render(request,'services.html', context)


def greet(request:HttpRequest):    
    name = request.GET.get("name") or "World"   
    return HttpResponse(f"Hello {name}")


# def return_all_posts(request:HttpRequest):
#     return HttpResponse(str(posts))


# def return_one_post(request:HttpRequest, post_id):
#     for post in posts:
#         if post["id"] == post_id:          
#             return HttpResponse(str(post))
        
    
def create_post(request):
    form = PostCreationForm()
    
    
    
    if request.method =="POST":
        
        form = PostCreationForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
        
        
        # data = request.POST
        # title = data["title"]
        # content = data["content"]
        # author = data["author"]
        
        # new_post = Post(
        #     title=title,
        #     content=content,
        #     author=author
        # )
        
        # new_post.save()
        
            return redirect('posts_home')
        
    context = {
        'form':form
    }
    
    return render(request,'createpost.html',context)


def post_detail(request,post_id):
    
    post = Post.objects.get(pk=post_id)
    
    
    
    context={
        'post':post
    }
    return render(request,'post_detail.html', context)

def update_post(request,post_id):
    context={}
    return render(request,'update.html', context)