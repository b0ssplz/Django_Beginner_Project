from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import PostCreationForm
from .models import Post
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator



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

class HomePageView(View):
    
    template_name = "index.html"
    
    def get(self, request):
        
        posts = Post.objects.all()  
        
        paginator=Paginator(posts,3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
    
        context = {
            "posts":page_obj,
            "title":"Home Page",
        }
        return render(request,self.template_name, context)



# def index(request:HttpRequest):
#     name = request.GET.get("name") or "World"   
    
#     posts = Post.objects.all()
    
#     context = {
#         "name":name,
#         "posts":posts,
#         "title":"Home Page",
#     }
    
#     return render(request,'index.html', context)


class AboutView(HomePageView):
    
    template_name = "about.html"
    
    def get(self, request):
        context = {
            "title":"About Page",
        }
        return render(request,self.template_name, context)           
        

# def about(request):
    
#     context = {
#         "title":"About Page",
#     }
#     return render(request,'about.html', context)

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
  
  
@method_decorator(login_required,'dispatch')
class CreatePostView(View):
    
    template_name = 'createpost.html'
    form_class = PostCreationForm
    
    # @method_decorator(login_required)
    # def dispatch(self, *args,**kwargs):
    #     return super().dispatch(*args,**kwargs)
        
    
    def get(self, request):
        #form = self.form_class(initial=self.initial_values)
        context = {
            'form':self.form_class
        }
            
        return render(request,self.template_name,context)
    
    def post(self, request):
        form = self.form_class(request.POST, request.FILES) 
           
        if form.is_valid():
            form.save()
            return redirect('posts_home')
            
      
# @login_required
# def create_post(request):
#     form = PostCreationForm()
    
    
    
#     if request.method =="POST":
        
#         form = PostCreationForm(request.POST, request.FILES)
        
#         if form.is_valid():
#             form.save()
        
        
#         # data = request.POST
#         # title = data["title"]
#         # content = data["content"]
#         # author = data["author"]
        
#         # new_post = Post(
#         #     title=title,
#         #     content=content,
#         #     author=author
#         # )
        
#         # new_post.save()
        
#             return redirect('posts_home')
        
#     context = {
#         'form':form
#     }
    
#     return render(request,'createpost.html',context)





def post_detail(request,post_id):
    
    post = Post.objects.get(pk=post_id)
    context={
        'post':post
    }
    
    return render(request,'post_detail.html', context)





@login_required
def update_post(request,post_id):
    
    post_to_update = Post.objects.get(pk=post_id)
    form = PostCreationForm(instance=post_to_update)
    
    if request.method == "POST":
        form = PostCreationForm(instance = post_to_update,data=request.POST, files = request.FILES)
        
        
        if form.is_valid():
            form.save()
            
            return redirect('posts_home')
    
    context={
        'form':form
    }
    return render(request,'update.html', context)