from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
urlpatterns = [
    # path('', views.home , name="blog_home"),
    path('', PostListView.as_view() , name="blog_home"),
    path('about/', views.about , name="blog_about"),
    path('post/new/', PostCreateView.as_view(), name="post_create"),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<pk>/',PostDetailView.as_view()  , name="post_detail"),
    path('post/<pk>/update', PostUpdateView.as_view(), name="post_update"),
    path('post/<pk>/delete', PostDeleteView.as_view(), name="post_delete"),

]