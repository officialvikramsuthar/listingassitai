from django.urls import path
from .views import BlogView, BlogList

urlpatterns = [
    path('<int:pk>/<str:slug>/', BlogView.as_view(), name='blog_detail'),
    path('', BlogList.as_view(), name='blog_list'),
]