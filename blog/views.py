from typing import ContextManager
from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import BlogPost

#GET -> 1 object
#filter -> [] objects

def blog_post_detail_page(request,slug):
    #print(post_id.__class__)
    print("Django says", request.method,request.user,request.path)

    ''' querySet = BlogPost.objects.filter(slug=slug)
    if querySet.count() ==0:
        raise Http404
    obj = querySet.first()    ''' 
    try:
        obj = get_object_or_404(BlogPost,slug=slug)
    except ValueError:
        raise Http404

    """ try:
        obj = BlogPost.objects.get(id=int(post_id) )
    except BlogPost.DoesNotExist:
        raise Http404
    except ValueError:
        raise Http404  """       
    template_name = 'blog_post_detail.html'
    context = {"object":obj}
    return render(request, template_name,context)


# CRUD - Create Retrieve Update Delete
# GET -> Retrieve / List
# POST -> Create / Update / Delete 

def blog_post_list_view(request):
    #qs = BlogPost.objects.filter(title='Hello World')
    #query set ---> list of python objects
    qs = BlogPost.objects.all()
    template_name = 'blog_post_list.html'
    context = {'object_list':qs}
    return render(request,template_name,context)

def blog_post_create_view(request):
    template_name = 'blog_post_create.html'
    context = {'form':None}
    return render(request,template_name,context) 

def blog_post_retrieve_view(request,slug):
    #i object -> detail view
    try:
        obj = get_object_or_404(BlogPost,slug=slug)
    except ValueError:
        raise Http404
    template_name = 'blog_post_detail2.html'
    context = {"object":obj}
    return render(request, template_name,context) 

def blog_post_update_view(request,slug):
    
    obj = get_object_or_404(BlogPost,slug=slug)
    template_name = 'blog_post_update.html'
    context = {"object":obj,'form':None}
    return render(request, template_name,context)  

def blog_post_delete_view(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    template_name = 'blog_post_delete.html'
    context = {"object":obj}
    return render(request, template_name,context) 
