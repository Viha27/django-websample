 
from .views import blog_post_create_view, blog_post_delete_view, blog_post_detail_page, blog_post_list_view, blog_post_retrieve_view, blog_post_update_view

from django.urls import path, re_path

urlpatterns = [
    path('',blog_post_list_view),
    path('<slug:slug>/',blog_post_retrieve_view),
    path('<slug:slug>/edit',blog_post_update_view),
    path('<slug:slug>/delete',blog_post_delete_view),
   
]

 
