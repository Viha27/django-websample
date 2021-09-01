from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

#Dont repeat yourself = DRY

def home_page(request):
    
    template_name = "title.txt"
    template_obj  = get_template(template_name)
    rendered_string = template_obj.render()
    print(rendered_string)
    return render(request,"hello_world.html",{"title":rendered_string})
    
def home(request):
    context = {"head_title":"Hello"}
    if request.user.is_authenticated:
        context = {"head_title":"Hello World","my_list":[6,8,4,5,2]}
    return render(request,"home.html",(context))
    


def about_page(request):
    About = "About Us"
    ##return HttpResponse("<h1>About Us</h1>")    
    return render(request,"about.html",{"title":About})

def contact_page(request):
    contact = "Contact us"
    ##return HttpResponse("<h1>Contact Us</h1>")     
    return render(request,"hello_world.html",{"title":contact})  

def example_page(request):
    context  = {"title":"Example"}
    template_name = "hello_world.html"
    template_obj  = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
