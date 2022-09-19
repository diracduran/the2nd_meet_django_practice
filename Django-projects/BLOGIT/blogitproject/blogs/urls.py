from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from blogs import views


urlpatterns = [
    path('', views.show_blog, name='show_blog'),
    path('blog/<slug:author>/<slug:slug>/view', views.single_blog, name='single_blog'),
    path('blog/create', views.create_blog, name='create_blog'),
    path('blog/<slug:author>/<slug:slug>/edit', views.edit_blog, name='edit_blog'),
    path('blog/<slug:author>/<slug:slug>/delete', views.delete_blog, name='delete_blog'),
    path('blog/<slug:author>/<slug:slug>/leave_comment_to_blog', views.leave_comment_to_blog, name='leave_comment_to_blog'),
    path('blog/<slug:author>/<slug:slug>/comment/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
    path('blog/<slug:author>/<slug:slug>/add-or-remove-like', views.add_or_remove_like_to_blog, name='add_or_remove_like_to_blog'),
    path('blog/add-or-remove-like-ajax', views.add_or_remove_like_ajax, name='add_or_remove_like_ajax'),
]