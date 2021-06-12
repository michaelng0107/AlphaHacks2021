from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.UserList.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('lists/', views.ListView.as_view()),
    path('lists/<int:pk>/', views.ListDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
